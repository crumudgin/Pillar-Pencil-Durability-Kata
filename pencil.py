class Pencil():

	def __init__(self):
		self.how_to_write = None

	def write_to_string(self, to_write, paper):
		paper[0] += to_write

	def write_to_text_file(self, to_write, paper):
		with open(paper, "a") as file:
			file.write(to_write)


	def write(self, to_write, paper):
		self.how_to_write(to_write, paper)