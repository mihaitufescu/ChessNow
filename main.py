import arcade
import arcade.gui
import config
import loadCharacters as lC

ROWS = -1
COLUMNS = -1
WIDTH_CELL = -1
HEIGHT_CELL = -1
MARGIN = -1
SCREEM_WIDTH = (WIDTH_CELL + MARGIN) * ROWS + MARGIN
SCREEM_HEIGHT = (HEIGHT_CELL + MARGIN) * COLUMNS + MARGIN
CHARACTER_SCALING = -1
ROWS,COLUMNS,WIDTH_CELL,HEIGHT_CELL,MARGIN,SCREEM_WIDTH,SCREEM_HEIGHT,CHARACTER_SCALING = config.config_size(ROWS,COLUMNS,WIDTH_CELL,HEIGHT_CELL,MARGIN,SCREEM_WIDTH,SCREEM_HEIGHT,CHARACTER_SCALING)

class gameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super(gameWindow, self).__init__(width, height, title, resizable=False)
        self.set_location(400, 100)
        self.grid = []
        for row in range(ROWS):
            self.grid.append([])
            for column in range(COLUMNS):
                self.grid[row].append(0)
        arcade.set_background_color(arcade.color.BLACK)
        self.player_list = None
        self.player_sprite = None
        print(arcade.get_projection())

    def setup(self):
        self.player_list = arcade.SpriteList()
        loaded = False
        i = 0
        while loaded == False:
            if i==11:
                loaded = True
            image_source = lC.loadFiles(i)
            print(image_source)
            if i<12:
                coords = lC.loadPiece(i)
                if i==4 or i==5 or i==6 or i==7:
                    self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
                    self.player_sprite.center_x = coords[0]
                    self.player_sprite.center_y = coords[1]
                    self.player_list.append(self.player_sprite)
                elif i==10:
                    j = 0
                    coords = lC.loadPiece(i)
                    while(j<8):
                        tempX = coords[0] + 37.8*(2*j) + 5*(2*j)
                        tempY = coords[1]
                        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
                        self.player_sprite.center_x = tempX
                        self.player_sprite.center_y = tempY
                        self.player_list.append(self.player_sprite)
                        j+=1
                elif i==11:
                    j = 0
                    coords = lC.loadPiece(i)
                    while (j < 8):
                        tempX = coords[0] + 37.8 * (2 * j) + 5 * (2 * j)
                        tempY = coords[1]
                        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
                        self.player_sprite.center_x = tempX
                        self.player_sprite.center_y = tempY
                        self.player_list.append(self.player_sprite)
                        j += 1
                else:
                    self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
                    self.player_sprite.center_x = coords[0]
                    self.player_sprite.center_y = coords[1]
                    self.player_list.append(self.player_sprite)
                    self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
                    self.player_sprite.center_x = coords[2]
                    self.player_sprite.center_y = coords[3]
                    self.player_list.append(self.player_sprite)
            i+=1

    def on_draw(self):
        arcade.start_render()
        for row in range(ROWS):
            for column in range(COLUMNS):
                if (row + column) % 2 == 0:
                    color = arcade.color.BEIGE
                else:
                    color = arcade.color.COFFEE
                x = (MARGIN + WIDTH_CELL) * column + MARGIN + WIDTH_CELL // 2
                y = (MARGIN + HEIGHT_CELL) * row + MARGIN + HEIGHT_CELL // 2
                arcade.draw_rectangle_filled(x, y, WIDTH_CELL, HEIGHT_CELL, color)
        self.player_list.draw()


def main():
    window = gameWindow(SCREEM_WIDTH, SCREEM_HEIGHT, "chessNow")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
