class Map:
  instance = None
  initialized = False

  '''
  Singleton Design Structure
  '''
  def __new__(cls):
    if cls.instance is None:
      cls.instance = super().__new__(cls)
    return cls.instance

  '''
  Creates the map and a revealed list representing if the player has seen an area (False in the beginning for all values)
  '''
  def __init__(self):
    initialized = False

  def __getitem__(self, row):
    return self.map[row]

  def __len__(self):
    return len(self.map)

  def load_map(self, map_num):
    if not Map.initialized:
      self.map = []
      self.revealed = []
      maps = ["map1.txt", "map2.txt", "map3.txt"]
      with open(maps[map_num-1]) as f:
        for line in f:
          self.map.append(list(line.strip()))
      for i in range(len(self.map)):
        innerReveal = []
        for j in range(len(self.map[i])):
          innerReveal.append(False)
        self.revealed.append(innerReveal)

  
  '''
  Map is displayed depending on the user's location (*), seen areas (letters), and unseen areas (X))
  '''
  def show_map(self, loc):
    map2 = ""
    for row in range(len(self.map)):
      for col in range(len(self.map[row])):
        if self.revealed[row][col]:
          if row == loc[0] and col == loc[1]:
            map2 += '* '
          else:
            map2 += self.map[row][col] + " "
        else:
          map2 += "X "
      map2 += "\n"
    return map2

  '''
  Switches to True in the revealed list if the area has been seen
  '''
  def reveal(self, loc):
    self.revealed[loc[0]][loc[1]] = True

  def remove_at_loc(self, loc):
    self.map[loc[0]][loc[1]] = "n"