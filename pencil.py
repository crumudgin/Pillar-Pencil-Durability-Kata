class Pencil():

	def __init__(self, point_durability, length, eraser):
		self.point_durability = point_durability
		self.max_point_durrability = point_durability
		self.length = length
		self.eraser = eraser

	"""
	Paramaters: char_to_write 			- the char the pencil is being instructed to "write"
				char_in_paper 			- the char currently on the paper
	Description: decrements the pencil's point durability.
				 if the char is lowercase the point durrability is decremented once.
				 if the char is uppercase the point durrability is decremented twice.
				 if the point durrability is zero the point durrability is not decremented.
	Returns: the char that should be written down based on the point durrability
	"""
	def decrement_durability(self, char_to_write, char_in_paper):
		if char_to_write != char_in_paper and char_to_write != "\n":
			self.point_durability -= 1
			if char_to_write.isupper():
				self.point_durability -= 1
			if self.point_durability < 0:
				self.point_durability = 0
				return char_in_paper
		return char_to_write

	"""
	Paramaters: to_write				- the string the pencil is being instructed to "write"
				paper					- the current text on the "paper"
				string_starting_point	- the index where the pencil should begin writing
										  if None, the pencil will append the text to the end of the paper
	Description: writes the provided string to the paper.
				 any conflicts while writing will be recorded by writing "@" instead of any given char.
	Returns: the amended paper
	"""
	def write(self, to_write, paper, string_starting_point=None):
		if string_starting_point is None:
			string_starting_point = len(paper)

		string_ending_point = string_starting_point + len(to_write)
		new_paper_text = [" "] * max(len(paper), string_ending_point)

		for index in range(len(new_paper_text)):
			if index < len(paper):
				new_paper_text[index] = paper[index]
			if index >= string_starting_point and index < string_ending_point:
				to_write_char = to_write[index - string_starting_point]
				if to_write_char != " " and new_paper_text[index] != " ":
					new_paper_text[index] = self.decrement_durability("@", new_paper_text[index])
				elif to_write_char == " ":
					new_paper_text[index] = self.decrement_durability(new_paper_text[index], new_paper_text[index])
				else:
					new_paper_text[index] = self.decrement_durability(to_write_char, new_paper_text[index])

		return "".join(new_paper_text)

	"""
	Description: restores the pencils point durrability to it's initial value and decrements the pencils length
	"""
	def sharpen(self):
		if self.length <= 0:
			return
		self.length -= 1
		self.point_durability = self.max_point_durrability

	"""
	Paramaters: paper			- the current text on the "paper"
				string_to_erase	- the string to find in the paper
	Description: locates the last instance of the string_to_erase in the paper and replaces
				 all the chars with " " so long as the eraser remains above zero
	Returns: the amended paper
	"""
	def erase(self, paper, string_to_erase):
		location_of_string_to_erase = paper.rfind(string_to_erase)
		if location_of_string_to_erase == -1:
			return paper

		erased_string = " " * min(len(string_to_erase), self.eraser)
		stop_erasing = location_of_string_to_erase + len(string_to_erase)
		start_erasing = stop_erasing -  len(erased_string)

		self.eraser -= sum([1 for i in string_to_erase[len(string_to_erase) - len(erased_string):] if i != " "])
		return paper[:start_erasing] + erased_string + paper[stop_erasing:]
			