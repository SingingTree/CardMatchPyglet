import pyglet


def draw_card():
    pyglet.graphics.draw(4,
                         pyglet.gl.GL_QUADS,
                         ('v2i', (get_card_vertices()))
                         )


def get_card_vertices():
    card_width = 200
    card_height = 200
    card_vertices = [
        0, 0,
        0, card_height,
        card_width, card_height,
        card_width, 0
    ]
    return card_vertices

# Create a Pyglet Window
window = pyglet.window.Window()


# Set up our window event handlers, we need to do this before we start our app running
@window.event
def on_draw():
    window.clear()
    draw_card()

# Start the app running!
pyglet.app.run()
