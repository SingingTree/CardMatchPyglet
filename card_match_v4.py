import pyglet


class Card:
    def __init__(self, left, bottom, width, height):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height

    def draw_card(self):
        pyglet.graphics.draw(4,
                             pyglet.gl.GL_QUADS,
                             ('v2i', (self.get_card_vertices()))
                             )

    def get_card_vertices(self):
        card_vertices = [
            self.left, self.bottom,
            self.left, self.bottom + self.height,
            self.left + self.width, self.bottom + self.height,
            self.left + self.width, self.bottom
        ]
        return card_vertices

    def contains_point(self, point_x, point_y):
        return (self.left < point_x < self.left + self.width and
                self.bottom < point_y < self.bottom + self.height)


def get_window_width():
    return 600


def get_window_height():
    return 400


def get_card_width():
    return 300


def get_card_height():
    return 200


def on_mouse_press(x, y, button, modifiers):
    print("Mouse Pressed")
    for i, card in enumerate(cards):
        if card.contains_point(x, y):
            print("Clicked inside card {}".format(i))


# Create a Pyglet Window
window = pyglet.window.Window(get_window_width(), get_window_height())
window.push_handlers(on_mouse_press)
cards = [Card(0, 0, get_card_width(), get_card_height()),
         Card(get_card_width(), get_card_height(), get_card_width(), get_card_height())]

# Set up our window event handlers, we need to do this before we start our app running
@window.event
def on_draw():
    window.clear()
    for card in cards:
        card.draw_card()

# Start the app running!
pyglet.app.run()
