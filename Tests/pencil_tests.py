import pytest
from pencil import Pencil

@pytest.fixture
def pencil():
	return Pencil()

@pytest.mark.parametrize(	 ("expected_writing_on_page", 				"page_before_being_writen_on", 	"string_to_write"),
							[("Hello World!", 							"",								"Hello World!"),
							 ("She sells sea shells by the sea shore", 	"She sells sea shells",			" by the sea shore")
							])
def test_write_on_strings(pencil, expected_writing_on_page, page_before_being_writen_on, string_to_write):
	paper = [page_before_being_writen_on]
	pencil.write(string_to_write, paper)
	assert expected_writing_on_page == paper[0]
