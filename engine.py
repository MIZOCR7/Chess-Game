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
    self.selected_square = ()
    self.player_clicks = []
  
  def get_box_dimensions(self):
    box_width = self.scaled.get_width() // 8
    box_height = self.scaled.get_height() // 8
    
    return box_width, box_height 

  def draw_pieces(self, screen):
    for x in range(8):
      for y in range(8):
        piece = self.data[y][x]
        if piece != "--":
          image = self.parts[piece]
          screen.blit(image, (x * 100, y * 100))
  
  def get_clicks(self, row, col):
        if len(self.player_clicks) == 0:
            if self.data[row][col] != '--':
              piece_color = self.data[row][col][-1]
              if (self.role == "white" and piece_color == "W") or (self.role == "black" and piece_color == "B"):
                self.player_clicks.append((row, col))
                self.selected_square = (row, col)
                
        elif len(self.player_clicks) == 1:
            if (row, col) == self.selected_square:
                self.player_clicks.clear()
                self.selected_square = ()
                
            else:
                self.player_clicks.append((row, col))
                
     
        if len(self.player_clicks) == 2:
            start_row, start_col = self.player_clicks[0]
            end_row, end_col = self.player_clicks[1]

            
            self.data[end_row][end_col] = self.data[start_row][start_col]
            
          
            self.data[start_row][start_col] = '--'
            if self.role == "white":
              self.role = "black"
            else:
              self.role = "white"
          
            self.player_clicks.clear()
            self.selected_square = ()
  
  def pawn_move(self):
    pass 
      
    
        


