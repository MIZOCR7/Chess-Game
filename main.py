import pygame
from engine import Engine

pygame.init()

WIDTH = 800
HEIGHT = 800


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess Game")

game_state = Engine()
pieces = [
    'PawnW', 'RookW', 'KnightW', 'BishopW', 'KingW', 'QueenW',
    'PawnB', 'RookB', 'KnightB', 'BishopB', 'KingB', 'QueenB'
]

for piece in pieces:
  piece_img = pygame.image.load(f"assets/{piece}.png")
  piece_img = pygame.transform.scale(piece_img, (100,100))
  game_state.parts[piece] = piece_img



def background():
  image = pygame.image.load('assets/Board.png').convert_alpha()
  image = pygame.transform.scale(image, (WIDTH,HEIGHT))
  screen.blit(image, (0,0)) 


def main():
  pos_col = None
  pos_row = None
  run = True  
  
  
  
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          mouse_x, mouse_y = event.pos
          pos_row = mouse_y // 100
          pos_col = mouse_x // 100
          game_state.get_clicks(pos_row, pos_col)
    background()
    game_state.draw_pieces(screen)
    pygame.display.flip()
      

  pygame.quit()



if __name__ == '__main__':
  main()
