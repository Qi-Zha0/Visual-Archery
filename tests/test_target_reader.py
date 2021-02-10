import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../code"))
from target_reader import target_reader
import pytest

test_img = os.path.realpath(os.path.dirname(__file__)+'/test_image.jpeg')

def test_target_reader():
	tr = target_reader()
	test_result = tr.run(test_img)
	assert test_result == None
	assert len(tr.stage_images) == 4


def test_read_image():
	tr = target_reader()
	assert tr.read_image(test_img) == None


def test_remove_skew():
	tr = target_reader()
	tr.read_image(test_img)
	skew_removed = tr.remove_skew()
	assert skew_removed == None
	assert len(tr.stage_images) == 1

def test_standardize_size():
	tr = target_reader()
	tr.read_image(test_img)
	tr.remove_skew()
	assert tr.standardize_size() == None
	assert len(tr.stage_images) == 2

def test_balance_contrast():
	tr = target_reader()
	tr.read_image(test_img)
	tr.remove_skew()
	tr.standardize_size()
	assert tr.balance_contrast() == None
	assert len(tr.stage_images) == 3

def test_find_shots():
	tr = target_reader()
	tr.read_image(test_img)
	tr.remove_skew()
	tr.standardize_size()
	tr.balance_contrast()
	assert tr.find_shots() == None
	assert len(tr.stage_images) == 4