import pyglet

# Create a Pyglet Window
window = pyglet.window.Window()

# Set up our window event handlers, we need to do this before we start our app running
@window.event
def on_draw():
    window.clear()

# Start the app running!
pyglet.app.run()
