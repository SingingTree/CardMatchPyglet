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
                          (get_translated_vertices(window, 0, 0))
                          )
                         )


def get_card_buffer():
    return 50


def get_card_scale(window):
    window_size = window.get_size()
    # Double / performs integer division
    return window_size[0] // 4, window_size[1] // 3


def get_scaled_vertices(window):
    scale = get_card_scale(window)
    scaled_vertices = []
    for i in range(0, len(card_vertices), 2):
        scaled_vertices.append(card_vertices[i] * scale[0])
        scaled_vertices.append(card_vertices[i + 1] * scale[1])
    return scaled_vertices


def get_translated_vertices(window, card_row, card_col):
    card_scale = get_card_scale(window)
    scaled_vertices = get_scaled_vertices(window)
    translated_vertices = []
    for i in range(0, len(scaled_vertices), 2):
        translated_vertices.append(scaled_vertices[i] + card_scale[0] * card_col + get_card_buffer() * (card_col + 1))
        translated_vertices.append(scaled_vertices[i + 1] + card_scale[1] * card_row + get_card_buffer() * (card_row + 1))
    return translated_vertices


window = pyglet.window.Window()

# Set up event handlers
# We need to do this after declaring the variables the handlers use
# but before we start running the app
@window.event
def on_draw():
    window.clear()
    draw_card(window)


pyglet.app.run()
