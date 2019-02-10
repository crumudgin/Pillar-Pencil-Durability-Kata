import pytest
from pencil import Pencil

"""
A series of tests to test that the pencil can write to a string
"""
@pytest.mark.parametrize(("expected_writing_on_page",				"page_before_being_writen_on",	"string_to_write",		"string_starting_point"), 
						[("Hello World!",							"",								"Hello World!",			None),
						("She sells sea shells by the sea shore",	"She sells sea shells",			" by the sea shore",	None),
						("123",										"1 3",							"2",					1),
						("1@3",										"123",							"2",					1),
						("12 3",									"12",							"3",					3),
						("",										"",								"",						None)
						])
def test_write_on_strings(expected_writing_on_page, page_before_being_writen_on, string_to_write, string_starting_point):
	pencil = Pencil(10000, 10, 10)
	paper = pencil.write(string_to_write, page_before_being_writen_on, string_starting_point)
	assert expected_writing_on_page == paper

"""
A series of tests to test the pencil durability and what happens when that durability runs out
"""
@pytest.mark.parametrize(("expected_writing_on_page",	"expected_point_value",	"starting_point_value",	"page_before_being_writen_on",	"string_to_write",	"string_starting_point"), 
						[("test",						0,						4,						"",								"test",				None),
						("Test",						0,						5,						"",								"Test",				None),
						("Tes ",						0,						4,						"",								"Test",				None),
						("This is a Test!",				0,						14,						"",								"This is a Test!",	None),
						("This           ",				0,						5,						"",								"This is a Test!",	None),
						("This is a Test!",				10,						24,						"",								"This is a Test!",	None),
						("This is a Test!",				8,						14,						"This is a ",					"Test!",			10),
						("    ",						0,						0,						"",								"test",				None),
						("    ",						0,						-1,						"",								"test",				None),
						("",							10,						10,						"",								"",					None)
						])
def test_point_degradation(expected_writing_on_page, expected_point_value, starting_point_value, page_before_being_writen_on, string_to_write, string_starting_point):
	pencil = Pencil(starting_point_value, 1, 1)
	paper = pencil.write(string_to_write, page_before_being_writen_on, string_starting_point)
	assert expected_writing_on_page == paper
	assert expected_point_value == pencil.point_durability

"""
A series of tests to test the sharpen functionality of the pencil
"""
@pytest.mark.parametrize(("expected_point_value",	"starting_point_value",	"expected_length",	"starting_length",	"page_before_being_writen_on",	"string_to_write",	"string_starting_point"), 
						[(1,						1,						0,					1,					"",								"",					None),
						(5,							5,						0,					1,					"",								"Test",				None),
						(5,							5,						1,					2,					"",								"Test",				None),
						(0,							5,						0,					0,					"",								"Test",				None),
						(1,							6,						0,					0,					"",								"Test",				None)
						])
def test_sharpen(expected_point_value, starting_point_value, expected_length, starting_length, page_before_being_writen_on, string_to_write, string_starting_point):
	pencil = Pencil(starting_point_value, starting_length, 1)
	pencil.write(string_to_write, page_before_being_writen_on, string_starting_point)
	pencil.sharpen()
	assert pencil.point_durability == expected_point_value
	assert pencil.length == expected_length

"""
A series of tests to test the erase functionality of the pencil
"""
@pytest.mark.parametrize(("expected_writing_on_page",	"page_before_being_erased",	"string_to_erase",	"eraser_size",	"expected_eraser_size"), 
						[("    ",						"test",						"test",				10,				6),
						("test    ",					"testtest",					"test",				10,				6),
						("123 ",						"1232",						"2",				10,				9),
						("test",						"test",						"2",				10,				10),
						("t    est",					"the rest",					"he r",				10,				7),
						("test",						"test",						"test",				0,				0),
						("tes ",						"test",						"test",				1,				0),
						("Buffalo B   ",				"Buffalo Bill",				"Bill",				3,				0)
						])
def test_erase(expected_writing_on_page, page_before_being_erased, string_to_erase, eraser_size, expected_eraser_size):
	pencil = Pencil(10000, 10000, eraser_size)
	paper = pencil.erase(page_before_being_erased, string_to_erase)
	assert expected_writing_on_page == paper
	assert expected_eraser_size == pencil.eraser
