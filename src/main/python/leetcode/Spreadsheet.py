class Spreadsheet:

  def __init__(self, rows: int):
    self.data = defaultdict(int)

  def setCell(self, cell: str, value: int) -> None:
    self.data[cell] = value

  def resetCell(self, cell: str) -> None:
    self.data[cell] = 0

  def getValue(self, p: str) -> int:
    v1, v2 = p[1:].split('+')
    if v1.isdigit() and v2.isdigit():
      return int(v1) + int(v2)
    
    if v1.isdigit():
      return int(v1) + self.data[v2]
    
    if v2.isdigit():
      return int(v2) + self.data[v1]

    return self.data[v1] + self.data[v2]
