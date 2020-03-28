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
SCREEN_WIDTH = m[0].width
SCREEN_HEIGHT = m[0].height-(m[0].height//6)
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
        self.bingo_list = []
        self.nb_boards = len(self.bingo_boards)
        self.rows_per_board = len(self.bingo_boards[0])
        self.columns_per_board = len(self.bingo_boards[0, 0])

        self.columns_of_boards = 5 if self.nb_boards >= 5 else self.nb_boards
        self.rows_of_boards = 1 + self.nb_boards // 5

        self.screen_margin_vertical = SCREEN_HEIGHT//12
        self.screen_margin_horizontal = SCREEN_WIDTH//10

        self.new_numbers_list_height = SCREEN_HEIGHT//4
        self.board_size_x = (SCREEN_WIDTH - (1 + self.columns_of_boards) * self.screen_margin_horizontal) // (self.columns_of_boards)

        self.cell_width, self.cell_height = self.board_size_x//self.rows_per_board, self.board_size_x//self.rows_per_board

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        
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
        base_x = (1 + i % self.columns_of_boards) * self.screen_margin_horizontal + (i * self.board_size_x)
        base_y = (i // 5 + 1) * self.screen_margin_vertical + ((i//5)  * self.board_size_x)
        for row in range(self.rows_per_board):
            for column in range(self.columns_per_board):
                data = board[row, column]
                x = base_x + (self.cell_width * column)
                y = base_y + (self.cell_width * row)

                if data in self.bingo_list:
                    arcade.draw_rectangle_filled(x, y, self.cell_width, self.cell_height, arcade.color.GREEN)
                    arcade.draw_text(str(data), x, y, arcade.color.BLACK, self.cell_width//2, align="center", anchor_x="center", anchor_y="center", bold=True)
                else:
                    arcade.draw_rectangle_outline(x, y, self.cell_width, self.cell_height, arcade.color.WHITE)
                    arcade.draw_text(str(data), x, y, arcade.color.WHITE, self.cell_width//2, align="center", anchor_x="center", anchor_y="center", bold=True)
                
    def draw_list(self, liste):
        for i in range(len(liste)):
            x = self.screen_margin_horizontal//2 + i%20 * self.cell_width
            y = SCREEN_HEIGHT - self.screen_margin_vertical//2 - i//20*self.cell_width
            arcade.draw_rectangle_outline(x, y, self.cell_width, self.cell_height, arcade.color.WHITE)
            arcade.draw_text(str(liste[i]), x, y, arcade.color.WHITE, self.cell_width//2, align="center", anchor_x="center", anchor_y="center", bold=True)

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()