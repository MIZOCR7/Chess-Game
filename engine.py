import pygame

class Engine():
  def __init__(self):
    self.background = pygame.image.load("assets/Board.png")
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
    self.light = pygame.Surface((100, 100), pygame.SRCALPHA)
    for r in range(35, 0, -1):
      pygame.draw.circle(self.light, (0, 255, 0, int(120 * (1 - r/35)**2)), (50, 50), r)
  
  def get_box_dimensions(self):
    box_width = self.scaled.get_width() // 8
    box_height = self.scaled.get_height() // 8
    
    return box_width, box_height 

  def draw_pieces(self, screen):
    if self.selected_square:
      r, c = self.selected_square
      for y in range(8):
        for x in range(8):
          if self.is_valid_move(r, c, y, x):
            screen.blit(self.light, (x * 100, y * 100))
    for x in range(8):
      for y in range(8):
        piece = self.data[y][x]
        if piece != "--":
          image = self.parts[piece]
          screen.blit(image, (x * 100, y * 100))
  
  def is_valid_move(self, start_row, start_col, end_row, end_col):
    piece = self.data[start_row][start_col]
    target = self.data[end_row][end_col]
    piece_type = piece[:-1]
    piece_color = piece[-1]
    
    if target != "--" and target[-1] == piece_color:
      return False
    
    row_diff = end_row - start_row
    col_diff = end_col - start_col
    
    if piece_type == 'Pawn':
      direction = -1 if piece_color == "W" else 1 
      if row_diff == direction and col_diff == 0 and target == '--':
        return True
      if row_diff == direction * 2 and col_diff == 0 and start_row == (6 if piece_color == 'W' else 1) and target == '--' and self.data[start_row + direction][start_col] == '--':
        return True
      if row_diff == direction and abs(col_diff) == 1 and target != '--':
        return True
      return False
    
    if piece_type == "Knight":
      if (abs(row_diff) == 2 and abs(col_diff) == 1) or (abs(row_diff) == 1 and abs(col_diff) == 2):
        return True
      return False 
    
    if piece_type == "King":
      if abs(row_diff) <= 1 and abs(col_diff) <=1:
        return True
      return False
    
    if piece_type == "Rook":
      if row_diff == 0 or col_diff == 0:
        return self.check_path_clear(start_row, start_col, end_row, end_col)
      return False
    
    if piece_type == "Bishop":
      if abs(row_diff) == abs(col_diff):
        return self.check_path_clear(start_row, start_col, end_row, end_col)
      return False
    
    if piece_type == "Queen":
      if row_diff == 0 or col_diff == 0 or abs(row_diff) == abs(col_diff):
        return self.check_path_clear(start_row, start_col, end_row, end_col)
      return False
    
    return False

  def check_path_clear(self, start_row, start_col, end_row, end_col):
    row_step = 0 if start_row == end_row else (1 if end_row > start_row else -1)
    col_step = 0 if start_col == end_col else (1 if end_col > start_col else -1)
    curr_row, curr_col = start_row + row_step, start_col + col_step
    while (curr_row, curr_col) != (end_row, end_col):
      if self.data[curr_row][curr_col] != "--":
        return False
      curr_row += row_step
      curr_col += col_step
    return True
  
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
            
            if self.is_valid_move(start_row, start_col, end_row, end_col):
              self.data[end_row][end_col] = self.data[start_row][start_col]
            
              self.data[start_row][start_col] = '--'
              if self.role == "white":
                
                self.role = "black"
              else:
                self.role = "white"
            
            self.player_clicks.clear()
            self.selected_square = () 
    
        


