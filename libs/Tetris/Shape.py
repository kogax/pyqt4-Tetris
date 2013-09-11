class Shape(object):
	coordsTable = (
		((0, 0),    (0, 0),    (0, 0),    (0, 0)),  # NoShape
		((0, -1),   (0, 0),    (1, 0),    (1, 1)),  # ZShape
		((0, -1),   (0, 0),    (-1, 0),   (-1, 1)), # SShape
		((0, -1),   (0, 0),    (0, 1),    (0, 2)),  # LineShape
		((-1, 0),   (0, 0),    (1, 0),    (0, 1)),  # TShape
		((0, 0),    (0, 1),    (1, 1),    (1, 0)),  # SquareShape
		((1, -1),   (0, -1),   (0, 0),    (0, 1)),  # LShape
		((-1, -1),  (0, -1),   (0, 0),    (0, 1)),  # MirroredLShape
	)

	def __init__(self):
		self.coords = [ [0, 0] for i in range(4) ]
		self.pieceShape = Tetrominoes.NoShape
