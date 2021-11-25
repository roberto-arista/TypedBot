# TypedBot
A type annotated wrapper around [DrawBot](https://www.drawbot.com)

## FAQs

+ First of all, why? Don't we already have DrawBot?

    During the last year, I started to study and use Swift. It's not so hard to learn if you come from Python, the syntax is quite similar, but you have to get used to handling types. That's a bit annoying at the beginning, but it has its own advantages. In a way, it made me realize that I often write crappy Python code (unwrapping optionals? what's that?).

    Handling types is frustrating because you get all these annoying error messages from your IDE, like "this function might return a None value, are you prepared for that?". It slows you down and it forces you to cast ints as floats for a `sin()` function and other things only meaningful to Computer Science people. At the same time, all these annoying messages risk becoming errors at runtime. And it sucks if you are going to distribute the code to other users. Bugs mean extra complaints and less confidence. Bad for users and developers.

    How can I get some extra confidence in writing my code while using Python? I like Swift, but Python is useful, especially for font development work. Maybe I can get a similar experience to writing Swift by adding type annotations to Python code. But, you can't check annotations where they do not exist. And most of the packages I use for my own work do not have annotations. So, I screamed to the sky: «I will add annotations to DrawBot!»

    Well, that's not so easy. Let's start with a wrapper around DrawBot, then we'll see.
    
+ What is DrawBot?

    I usually present DrawBot to non-type people in this way: "It is a cousin of Processing, but: (1) you write Python code, (2) it handles text and vectors super well with powerful APIs like `BezierPath` and `FormattedString`, (3) it's not meant for real-time interaction". Quoting from the DrawBot home page:
    
    > DrawBot is a powerful, free application for macOS that invites you to write simple python scripts to generate two-dimensional graphics. 

    DrawBot is © by Erik van Blokland, Just van Rossum, Frederik Berlaen

+ Why a wrapper?

    Consider that the DrawBot API makes extensive use of duck typing in the way it structures its API. For example, when you pass a coordinate to a function like [`text(txt, (x, y), align=None)`](https://www.drawbot.com/content/text/drawingText.html?highlight=text#drawBot.text), DrawBot does not really care if you pass a `tuple`, a `list`, a `namedtuple`, a class acting like a sequence (like a custom `Vector` class). DrawBot says «Two numbers? Cool, I need nothing more, let's draw». That's very cool and flexible, but flexibility sometimes can lead to bugs. Annotating this kind of API might be difficult and it can generate ugly code. And I don't really want my contribution to DrawBot to be remembered for being ugly 🥲.

+ Wait, did you say Duck Typing? Like the animal?

    "If it walks like a duck and it quacks like a duck, then it must be a duck" see [1](https://en.wikipedia.org/wiki/Duck_typing) and [2](https://i.stack.imgur.com/DNeRD.jpg)

+ Type annotations are an interesting topic, I want to know more.

    You can start read a few PEPs related to type annotatios:
    + [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
    + [PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)
    + [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/)

    I have also found these talks useful:
    - [Gradual Typing in Practice](https://www.youtube.com/watch?v=Lj_9TyT3V98)
    - [Bernat Gabor - Type hinting (and mypy) - PyCon 2019](https://www.youtube.com/watch?v=hTrjTAPnA_k)

+ If type annotations are not checked at runtime, how do I know if I am doing something wrong?

    You need to use a static type checker, like [mypy](http://mypy-lang.org) or [pyre](https://pyre-check.org). You could tie the static type checker to your favorite code editor linter functionality. I use [SublimeText](https://www.sublimetext.com) with the [SublimeLinter](http://www.sublimelinter.com/en/stable/) plugin. You can install mypy as [extension](https://github.com/fredcallaway/SublimeLinter-contrib-mypy) for the SublimeLinter plugin. In my experience, in a similar way to unit tests, type annotations are extremely helpful during refactoring.

+ Ok, sold. I want to try it. How can I install it?

    `pip install git+https://github.com/roberto-arista/TypedBot`

    Be aware, it's the first package I release, so I probably did something wrong in `setup.py` or similar. Open an issue if something goes wrong and I'll try to figure out a solution.

+ Wait, is this stable? Can I use it in production?

    Yes, no, almost. DrawBot is stable and well tested. TypedBot, not yet. Some tests are still failing, and part of the DrawBot API is not annotated yet (see imageObject). I am using this module in a couple of projects and the experience acquired will probably push me to adjust or change some things. IMHO you can use it, but you need to be a bit flexible

+ Is the TypedBot API equivalent to the DrawBot API?

    Not completely. Type annotations syntax allows to annotate functions and methods of any kind in Python, but the result is not always great code. Considering that this wrapper is separate from drawBot and that it does not break any existing functionality, I decided to change a few things to make the source code easier and cleaner.

+ Ok, so how do I know what differs between the two APIs?

    The source code of TypedBot and the DrawBot docs are the best references.

+ This project is cool, I want to help you. How can I contribute to it?

    That's great! Right now I see three areas where I could need some help:
    + Some tests are still failing. I'll work on these, but if you have time to figure out what's wrong, be my guest!
    + It would be nice to have some docs online. I don't know what these docs should show, probably each method should have a link to the drawBot's original version and the annotations.
    + Part of the API is not annotated yet. For example the `imageObject`. It has a large API (about 100 methods?) and I seldom use it. So, it's not my priority to annotate it.

    If you want to contribute, I suggest to:
    + fork the repo
    + clone it on your machine
    + install it locally in editable mode with pip
    ```
    cd path/to/cloned/repo
    pip install -e .
    ```

+ What about the license?

    TypedBot has the same license as DrawBot, so you can use it wherever you use DrawBot
