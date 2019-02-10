class Pencil():

	def __init__(self, point_durability, length, eraser):
		self.point_durability = point_durability
		self.max_point_durrability = point_durability
		self.length = length
		self.eraser = eraser

	def __calc_char_to_write(self, potential_char_to_write, char_in_paper):
		if potential_char_to_write != char_in_paper:
			self.point_durability -= 1
			if potential_char_to_write.isupper():
				self.point_durability -= 1
			if self.point_durability < 0:
				self.point_durability = 0
				return char_in_paper
		return potential_char_to_write

	def write(self, to_write, paper, string_starting_point):
		if string_starting_point is None:
			string_starting_point = len(paper)
		if len(paper) < string_starting_point:
			paper += " " * (string_starting_point - len(paper))
		new_paper_text = list(paper[:string_starting_point])

		paper_index = 0
		for index, char in enumerate(to_write):
			paper_index = string_starting_point + index
			if paper_index < len(paper) and char != " " and paper[paper_index] != " ":
				new_paper_text.append(self.__calc_char_to_write("@", paper[paper_index]))
			elif paper_index < len(paper):
				new_paper_text.append(self.__calc_char_to_write(max(char, paper[paper_index]), paper[paper_index]))
			else:
				new_paper_text.append(self.__calc_char_to_write(char, " "))

		return "".join(new_paper_text) + paper[paper_index+1:]

	def sharpen(self):
		if self.length <= 0:
			return
		self.length -= 1
		self.point_durability = self.max_point_durrability

	def erase(self, paper, to_erase):
		location_of_to_erase = paper.rfind(to_erase)
		if location_of_to_erase == -1:
			return paper

		if self.eraser >= len(to_erase) and self.eraser > 0:
			self.eraser -= sum([1 for i in to_erase if i != " "])
			return paper[:location_of_to_erase] + (" " * len(to_erase)) + paper[location_of_to_erase + len(to_erase):]
		start_erasing = location_of_to_erase + (len(to_erase) - self.eraser)
		paper = paper[:start_erasing] + (" " * self.eraser) + paper[start_erasing + self.eraser:]
		self.eraser = 0
		return paper
			