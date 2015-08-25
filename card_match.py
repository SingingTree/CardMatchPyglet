import pyglet


def draw_card():
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                         ('v2i',
                          (10, 15,
                           10, 35,
                           20, 35,
                           20, 15)
                          )
                         )


window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')


# Set up event handlers
# We need to do this after declaring the variables the handlers use
# but before we start running the app
@window.event
def on_draw():
    window.clear()
    label.draw()
    draw_card()


pyglet.app.run()
