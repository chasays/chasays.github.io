

>在 Stack Overflow 上有这样的一个贴子《What’s your most controversial programming opinion?》，翻译成中文就是“你认为最有争议的编程观点是什么？”，由 Jon Skeet 在 2009 年 1 月提出。此人可不是无名小卒，C#社区大名鼎鼎的人物，多年微软 MVP，所著《深入理解 C#》（英文版 C# in Depth）一书是 C#领域少数不可不读的名著，现在 Google 英国公司任工程师。不过，在 400 多个主回贴，以及千把个子回贴中，好像并不是很有争议，而是令人相当的茅塞顿开，下面罗列一些，并通过我自己的经历和理解发挥了一些，希望对你有帮助。

##  The only “best practice” you should be using all the time is “Use Your Brain”.

唯一的“Best Practice”并不是使用各种各样被前人总结过的各种设计方法、模式，框架，那些著名的方法、模式、框架只代码赞同他们的人多，并不代表他们适合你，你应该更多的去使用你的大脑，独立地思考那些方法、模式、框架出现的原因和其背后的想法和思想，那才是“Best Practice”。事实上来说，那些所谓的“Best Practice”只不过是限制那些糟糕的程序员们的破坏力。

## Programmers who don’t code in their spare time for fun will never become as good as those that do.

如果你对编程没有感到一种快乐，没有在你空闲的时候去以一种的轻松的方式去生活，无论是编程，还是运动，还是去旅游，只要你在没有从中感到轻松和愉快，那么你只不过是在应付它们。而你无时无刻不扎在程序堆中，这样下来，就算是你是一个非常聪明，非常有才华的人，你也不会成为一个优秀的编程员，要么只会平平凡凡，要么只会整天扎在技术中成为书呆子。当然，这个观点是有争议，热情和能力的差距也是很大的。不过我们可以从中汲取其正面的观点。

## Most comments in code are in fact a pernicious form of code duplication.

注释应该是注释 Why，而不是 How 和 What，参看《惹恼程序员的十件事》，代码告诉你 How，而注释应该告诉你 Why。但大多数的程序并不知道什么是好的注释，那些注释其实和 code 是重复的，毫无意义。

## XML is highly overrated

XML 可能被高估了。XML 对于 Web 上的应用是不错的，但是我们把其用到了各种地方，好像没有 XML，我们都不会编程了。

## Not all programmers are created equal

这是那些 junior 经理或是流程爱犯的错，他们总是认为，DeveloperA == DeveloperB，只要他们的 title 一样，他们以为他们的能力、工作速度、解决问题的方法，掌握的技能等等都是一样的。呵呵。更扯的是，在某些时候，就算是最差的程序员，因为 Title，他们也会认为其比别人强十倍，这就是很表面的愚蠢的管理。

## ”Googling it” is okay!

不可否认，查找知识是一种能力。但 Google 只会给你知识，并不会教给你技能。那里只有“鱼”，没有“渔”，过度的使用 Google，只会让你越来越离不开他，你越来越需要要它立马告诉你答案，而你越来越不会自己去思考，自己去探索，去专研。如果 KFC 快餐是垃圾食品对我们的身体没有好处，那么使用 Google 也一种快餐文化对我们的智力发展大大的没有好处。因为我们过度地关注了答案，而不是寻找答案的技术和过程。

## If you only know one language, no matter how well you know it, you’re not a great programmer.

如果你只懂一种语言，准确的说，如果你只懂一类语类，如：Java 和 C#，PHP 和 Perl，那么，你将会被局限起来，只有了解了各种各样的语言，了解了不同语言的不同方法 ，你才会有比较，只有了比较，你才会明白各种语言的长处和短处，才会让你有更为成熟的观点，而且不整天和别的程序在网上斗嘴争论是 Windows 好还是 Unix 好，是 C 好还是 C++好，有这点工夫能干好多事了。世界因为不同而精彩，只知道事物的一面是有害的。

## Your job is to put yourself out of work.

你的工作不是保守，那种教会徒弟，饿死师父的想法，不但是相当短浅的，而且还是相当脑残的。因为，在计算机世界里，你掌握的老技术越多，你就越没用，因为技术更新的太快。你对工作越保守，这个工作就越来越离不开你，你就越不越不能抽身去学新的东西，你也就越来越 OUT 了。记住：If you can’t be replaced then you can’t be promoted!

## Design patterns are hurting good design more than they’re helping it.

很多程序员把设计模式奉为天神，他们过度的追求设计模式以至都都忘了需求是什么，结果整个系统设计被设计模式搞得乱七八糟，我们叫这种编程为“设计模式驱动编程”，正如第一点所说，如果你不懂得用自己的大脑思考的话，知其然，不知所以然的话，那么你不但得不到其好处，反而受其所累。

## Unit Testing won’t help you write good code

其实，Unit Test 的主要目的是，为了防止你不会因为一个改动而引入 Bug，但这并不会让你能写出更好的代码。这只会让你写出不会出错的代码。同第一点，这样的方法，只不过是防止糟糕的程序员，而并不是让程序员或代码质量更有长进。反而，程序员通常会借用“通过 Unit Test”来为自己代码做辩解，而此时，Unit Test Report 成了一种托辞。

