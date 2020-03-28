import arcade
import bingocheck
import numpy as np
from screeninfo import get_monitors

m = get_monitors()
SCREEN_WIDTH = m[0].width
SCREEN_HEIGHT = m[0].height-(m[0].height//6)
SCREEN_TITLE = "BINGO"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.bingo_boards = bingocheck.test_board_two
        self.bingo_list = []
        self.nb_boards = len(self.bingo_boards)
        self.rows_per_board = len(self.bingo_boards[0])
        self.columns_per_board = len(self.bingo_boards[0, 0])

        MAX_BOARDS_PER_ROW = self.get_optimal_boards_per_row()


        self.columns_of_boards = MAX_BOARDS_PER_ROW if self.nb_boards >= MAX_BOARDS_PER_ROW else self.nb_boards
        self.rows_of_boards = 1 + (self.nb_boards-1) // MAX_BOARDS_PER_ROW

        self.new_numbers_list_height = SCREEN_HEIGHT//4

        self.nb_cells_x = self.columns_of_boards*self.columns_per_board + self.columns_of_boards + 1
        self.nb_cells_y = self.rows_of_boards*self.rows_per_board + self.rows_of_boards + 1 

        self.cell_size = min((SCREEN_HEIGHT-self.new_numbers_list_height)//self.nb_cells_y, SCREEN_WIDTH//self.nb_cells_x)

        self.new_numbers_list_cells_per_row = (SCREEN_WIDTH // self.cell_size) - 2
        self.board_size_x = self.columns_per_board * self.cell_size
        self.board_size_y = self.rows_per_board * self.cell_size


    def setup(self):
        pass

    def get_optimal_boards_per_row(self):
        if self.nb_boards <= 12:
            return 6
        elif self.nb_boards <= 30:
            return 10
        else:
            return 12

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        list_of_boards_with_bingo = [[0] for _ in range(self.rows_per_board)]
        
        for i in range(len(self.bingo_boards)):
            self.draw_board(self.bingo_boards[i], i, list_of_boards_with_bingo)
        self.draw_list(self.bingo_list)
        self.draw_bingo_string(list_of_boards_with_bingo)
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


    def draw_board(self, board, i, boards_with_bingo_list):
        base_x = ((i % self.columns_of_boards)+1) * self.cell_size + (i % self.columns_of_boards) * self.board_size_x
        base_y = SCREEN_HEIGHT - self.new_numbers_list_height - ((i // self.columns_of_boards) + 1) * self.cell_size - (i // self.columns_of_boards) * self.board_size_y
        
        for row in range(self.rows_per_board):
            for column in range(self.columns_per_board):
                data = board[row, column]
                x = base_x + (self.cell_size * column)
                y = base_y - (self.cell_size * row)
                if row == 0:
                    arcade.draw_text("BINGO"[column], x, y + self.cell_size, arcade.color.ORANGE, self.cell_size//2, align="center", anchor_x="center", anchor_y="center", bold=True)
                if data in self.bingo_list:
                    arcade.draw_rectangle_filled(x, y, self.cell_size, self.cell_size, arcade.color.GREEN)
                    arcade.draw_text(str(data), x, y, arcade.color.BLACK, self.cell_size//2, align="center", anchor_x="center", anchor_y="center", bold=True)
                else:
                    arcade.draw_rectangle_outline(x, y, self.cell_size, self.cell_size, arcade.color.WHITE)
                    arcade.draw_text(str(data), x, y, arcade.color.WHITE, self.cell_size//2, align="center", anchor_x="center", anchor_y="center", bold=True)
        
        bingos = bingocheck.check_board(board, self.bingo_list)
        if bingos:
            boards_with_bingo_list[bingos].append(i+1)


    def draw_list(self, liste):
        for i in range(len(liste)):
            x = self.cell_size*(i % 20 + 1)
            y = SCREEN_HEIGHT - self.cell_size - (i//20)*self.cell_size
            arcade.draw_rectangle_outline(x, y, self.cell_size, self.cell_size, arcade.color.WHITE)
            arcade.draw_text(str(liste[i]), x, y, arcade.color.WHITE, self.cell_size//2, align="center", anchor_x="center", anchor_y="center", bold=True)


    def draw_bingo_string(self, list_of_boards_with_bingo):
        text_to_draw = ''
        for i in range(len(list_of_boards_with_bingo)-1, 0, -1):
            l = len(list_of_boards_with_bingo[i])
            if l > 1:
                if l > 2:
                    text_to_draw += "BINGO x" + str(i) + " on boards " + str(list_of_boards_with_bingo[i])
                else:
                    text_to_draw += "BINGO x" + str(i) + " on board " + str(list_of_boards_with_bingo[i][-1]) + "!!"
        if text_to_draw:
            arcade.draw_text(text_to_draw, self.cell_size, self.cell_size//2, color=arcade.color.GREEN, font_size=self.cell_size // 3, align='center')

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()