import pytest
from gidconfig.standard.classes import ConfigHandler, Get, SingleAccessConfigHandler

import os

SAMPLE_INI_CONTENT = """[DEFAULT]
default_string = this is a default test
is_empty_value = not in default

[one]
string_exp = testerstr
int_exp = 6
# one small comment
bool_exp = yes
float_exp = 6.31
multiword_string = this is a test of a sentence
multiword_comma_string = this is a test of a sentence with an, comma in it

[two]
list_str_exp = first, second, third
list_int_exp = 1, 2, 3
list_bool_exp = yes, no, True, false, off, on
list_mixed_exp = big, 12, small, off, true, 69
multiword_string_list = this is a, test of a sentence, that is split inside a list

[three]
list_bad_format = first,second, third,     fourth
special_bool = True

[four]
empty_not_backed_by_default =
is_empty_value =

"""
SAMPLE_COMMENTED_INI_CONTENT = """
# top_comment, that should be removed

[DEFAULT]
# This is a default comment
default_string = this is a default test

# this is a comment for section 'one'
[one]

# commenting 'string_exp'
string_exp = testerstr
# commenting 'int_exp'
int_exp = 6

# commenting 'bool_exp'
# with two comments
bool_exp = yes

float_exp = 6.31
multiword_string = this is a test of a sentence

multiword_comma_string = this is a test of a sentence with an, comma in it


# this is a comment for section 'two'
[two]

# commenting 'list_str_exp'
list_str_exp = first, second, third

# commenting 'list_int_exp'
list_int_exp = 1, 2, 3

# commenting 'list_bool_exp'
list_bool_exp = yes, no, True, false, off, on

# commenting 'list_mixed_exp'
list_mixed_exp = big, 12, small, off, true, 69

# commenting 'multiword_string_list'
multiword_string_list = this is a, test of a sentence, that is split inside a list

# this is a comment for section 'three'
# with another comment underneath
[three]
list_bad_format = first,second, third,     fourth

"""


@pytest.fixture
def sample_ini_file(tmpdir):
    _path = tmpdir.join('sample_config.ini')
    with open(_path, 'w') as samp_conf_file:
        samp_conf_file.write(SAMPLE_INI_CONTENT)
    yield _path


@pytest.fixture
def comment_sample_ini_file(tmpdir):
    _path = tmpdir.join('sample_config.ini')
    with open(_path, 'w') as samp_conf_file:
        samp_conf_file.write(SAMPLE_COMMENTED_INI_CONTENT)
    yield _path


@pytest.fixture
def ini_config(sample_ini_file):
    _out_cfg = ConfigHandler.from_defaults(sample_ini_file)
    yield _out_cfg, sample_ini_file


@pytest.fixture
def basic_single_access_config(sample_ini_file):
    _out_cfg = SingleAccessConfigHandler.from_defaults(sample_ini_file)
    yield _out_cfg, sample_ini_file


@pytest.fixture
def comment_single_access_config(comment_sample_ini_file):
    _out_cfg = SingleAccessConfigHandler.from_defaults(comment_sample_ini_file)
    yield _out_cfg, comment_sample_ini_file
