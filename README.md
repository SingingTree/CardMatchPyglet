# Introduction

This is a tutorial that incrementally builds up a card matching game that uses Pyglet. Each section of the tutorial aims to build to a new concept, and each section will correspond to a Python program in the repo.

The sections will build upon one another, and code may be reworked from section to section.

# card_match_v1.py

## Installing Pyglet

Before we can get started programming, we need to make sure Pyglet is installed and that Python can use it. The Pyglet [download page](https://bitbucket.org/pyglet/pyglet/wiki/Download) details how to install Pyglet:

```
pip install pyglet
```
 
Pyglet has [online documentation](https://bitbucket.org/pyglet/pyglet/wiki/Documentation) in case you ever need more info on it, or are having trouble. If you're unsure on which version of the docs to use, you probably want the stable ones.
 
## Creating a Window
 
To create a window in Pyglet we need to do a few things:

First we need to import Pyglet:

```python
import pyglet
```

This line of code tells our program to import Pyglet. We can then use the features of the Pyglet library, as we'll see below.

Next we can ask Pyglet to create a Window for us. To do this we need to call `pyglet.window.Window()`. This is the Window constructor, and it returns to us a Pyglet application window. We can assign that window to a varibale so we can use it later like this:

```python
window = pyglet.window.Window()
```

So that's all good and well, but we're not actually doing anything with our Window yet. So let's set up something for the window to do! We're going to set up a simple event. This event is going to make sure that every time the window is drawn it is cleared. What I mean by this is that before we draw content in the window, we clear the old content so we have a blank slate to draw on. It's not wildly exciting, but it's an important starting point. Anywho, we do that like this:

```python
@window.event
def on_draw():
    window.clear()
```

Let's break this down:

- The `@window.event` part is a special bit of information called a **decorator** in Python. These are used in Python to dress up functions and modify their behaviour. This decorator tells Python that the function following it is related to `window` (yep the same variable we created earlier), and is an event associated with that window. Decorators are pretty cool, but I'm not going to get into too much detail here.
- The `def on_draw():` part says we're declaring a function named `on_draw`. The name of this function is important, because Pyglet uses a combination the decorator from the previous line and our function name to determine when use our functions. The on_draw function is used every time the window needs to be drawn.
- The `window.clear()` part asks Pyglet to clear our window, which involves filling the window with black to get rid of anything that may have previously been drawn in it.

Putting it all together: we're creating a function that is going to be called every time our window is drawn. Pyglet knows this because of the decorator and function name. Every time our window is drawn this function makes sure it's filled with black.

We need one last thing before you can experience the glory of your new Pyglet application: we need to start the application running. We do this with the following code:

```python
pyglet.app.run()
```

This code asks Pyglet to start our application running. Pyglet handles a lot of complicated stuff to do with windows and graphics and all sorts of cool things, this is why we let it handle running of our application.

At this point your code should look something like [this](https://github.com/SingingTree/CardMatchPyglet/blob/master/card_match_v1.py)!