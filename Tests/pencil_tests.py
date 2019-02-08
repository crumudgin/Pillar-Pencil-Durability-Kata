import unittest
from pencil import Pencil

class PencilTests(unittest.TestCase):

	# Tests for Write Section of problem statment
	def setUp(self):
		self.pencil = Pencil()

	def tearDown(self):
		pass

	def when_write_on_string(self):
		test_string = "Hello World!"
		paper = [""]
		self.pencil.write(test_string, paper)
		self.assertEqual(paper[0], test_string)

	def when_write_with_existing_text(self):
		test_string = "she sells sea shells by the sea shore"
		paper = [test_string[:19]]
		self.pencil.write(test_string[19:], paper)
		self.assertEqual(paper[0], test_string)



if __name__ == '__main__':
    unittest.main()