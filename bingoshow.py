"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import bingocheck
import numpy as np
from screeninfo import get_monitors

m = get_monitors()
print(m)
SCREEN_WIDTH = m[0].width
SCREEN_HEIGHT = m[0].height
SCREEN_MARGIN_VER = SCREEN_HEIGHT//6
SCREEN_MARGIN_HOR = SCREEN_WIDTH//6
WIDTH, HEIGHT = SCREEN_MARGIN_VER//2, SCREEN_MARGIN_VER//2
SCREEN_TITLE = "BINGO"


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.bingo_boards = bingocheck.test_board_two
        self.bingo_list = bingocheck.test_list
        self.nb_boards = len(self.bingo_boards)
        self.rows = len(self.bingo_boards[0])
        self.columns = len(self.bingo_boards[0, 0])
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        for i in range(len(self.bingo_boards)):
            self.draw_board(self.bingo_boards[i], i)
        self.draw_list(self.bingo_list)
        with open('bingolist.txt', 'w') as f:
            for item in self.bingo_list:
                f.write("%s\n" % item)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        while True:
            try:
                inp = int(input("> "))
                break
            except Exception as e:
                print("try again", e)
        if inp in self.bingo_list:
            self.bingo_list.remove(inp)
        else:   
            self.bingo_list.append(inp)


    def draw_board(self, board, i):
        for row in range(self.rows):
            for column in range(self.columns):
                data = board[row, column]
                x = (i * self.columns * WIDTH * 2) + (WIDTH) * column + SCREEN_MARGIN_HOR + WIDTH // 2
                y = (HEIGHT) * row + SCREEN_MARGIN_VER//2 + HEIGHT // 2

                if data in self.bingo_list:
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, arcade.color.GREEN)
                    arcade.draw_text(str(data), x, y, arcade.color.BLACK, 30, align="center", anchor_x="center", anchor_y="center", bold=True)
                else:
                    arcade.draw_rectangle_outline(x, y, WIDTH, HEIGHT, arcade.color.WHITE)
                    arcade.draw_text(str(data), x, y, arcade.color.WHITE, 30, align="center", anchor_x="center", anchor_y="center", bold=True)
                
    def draw_list(self, liste):
        for i in range(len(liste)):
            x = SCREEN_MARGIN_HOR//2 + i%20 * WIDTH
            y = SCREEN_HEIGHT - SCREEN_MARGIN_VER//2 - i//20*WIDTH
            arcade.draw_rectangle_outline(x, y, WIDTH, HEIGHT, arcade.color.WHITE)
            arcade.draw_text(str(liste[i]), x, y, arcade.color.WHITE, 30, align="center", anchor_x="center", anchor_y="center", bold=True)

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()
    i = input("test")


if __name__ == "__main__":
    main()