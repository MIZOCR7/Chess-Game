import pygame


class Engine():
  def __init__(self):
    self.background = pygame.image.load("assets/board.png")
    self.scaled = pygame.transform.scale(self.background, (800,800))
    self.role = "white"
    self.data = [
    ["RookB", "KnightB", "BishopB", "QueenB", "KingB", "BishopB", "KnightB", "RookB"],  
    ["PawnB", "PawnB", "PawnB", "PawnB", "PawnB", "PawnB", "PawnB", "PawnB"],        
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["PawnW", "PawnW", "PawnW", "PawnW", "PawnW", "PawnW", "PawnW", "PawnW"],         
    ["RookW", "KnightW", "BishopW", "QueenW", "KingW", "BishopW", "KnightW", "RookW"]  
]
    self.parts = {}
  
  def get_box_dimensions(self):
    box_width = self.scaled.get_width() // 8
    box_height = self.scaled.get_height() // 8
    
    return box_width, box_height 

  def draw_pieces(self, screen):
    index = 0 
    for x in range(8):
      for y in range(8):
        piece = self.data[y][x]
        if piece != "--":
          image = pygame.image.load(f"assets/{piece}.png")
          image = pygame.transform.scale(image, (100, 100))
          screen.blit(image, (x * 100, y * 100))
          pygame.display.update()
        


