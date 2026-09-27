(function () {
  'use strict';

  var overlay = document.querySelector('.search-page');
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  var status = document.getElementById('search-status');
  var closeButton = document.querySelector('.search-icon-close');
  var form = document.getElementById('site-search-form');
  if (!overlay || !input || !results || !status || !closeButton) return;

  var indexUrl = "/search.json";
  var entries = null;
  var pending = null;
  var previousFocus = null;

  function clearResults() {
    while (results.firstChild) results.removeChild(results.firstChild);
  }

  function setStatus(message) {
    status.textContent = message;
  }

  function loadIndex() {
    if (entries) return Promise.resolve(entries);
    if (!pending) {
      pending = fetch(indexUrl, { credentials: 'same-origin' })
        .then(function (response) {
          if (!response.ok) throw new Error('Search index unavailable');
          return response.json();
        })
        .then(function (data) {
          if (!Array.isArray(data)) throw new Error('Invalid search index');
          entries = data;
          return entries;
        })
        .catch(function (error) {
          pending = null;
          throw error;
        });
    }
    return pending;
  }

  function score(entry, words) {
    var title = String(entry.title || '').toLocaleLowerCase();
    var subtitle = String(entry.subtitle || '').toLocaleLowerCase();
    var tags = String(entry.tags || '').toLocaleLowerCase();
    var total = 0;
    for (var i = 0; i < words.length; i++) {
      var word = words[i];
      if (title.indexOf(word) !== -1) total += title.indexOf(word) === 0 ? 6 : 4;
      else if (tags.indexOf(word) !== -1) total += 3;
      else if (subtitle.indexOf(word) !== -1) total += 1;
      else return 0;
    }
    return total;
  }

  function render(query) {
    clearResults();
    var words = query.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length) {
      setStatus('输入关键词，查找你感兴趣的文章。');
      return;
    }
    if (!entries) {
      setStatus('正在加载文章索引…');
      loadIndex().then(function () {
        if (input.value === query) render(query);
      }).catch(function () {
        if (input.value === query) setStatus('搜索暂时不可用，请稍后重试。');
      });
      return;
    }

    var found = entries.map(function (entry) {
      return { entry: entry, rank: score(entry, words) };
    }).filter(function (item) { return item.rank > 0; });
    found.sort(function (a, b) {
      return b.rank - a.rank || String(b.entry.date).localeCompare(String(a.entry.date));
    });
    setStatus(found.length ? '找到 ' + found.length + ' 篇相关文章' : '没有找到相关文章，试试其他关键词。');
    found.slice(0, 20).forEach(function (item) {
      var article = document.createElement('article');
      article.className = 'search-result';
      var link = document.createElement('a');
      link.href = item.entry.url;
      var meta = document.createElement('span');
      meta.className = 'search-result-meta';
      meta.textContent = [item.entry.date, item.entry.tags].filter(Boolean).join(' · ');
      var title = document.createElement('strong');
      title.textContent = item.entry.title || '未命名文章';
      link.appendChild(meta);
      link.appendChild(title);
      if (item.entry.subtitle) {
        var subtitle = document.createElement('span');
        subtitle.className = 'search-result-subtitle';
        subtitle.textContent = item.entry.subtitle;
        link.appendChild(subtitle);
      }
      article.appendChild(link);
      results.appendChild(article);
    });
  }

  function openSearch() {
    previousFocus = document.activeElement;
    overlay.classList.add('search-active');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.classList.add('search-is-open');
    input.focus();
    if (input.value.trim()) render(input.value);
  }

  function closeSearch() {
    overlay.classList.remove('search-active');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('search-is-open');
    if (previousFocus && previousFocus.focus) previousFocus.focus();
  }

  document.querySelectorAll('.search-icon a, .search-open-button').forEach(function (trigger) {
    trigger.addEventListener('click', function (event) {
      event.preventDefault();
      openSearch();
    });
  });
  closeButton.addEventListener('click', closeSearch);
  input.addEventListener('input', function () { render(input.value); });
  if (form) form.addEventListener('submit', function (event) { event.preventDefault(); });
  overlay.addEventListener('click', function (event) {
    if (event.target === overlay) closeSearch();
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && overlay.classList.contains('search-active')) closeSearch();
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault();
      if (overlay.classList.contains('search-active')) closeSearch();
      else openSearch();
    }
  });
})();
