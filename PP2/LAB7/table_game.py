import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

window_size = (450, 500)
cell_size = 150
    
font = pygame.font.SysFont("Courier New", 40)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Arnur Krasavchik")

class TableGame():
    def __init__(self, table_size):
        self.table_size = table_size
        self.cell_size = table_size // 3
        self.table = []
        self.player = "X"
        self.winner = None
        self.taking_move = True
        self.running = True
        self.background_color = (255, 174, 66)
        self.table_color = (50, 50, 50)
        self.line_color = (12, 12, 12)
        self.instruction_color = (23, 25, 25)
        self.game_over_color = (255, 0, 0)
        self.game_over_bg_color = (123, 65, 101)
        self.font = pygame.font.SysFont("Courier New", 40)
        self.FPS = pygame.time.Clock()

        for col in range(3):
            self.table.append([])
            for row in range(3):
                self.table[col].append("-")

    def main(self):
        screen.fill(self.background_color)
        self._draw_table()

        while self.running:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    if self.taking_move:
                        self._move(self.event.pos)



            pygame.display.flip()
            self.FPS.tick(60)

 
           
    def _draw_table(self):
        tb_space_point = (self.table_size // 10, self.table_size - (self.table_size // 10))
        cell_space_point = (self.cell_size, self.cell_size * 2)
        r1 = pygame.draw.line(screen, self.table_color, [tb_space_point[0], cell_space_point[0]], [tb_space_point[1], cell_space_point[0]], 8)
        c1 = pygame.draw.line(screen, self.table_color, [cell_space_point[0], tb_space_point[0]], [cell_space_point[0], tb_space_point[1]], 8)
        r2 = pygame.draw.line(screen, self.table_color, [tb_space_point[0], cell_space_point[1]], [tb_space_point[1], cell_space_point[1]], 8)
        c2 = pygame.draw.line(screen, self.table_color, [cell_space_point[1], tb_space_point[0]], [cell_space_point[1], tb_space_point[1]], 8)

    def _change_player(self):
        self.player = "O" if self.player == "X" else "X"
    
    def _draw_char(self, x, y, player):
        if self.player == "O":
            img = pygame.image.load("images/tictaktoe/Tc-O.png")
        else:
            img = pygame.image.load("images/tictaktoe/Tc-X.png")
        img = pygame.transform.scale(img, (self.cell_size, self.cell_size))
        screen.blit(img, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def _move(self, pos):
        try:
            x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
            if self.table[x][y] == "-":
                self.table[x][y] = self.player
                self._draw_char(x, y, self.player)
                self._game_check()
                self._change_player()
        except IndexError:
            print("Click inside the table only")
    
    def _game_check(self):
    
      for i in range(3):
        if self.table[i][0] == self.table[i][1] == self.table[i][2] != "-":  
            self.winner = self.table[i][0]
            self._game_over()
            return
        if self.table[0][i] == self.table[1][i] == self.table[2][i] != "-":  
            self.winner = self.table[0][i]
            self._game_over()
            return
      if self.table[0][0] == self.table[1][1] == self.table[2][2] != "-":

        self.winner = self.table[0][0]
        self._game_over()
        return
      if self.table[0][2] == self.table[1][1] == self.table[2][0] != "-": 
        self.winner = self.table[0][2]
        self._game_over()
        return

      draw = all(all(cell != "-" for cell in row) for row in self.table)
      if draw:
          self.winner = "Draw"
          self._game_over()
          return

    def _game_over(self):
      self.running = False
      print(self.winner)
      
    



if __name__ == "__main__":
    g = TableGame(window_size[0])
    g.main()
    