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

"""
A pencil fixture to be shared by the rest of the test cases
"""
@pytest.fixture
def durable_pencil():
	return Pencil(10000)

"""
A series of tests to test that the pencil can write to a string
"""
@pytest.mark.parametrize(writing_test_labels, writing_test_data)
def test_write_on_strings(durable_pencil, expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point):
	paper = [page_before_being_writen_on]
	durable_pencil.write(string_to_write, paper, string_starting_point)
	assert expected_writing_on_page == paper[0]

"""
A series of tests to test that the pencil can write to a file
"""
@pytest.mark.parametrize(writing_test_labels, writing_test_data)
def test_write_on_text_files(durable_pencil, tmpdir, expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point):
	durable_pencil.how_to_write = durable_pencil.write_to_text_file
	paper = tmpdir.mkdir("sub").join("paper.txt")
	paper.write(page_before_being_writen_on)
	durable_pencil.write(string_to_write, paper, string_starting_point)
	assert paper.read() == expected_writing_on_page

"""
A series of tests to test the pencil durrability and what happens when that durrability runs out
"""
@pytest.mark.parametrize(point_degradation_test_labels, point_degradation_test_data)
def test_point_degradation(expected_writing_on_page, expected_point_value, starting_point_value, page_before_being_writen_on, string_to_write, string_starting_point):
	pencil = Pencil(starting_point_value)
	paper = [page_before_being_writen_on]
	pencil.write(string_to_write, paper, string_starting_point)
	assert expected_writing_on_page == paper[0]
	assert expected_point_value == pencil.point_durability
