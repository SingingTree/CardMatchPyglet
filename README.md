# Table of Contents

  * [Table of Contents](#table-of-contents)
  * [Introduction](#introduction)
  * [card\_match\_v1\.py](#card_match_v1py)
    * [Installing Pyglet](#installing-pyglet)
    * [Creating a Window](#creating-a-window)
  * [card\_match\_v2\.py](#card_match_v2py)
    * [Coordinates](#coordinates)



# Introduction

This is a tutorial that incrementally builds up a card matching game that uses Pyglet. Each section of the tutorial aims to build to a new concept, and each section will correspond to a Python program in the repo.

The sections will build upon one another, and code may be reworked from section to section.

# card_match_v1.py

We're going to get started by making a program that creates an empty window. Onward!

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

And the output should look like this:

![card_match_v1_screenshot1](https://github.com/SingingTree/CardMatchPyglet/blob/master/images/card_match_v1_screenshot1.png "card_match_v1")

# card_match_v2.py

Next up we're going to draw a rectangle in the window. This is all setting the foundation for drawing cards and other stuff. Let's go!

## Coordinates

In computer graphics you'll come across various coordinate systems. For Pyglet we work with on where the bottom left of the window is the origin. The origin is the point where the x coordinate is 0, and the y coordinate is 0. I'll typically use the notation (0,0) for this, meaning x = 0, followed by y = 0.
 
As we move right across the window the x coordinate will increase, and as we move further up the window the y coordinate will increase. So the top right corner of the window is where x and y are both at their greatest. What the value of x and y are at this point is determined by how big the window is in pixels. So if our window is 800 (wide) by 600 pixels (high), the top right corner will be (800,600).
 
![coordinate_example1](https://github.com/SingingTree/CardMatchPyglet/blob/master/images/coordinate_example1.png "coordinate_example1")

## Vertices

A **vertex** is like a point. But a vertex is a special kind of point at the edge of a shape. They plural of vertex is vertices: one vertex, to vertices.

Anywho, the image below shows what I mean about vertices being a special kind of point. If we have a square, and we take points along it's edges, then we can find lots of points, but it's only points at the corners that are considered vertices!

![vertices_example1](https://github.com/SingingTree/CardMatchPyglet/blob/master/images/vertices_example1.png "vertices_example1")

So a vertex is just like a point, and you can represent it in the same way: two numbers, one for the x coordinate, and one for the y. Or if we were in three dimensions we'd have 3 numbers, but we're not worried about that in this tutorial!

For Pyglet (and many other libraries) we'll store our vertices in a list. This list will just be a series of numbers, and each 2 numbers will make up a vertex. So if my list is [0, 10, 20, 20] then I have two vertices, the first is (0, 10) and the second is (20, 20).

## Drawing a Rectangle

Armed with our knowledge from above we can get started on drawing a rectangle! Let's start by writing a function which is going to return our vertices:

```python
def get_card_vertices():
    card_width = 200
    card_height = 200
    card_vertices = [
        0,          0,
        0,          card_height,
        card_width, card_height,
        card_width, 0
    ]
    return card_vertices
```

So the `card_vertices` array contains x and y coordinates for 4 vertices, and I've split those to one set of x and y per line so it's readable. I could put them all on one line and it'd work the same, but I find it makes it hard to me to know which numbers belong to which vertex. We could potentially have this logic outside of a function, but having in a function will give us some flexibility later on, and I think it's just good style. So there.

How do we use these vertices? We give them to Pyglet and tell it to draw stuff! This is probably the most complicated part thus far. Pyglet uses a library called OpenGL under the hood. OpenGl is pretty rad, I used to program in OpenGL for a living as a game dev. That said, OpenGL can get pretty freakin' complicated. I say this not to intimidate or humble brag (straight up brag: I'm pretty amazing), but to indicate that it's okay if you find stuff tricky or unintuitive.

Anywho, we'll use the following to rectangle (card):

```python
def draw_card():
    pyglet.graphics.draw(4,
                         pyglet.gl.GL_QUADS,
                         ('v2i', (get_card_vertices()))
                         )
```

Breaking this down:

- We're calling the `pyglet.graphics.draw` function to draw stuff and giving it a number of arguments.
- The 1st argument is the number of vertices we're drawing.
- The 2nd argument is the type of thing we're drawing. In this case `pyglet.gl.GL_QUADS means we're drawing a thing with 4 sides. All the GLs in there refer to OpenGL.
- The 3rd argument is the vertex data, and is a tuple made up of two things:
    - The first thing is a string saying what format our vertex data is in. `v2i` says our vertices are made up of 2 components, and those components are integers.
    - The second thing is the actual numbers that make up our vertices.
    
And putting this all together with what we've already worked on, we can put this into the `on_draw` function for our window, so that it looks like this:

```python
@window.event
def on_draw():
    window.clear()
    draw_card()
```

After which you should have a program that looks a little something like this](https://github.com/SingingTree/CardMatchPyglet/blob/master/card_match_v2.py)!

