import pytest
from pencil import Pencil

test_labels = "expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point"

test_data = [("Hello World!", 							"",						"Hello World!",			0),
			("She sells sea shells by the sea shore", 	"She sells sea shells",	" by the sea shore",	20),
			("123", 									"1 3", 					"2",					1),
			("1@3",										"123",					"2", 					1),
			("12 3", 									"12", 					"3", 					3)
			]

"""
A pencil fixture to be shared by the rest of the test cases
"""
@pytest.fixture
def pencil():
	return Pencil()

"""
A series of tests to test that the pencil can write to a string
"""
@pytest.mark.parametrize(test_labels, test_data)
def test_write_on_strings(pencil, expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point):
	paper = [page_before_being_writen_on]
	pencil.how_to_write = pencil.write_to_string
	pencil.write(string_to_write, paper, string_starting_point)
	assert expected_writing_on_page == paper[0]

"""
A series of tests to test that the pencil can write to a file
"""
@pytest.mark.parametrize(test_labels, test_data)
def test_write_on_text_files(pencil, tmpdir, expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point):
	pencil.how_to_write = pencil.write_to_text_file
	paper = tmpdir.mkdir("sub").join("paper.txt")
	paper.write(page_before_being_writen_on)
	pencil.write(string_to_write, paper, string_starting_point)
	assert paper.read() == expected_writing_on_page

