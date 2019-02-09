class Pencil():

	def __init__(self):
		self.how_to_write = None

	def write_from_starting_point(self, to_write, paper_text, string_starting_point):
		new_paper_text = paper_text[:min(len(paper_text), string_starting_point)]
		if len(paper_text) < string_starting_point:
			new_paper_text += " " * (string_starting_point - len(paper_text))
		for index, char in enumerate(to_write):
			paper_index = string_starting_point + index
			if paper_index < len(paper_text) and char != " " and paper_text[paper_index] != " ":
				new_paper_text += "@"
			elif paper_index < len(paper_text):
				new_paper_text += max(char, paper_text[paper_index])
			else:
				new_paper_text += char
		new_paper_text += paper_text[paper_index+1:]
		return new_paper_text

	def write_to_string(self, to_write, paper, string_starting_point):
		paper[0] = self.write_from_starting_point(to_write, paper[0], string_starting_point)

	def write_to_text_file(self, to_write, paper, string_starting_point):
		with open(paper, "r+") as file:
			paper_text = self.write_from_starting_point(to_write, paper.read(), string_starting_point)
			file.write(paper_text)

	def write(self, to_write, paper, string_starting_point):
		self.how_to_write(to_write, paper, string_starting_point)