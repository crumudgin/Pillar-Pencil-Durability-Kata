import pytest
from pencil import Pencil

writing_test_labels = "expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point"

writing_test_data =	[("Hello World!",							"",						"Hello World!",			None),
					("She sells sea shells by the sea shore",	"She sells sea shells",	" by the sea shore",	None),
					("123",										"1 3",					"2",					1),
					("1@3",										"123",					"2",					1),
					("12 3",									"12",					"3",					3),
					("",										"",						"",						None)
					]

point_degradation_test_labels = "expected_writing_on_page, expected_point_value, starting_point_value, page_before_being_writen_on, string_to_write, string_starting_point"

point_degradation_test_data = 	[("test",			0,	4,	"",				"test",				None),
								("Test",			0,	5,	"",				"Test",				None),
								("Tes ",			0,	4,	"",				"Test",				None),
								("This is a Test!",	0,	14,	"",				"This is a Test!",	None),
								("This           ",	0,	5,	"",				"This is a Test!",	None),
								("This is a Test!",	10,	24,	"",				"This is a Test!",	None),
								("This is a Test!",	8,	14,	"This is a ",	"Test!",			10),
								("    ",			0,	0,	"",				"test",				None),
								("    ",			0,	-1,	"",				"test",				None),
								("",				10,	10,	"",				"",					None)
								]

sharpen_test_labels = "expected_writing_on_page, expected_point_value, starting_point_value, expected_length, starting_length, page_before_being_writen_on, string_to_write, string_starting_point"

sharpen_test_data = 	[("",		1,	1,	0,	1,	"",	"",		None),
						("Test",	5,	5,	0,	1,	"",	"Test",	None),
						("Test",	5,	5,	1,	2,	"",	"Test",	None),
						("Test",	0,	5,	0,	0,	"",	"Test",	None),
						("Test",	1,	6,	0,	0,	"",	"Test",	None)
						]

erase_test_labels = "expected_writing_on_page, page_before_being_erased, string_to_erase"

erase_test_data = 	[("", "test", "test"),
					("test", "testtest", "test"),
					("123", "1232", "2"),
					("test", "test", "2"),
					("test", "the rest", "he rest")
					]

"""
A pencil fixture to be shared by the rest of the test cases
"""
@pytest.fixture
def pencil():
	return Pencil(10000, 100)

"""
A series of tests to test that the pencil can write to a string
"""
@pytest.mark.parametrize(writing_test_labels, writing_test_data)
def test_write_on_strings(pencil, expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point):
	paper = [page_before_being_writen_on]
	pencil.write(string_to_write, paper, string_starting_point)
	assert expected_writing_on_page == paper[0]

"""
A series of tests to test that the pencil can write to a file
"""
@pytest.mark.parametrize(writing_test_labels, writing_test_data)
def test_write_on_text_files(pencil, tmpdir, expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point):
	pencil.how_to_write = pencil.write_to_text_file
	paper = tmpdir.mkdir("sub").join("paper.txt")
	paper.write(page_before_being_writen_on)
	pencil.write(string_to_write, paper, string_starting_point)
	assert paper.read() == expected_writing_on_page

"""
A series of tests to test that the pencil can write on any object
given to it so long as the pencil is told where to and how to write
to the object
"""
@pytest.mark.parametrize(writing_test_labels, writing_test_data)
def test_write_on_paper_object(pencil, expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point):
	class Paper():
		def __init__(self, text):
			self.text = text

	paper = Paper(page_before_being_writen_on)
	pencil.how_to_write = pencil.write_to_object_variable
	pencil.write(string_to_write, paper, string_starting_point, "text")
	assert paper.text == expected_writing_on_page

"""
A series of tests to test the pencil durability and what happens when that durability runs out
"""
@pytest.mark.parametrize(point_degradation_test_labels, point_degradation_test_data)
def test_point_degradation(expected_writing_on_page, expected_point_value, starting_point_value, page_before_being_writen_on, string_to_write, string_starting_point):
	pencil = Pencil(starting_point_value, 1)
	paper = [page_before_being_writen_on]
	pencil.write(string_to_write, paper, string_starting_point)
	assert expected_writing_on_page == paper[0]
	assert expected_point_value == pencil.point_durability

"""
A series of tests to test the sharpen functionality of the pencil
"""
@pytest.mark.parametrize(sharpen_test_labels, sharpen_test_data)
def test_sharpen(expected_writing_on_page, expected_point_value, starting_point_value, expected_length, starting_length, page_before_being_writen_on, string_to_write, string_starting_point):
	pencil = Pencil(starting_point_value, starting_length)
	paper = [page_before_being_writen_on]
	pencil.write(string_to_write, paper, string_starting_point)
	pencil.sharpen()
	assert pencil.point_durability == expected_point_value
	assert pencil.length == expected_length

@pytest.mark.parametrize(erase_test_labels, erase_test_data)
def test_erase(pencil, expected_writing_on_page, page_before_being_erased, string_to_erase):
	paper = [page_before_being_erased]
	pencil.erase(paper, string_to_erase)
	assert paper[0] == expected_writing_on_page