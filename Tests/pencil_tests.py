import pytest
from pencil import Pencil

"""
A pencil fixture to be shared by the rest of the test cases
"""
@pytest.fixture
def pencil():
	return Pencil()

"""
A series of tests to test that the pencil can write to a string
"""
@pytest.mark.parametrize(	 ("expected_writing_on_page", 				"page_before_being_writen_on", 	"string_to_write"),
							[("Hello World!", 							"",								"Hello World!"),
							 ("She sells sea shells by the sea shore", 	"She sells sea shells",			" by the sea shore")
							])
def test_write_on_strings(pencil, expected_writing_on_page, page_before_being_writen_on, string_to_write):
	paper = [page_before_being_writen_on]
	pencil.how_to_write = pencil.write_to_string
	pencil.write(string_to_write, paper)
	assert expected_writing_on_page == paper[0]

"""
A series of tests to test that the pencil can write to a file
"""
@pytest.mark.parametrize(	 ("expected_writing_on_page", 				"page_before_being_writen_on", 	"string_to_write"),
							[("Hello World!", 							"",								"Hello World!"),
							 ("She sells sea shells by the sea shore", 	"She sells sea shells",			" by the sea shore")
							])
def test_write_on_text_files(pencil, tmpdir, expected_writing_on_page, page_before_being_writen_on, string_to_write):
	pencil.how_to_write = pencil.write_to_text_file
	paper = tmpdir.mkdir("sub").join("paper.txt")
	paper.write(page_before_being_writen_on)
	pencil.write(string_to_write, paper)
	assert paper.read() == expected_writing_on_page

"""
A series of tests to test that the pencil can write on any object so long as pencil.write_to_paper is defined prior to the writing
"""
@pytest.mark.parametrize(	 ("expected_writing_on_page", 				"page_before_being_writen_on", 	"string_to_write"),
							[("Hello World!", 							"",								"Hello World!"),
							 ("She sells sea shells by the sea shore", 	"She sells sea shells",			" by the sea shore")
							])
def test_write_on_object(pencil, expected_writing_on_page, page_before_being_writen_on, string_to_write):
	class Paper():

		def __init__(self, space_on_paper):
			self.space_on_paper = space_on_paper

	def write_to_paper(to_write, paper):
		paper.space_on_paper += to_write

	paper = Paper(page_before_being_writen_on)
	pencil.how_to_write = write_to_paper
	pencil.write(string_to_write, paper)

	assert paper.space_on_paper == expected_writing_on_page