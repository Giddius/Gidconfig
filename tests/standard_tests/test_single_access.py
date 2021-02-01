from gidconfig.standard.classes import SingleAccessConfigHandler, List, Set, Tuple
import pytest
from pprint import pprint


def test_basic_retrieve(basic_single_access_config: SingleAccessConfigHandler):
    cfg = basic_single_access_config[0]
    assert set(cfg.sections()) == {'one', 'two', 'three'}
    assert set(cfg.options('one')) == {'multiword_comma_string', 'multiword_string', 'bool_exp', 'int_exp', 'string_exp', 'float_exp'}
    assert set(cfg.options('two')) == {"list_str_exp", "list_int_exp", "list_bool_exp", "list_mixed_exp", "multiword_string_list"}
    assert set(cfg.options('three')) == {'list_bad_format'}

    assert cfg.retrieve('one', 'string_exp', typus=str) == 'testerstr'
    assert cfg.retrieve('one', 'int_exp', typus=int) == 6
    assert cfg.retrieve('one', 'bool_exp', typus=bool) is True
    assert cfg.retrieve('one', 'float_exp', typus=float) == 6.31
    assert cfg.retrieve('one', 'multiword_string', typus=str) == 'this is a test of a sentence'

    assert cfg.retrieve('one', 'multiword_comma_string', typus=str) == 'this is a test of a sentence with an, comma in it'
    assert cfg.retrieve('one', 'multiword_comma_string', typus=List) == ['this is a test of a sentence with an', 'comma in it']
    assert cfg.retrieve('one', 'multiword_comma_string', typus=Set) == {'this is a test of a sentence with an', 'comma in it'}
    assert cfg.retrieve('one', 'multiword_comma_string', typus=Tuple) == ('this is a test of a sentence with an', 'comma in it')

    assert cfg.retrieve('one', 'multiword_comma_string', typus=list) == ['this is a test of a sentence with an', 'comma in it']
    assert cfg.retrieve('one', 'multiword_comma_string', typus=set) == {'this is a test of a sentence with an', 'comma in it'}
    assert cfg.retrieve('one', 'multiword_comma_string', typus=tuple) == ('this is a test of a sentence with an', 'comma in it')

    assert cfg.retrieve('one', 'multiword_comma_string', typus=List[str]) == ['this is a test of a sentence with an', 'comma in it']
    assert cfg.retrieve('one', 'multiword_comma_string', typus=Set[str]) == {'this is a test of a sentence with an', 'comma in it'}
    assert cfg.retrieve('one', 'multiword_comma_string', typus=Tuple[str]) == ('this is a test of a sentence with an', 'comma in it')

    assert cfg.retrieve('two', 'list_int_exp', typus=List[int]) == [1, 2, 3]
    assert cfg.retrieve('two', 'list_int_exp', typus=Set[int]) == {1, 2, 3}
    assert cfg.retrieve('two', 'list_int_exp', typus=Tuple[int]) == (1, 2, 3)
    assert cfg.retrieve('two', 'list_int_exp', typus=List[int], mod_func=lambda x: x * x) == [1, 4, 9]

    assert cfg.retrieve('two', 'list_bool_exp', typus=List[bool]) == [True, False, True, False, False, True]
    assert cfg.retrieve('two', 'list_bool_exp', typus=Set[bool]) == {True, False, True, False, False, True}
    assert cfg.retrieve('two', 'list_bool_exp', typus=Tuple[bool]) == (True, False, True, False, False, True)

    assert cfg.retrieve('three', 'list_bad_format', typus=str) == 'first,second, third,     fourth'
    assert cfg.retrieve('three', 'list_bad_format', typus=List) == ["first", "second", "third", "fourth"]


def test_basic_modification(basic_single_access_config: SingleAccessConfigHandler):
    cfg = basic_single_access_config[0]
    assert cfg.retrieve('one', 'multiword_comma_string', typus=str, mod_func=lambda x: x.upper()) == 'THIS IS A TEST OF A SENTENCE WITH AN, COMMA IN IT'
    assert cfg.retrieve('one', 'multiword_comma_string', typus=List, mod_func=lambda x: x.replace(' ', '')) == ['thisisatestofasentencewithan', 'commainit']
    assert cfg.retrieve('one', 'int_exp', typus=int, mod_func=lambda x: x * 2) == 12


