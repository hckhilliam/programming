# Too much code screw it.
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
      pn = None
      n = (0, 0)
      while True:
        # Out of bounds.
        if (n[0] < 0 or n[0] >= len(grid) or n[1] < 0 or n[1] >= len(grid[0])):
          return False

        pgv = grid[pn[0]][pn[1]] if pn else None
        gv = grid[n[0]][n[1]]
        if gv == 1:
          if pn and (
            (pn != (n[0], n[1] - 1) and pn != (n[0], n[1] + 1))  # Previous location check.
            or pgv not in [None, 1, 4, 6] # Correct road check.
          ):
            return False
          nn = (n[0], n[1] + 1)
        elif gv == 2:
          if pn and (pn != (n[0] - 1, n[1]) or pgv not in [None, 2, 3, 4]):
            return False
          nn = (n[0] + 1, n[1])
        elif gv == 3:
          if pn and (pn != (n[0], n[1] - 1) or pgv not in [None, 1, 4, 6]):
            return False
          nn = (n[0], n[1])
        elif gv == 4:
          if pn and (pn != (n[0], n[1] + 1) or pgv not in [None, 1, 3, 5]):
            return False
          nn = (n[0], n[1])
        elif gv == 5:
          if pn and (pn != (n[0] - 1, n[1]) or pgv not in [None, 2, 3, 4]):
            return False
          nn = (n[0], n[1])
        else:
          if pn and (pn != (n[0] - 1, n[1]) or pgv not in [None, 2, 3, 4]):
            return False
          nn = (n[0], n[1])
        pn = n
        n = nn