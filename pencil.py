class Pencil():

	def __init__(self, point_durability):
		self.how_to_write = self.write_to_string
		self.point_durability = point_durability

	def calc_char_to_write(self, potential_char_to_write, char_in_paper):
		if potential_char_to_write != char_in_paper:
			self.point_durability -= 1
			if potential_char_to_write.isupper():
				self.point_durability -= 1
			if self.point_durability < 0:
				self.point_durability = 0
				return char_in_paper
		return potential_char_to_write

	def write_from_starting_point(self, to_write, paper_text, string_starting_point):
		if string_starting_point is None:
			string_starting_point = len(paper_text)
		if len(paper_text) < string_starting_point:
			paper_text += " " * (string_starting_point - len(paper_text))
		new_paper_text = paper_text[:string_starting_point]
		paper_index = 0
		for index, char in enumerate(to_write):
			paper_index = string_starting_point + index
			if paper_index < len(paper_text) and char != " " and paper_text[paper_index] != " ":
				new_paper_text += self.calc_char_to_write("@", paper_text[paper_index])
			elif paper_index < len(paper_text):
				new_paper_text += self.calc_char_to_write(max(char, paper_text[paper_index]), paper_text[paper_index])
			else:
				new_paper_text += self.calc_char_to_write(char, " ")

		return new_paper_text + paper_text[paper_index+1:]

	def write_to_string(self, to_write, paper, string_starting_point, params):
		paper[0] = self.write_from_starting_point(to_write, paper[0], string_starting_point)

	def write_to_text_file(self, to_write, paper, string_starting_point, params):
		with open(paper, "r+") as file:
			paper_text = self.write_from_starting_point(to_write, paper.read(), string_starting_point)
			file.write(paper_text)

	def write_to_object_variable(self, to_write, paper, string_starting_point, paper_var):
		place_to_write = getattr(paper, paper_var)
		setattr(paper, paper_var, self.write_from_starting_point(to_write, place_to_write, string_starting_point))

	def write(self, to_write, paper, string_starting_point, params=None):
		self.how_to_write(to_write, paper, string_starting_point, params)