def test_basic_fallbacks(basic_single_access_config: SingleAccessConfigHandler):
    cfg = basic_single_access_config[0]
    assert cfg.retrieve('one', 'does_not_exist', typus=str, direct_fallback='direct fallback worked') == 'direct fallback worked'
    assert cfg.retrieve('one', 'does_not_exist', typus=str, direct_fallback='direct fallback worked', mod_func=lambda x: x.upper()) == 'direct fallback worked'

    assert cfg.retrieve('one', 'does_not_exist', typus=str, fallback_option="string_exp") == 'testerstr'
    assert cfg.retrieve('one', 'does_not_exist', typus=str, fallback_option="string_exp", mod_func=lambda x: x.upper()) == 'TESTERSTR'

    assert cfg.retrieve('one', 'does_not_exist', typus=list, fallback_option='multiword_comma_string') == ['this is a test of a sentence with an', 'comma in it']
    assert cfg.retrieve('one', 'does_not_exist', typus=list, fallback_option='multiword_comma_string', mod_func=lambda x: x.upper()) == ['THIS IS A TEST OF A SENTENCE WITH AN', 'COMMA IN IT']

    assert cfg.retrieve('one', 'does_not_exist', typus=list, fallback_section='two', fallback_option='list_str_exp') == ["first", "second", "third"]
    assert cfg.retrieve('one', 'does_not_exist', typus=list, fallback_section='two', fallback_option='list_str_exp', mod_func=lambda x: x.upper()) == ["FIRST", "SECOND", "THIRD"]


def test_top_comment_and_headers(basic_single_access_config: SingleAccessConfigHandler):
    cfg = basic_single_access_config[0]
    cfg.top_comment = 'this is the top_comment\nwith a second line'
    cfg.save()
    with open(basic_single_access_config[1], 'r') as f:
        content = f.read()

    content_lines = content.splitlines()
    assert content_lines[7] == '# this is the top_comment'
    assert content_lines[3] == "# ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌ INSTRUCTIONS ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌"
    cfg.save()
    cfg.read()
    with open(basic_single_access_config[1], 'r') as f:
        content = f.read()

    content_lines = content.splitlines()
    assert content_lines[7] == '# this is the top_comment'
    assert content_lines[3] == "# ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌ INSTRUCTIONS ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌"


def test_commented_ini(comment_single_access_config: SingleAccessConfigHandler):
    cfg = comment_single_access_config[0]
    assert set(cfg.sections()) == {'one', 'two', 'three'}
    assert set(cfg.options('one')) == {'multiword_comma_string', 'multiword_string', 'bool_exp', 'int_exp', 'string_exp', 'float_exp'}
    assert set(cfg.options('two')) == {"list_str_exp", "list_int_exp", "list_bool_exp", "list_mixed_exp", "multiword_string_list"}
    assert set(cfg.options('three')) == {'list_bad_format'}
    assert cfg.section_comments == {'one': ["# this is a comment for section 'one'"], 'two': ["# this is a comment for section 'two'"], 'three': ["# this is a comment for section 'three'", "# with another comment underneath"]}
    cfg.save()
    cfg.read()
    with open(comment_single_access_config[1], 'r') as f:
        content = f.read()

    content_lines = content.splitlines()

    assert content_lines[6] == "# this is a comment for section 'one'"


def test_append(basic_single_access_config: SingleAccessConfigHandler):
    cfg = basic_single_access_config[0]
    cfg.append('one', 'string_exp', 'appended_value')
    assert cfg.retrieve('one', 'string_exp', typus=str) == "testerstr, appended_value"

    cfg.append('one', 'multiword_comma_string', ['first_add', 'second_add', 'third_add'])
    assert cfg.retrieve('one', 'multiword_comma_string', typus=str) == "this is a test of a sentence with an, comma in it, first_add, second_add, third_add"
    assert cfg.retrieve('one', 'multiword_comma_string', typus=list) == ["this is a test of a sentence with an", "comma in it", "first_add", "second_add", "third_add"]
