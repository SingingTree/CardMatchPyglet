"""Simple code for a card matching game

This code is meant to serve as an example of getting going with Pyglet. It's intended to be simplified, so it's
missing some style and things are coded in a way that hopefully makes things clear, but may not be the best way.

The game is also not fully functional, this code just draws the cards.

More code is to follow with the game becoming more fleshed out and complex, but this code stands as a minimal
reference to getting stuff drawing with Pyglet
"""

import pyglet

card_width = 200
card_height = 200
inter_card_buffer = 25

card_vertices = [
    0,          0,
    0,          card_height,
    card_width, card_height,
    card_width, 0
]

""" The numbers at each position of the board
When drawing this the first row (the row containing the 1s) will be drawn below the second
This is because for each row we increase the y coordinate and in pyglet increasing the y coordinate puts things
further up the screen
"""
board = [[1, 1],
         [2, 2]]


"""Draws the nuber labels for each card"""
def draw_card_labels():
     for row in range(2):
        for col in range(2):
            x_pos = col * card_width + inter_card_buffer * col + card_width // 2
            y_pos = row * card_height + inter_card_buffer * row + card_height // 2

            label = pyglet.text.Label(str(board[row][col]),
                          font_name='Times New Roman',
                          font_size=36,
                          x=x_pos, y=y_pos,
                          anchor_x='center', anchor_y='center',
                          color=(255, 0, 255, 255))
            label.draw()


"""Draws the 4 cards"""
def draw_cards():
    for row in range(2):
        for col in range(2):
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                                 ('v2i',
                                 (get_translated_vertices(row, col))
                                 )
                                )


""" Returns a list of vertices for the card at a given row and column"""
def get_translated_vertices(card_row, card_col):
    translated_vertices = []
    for i in range(0, len(card_vertices), 2):
        translated_vertices.append(card_vertices[i]
                                   + card_width * card_col
                                   + inter_card_buffer * card_col)
        translated_vertices.append(card_vertices[i + 1]
                                   + card_height * card_row
                                   + inter_card_buffer * card_row)
    return translated_vertices


window = pyglet.window.Window()


# Set up event handlers
# We need to do this after declaring the variables the handlers use
# but before we start running the app
@window.event
def on_draw():
    window.clear()
    draw_cards()
    draw_card_labels()


# Start the app running
# This hands control to Pyglet, which then uses the event handlers we set up earlier
pyglet.app.run()
