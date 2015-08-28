import pyglet


card_vertices = [
    0, 0,
    0, 1,
    1, 1,
    1, 0
]


def draw_card(window):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                         ('v2i',
                          (get_scaled_vertices(window))
                          )
                         )


def get_scale(window):
    return 100, 100  # Place holder


def get_scaled_vertices(window):
    scale = get_scale(window)
    scaled_vertices = []
    for i in range(0, len(card_vertices), 2):
        scaled_vertices.append(card_vertices[i] * scale[0])
        scaled_vertices.append(card_vertices[i + 1] * scale[1])
    return scaled_vertices


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
    draw_card(window)


pyglet.app.run()
