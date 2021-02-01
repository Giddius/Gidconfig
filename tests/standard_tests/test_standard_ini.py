from gidconfig.standard.classes import ConfigHandler, Get
import pytest


def test_getlist(ini_config):
    cfg = ini_config[0]
    assert cfg.getlist('two', 'list_str_exp') == ["first", "second", "third"]
    assert cfg.getlist('two', 'list_int_exp') == ["1", "2", "3"]
    assert cfg.getlist('two', 'list_bool_exp') == ["yes", "no", "True", "false", "off", "on"]
    assert cfg.getlist('two', 'list_mixed_exp') == ["big", "12", "small", "off", "true", "69"]
    assert cfg.getlist('two', 'multiword_string_list') == ["this is a", "test of a sentence", "that is split inside a list"]
    assert cfg.getlist('three', 'list_bad_format') == ["first", "second", "third", "fourth"]

    assert cfg.getlist('two', 'list_str_exp', as_set=True) == {"first", "second", "third"}

    assert cfg.getlist('one', 'string_exp') == ['testerstr']


def test_set(ini_config):
    cfg = ini_config[0]
    cfg.set('two', 'new_option', 'value_is_string')
    cfg.set('two', 'new_list_option', ['alpha', 'bravo', 'charly'])
    assert cfg.get('two', 'new_option') == 'value_is_string'
    assert cfg.get('two', 'new_list_option') == "alpha, bravo, charly"
    with open(ini_config[1], 'r') as f:
        content = f.read()
    content_lines = content.splitlines()

    assert 'new_option = value_is_string' in content_lines
    assert "new_list_option = alpha, bravo, charly" in content_lines
