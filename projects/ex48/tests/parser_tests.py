from nose.tools import *
from ex48 import parser, lexicon

def test_peek():
    word_list = lexicon.scan("bear eat cabinet")
    assert_equal('noun', parser.peek(word_list))
    word_list = lexicon.scan("eat north")
    assert_equal('verb', parser.peek(word_list))

def test_match():
    word_list = lexicon.scan("bear eat cabinet")
    assert_equal(('noun', 'bear'), parser.match(word_list, 'noun'))
    assert_equal(('verb', 'eat'), parser.match(word_list, 'verb'))
    assert_equal(('noun', 'cabinet'), parser.match(word_list, 'noun'))
    assert_equal(None, parser.match(word_list, 'noun'))
    assert_equal(None, parser.match(word_list, 'asfdasdf'))
    word_list = lexicon.scan("eat north")
    assert_equal(None, parser.match(word_list, 'safasdfa'))
    assert_equal(('direction', 'north'), parser.match(word_list, 'direction'))

def test_skip():
    word_list = lexicon.scan("the door up in the north")
    parser.skip(word_list, 'noun')
    # should be 'the'
    assert_equal('stop', parser.peek(word_list))
    parser.skip(word_list, 'stop')
    # should be 'door'
    assert_equal('noun', parser.peek(word_list))
    # parser.skip([], None) infinite loop
    parser.skip(word_list, None)
    parser.skip([], {'noun'})

def test_parse_verb():
    word_list = lexicon.scan("the in of stop")
    assert_equal(('verb', 'stop'), parser.parse_verb(word_list))
    word_list = lexicon.scan("the princess in of stop")
    assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object():
    word_list = lexicon.scan("the in of stop")
    assert_raises(parser.ParserError, parser.parse_object, word_list)
    word_list = lexicon.scan("the princess in of stop")
    assert_equal(('noun', 'princess'), parser.parse_object(word_list))
    word_list = lexicon.scan("north of the bear")
    assert_equal(('direction', 'north'), parser.parse_object(word_list))
    assert_raises(parser.ParserError, parser.parse_object, [])

def test_parse_subject():
    word_list = lexicon.scan("go north")
    sen = parser.parse_subject(word_list, ('noun', 'princess'))
    assert_equal(sen.subject, "princess")
    word_list = lexicon.scan("bear north")
    assert_raises(parser.ParserError, parser.parse_subject, word_list, ('noun', 'princess'))
    word_list = lexicon.scan("go go")
    assert_raises(parser.ParserError, parser.parse_subject, word_list, ('noun', 'princess'))

def test_parse_sentence():
    word_list = lexicon.scan("the princess go north")
    assert_equal('princess', parser.parse_sentence(word_list).subject)
    word_list = lexicon.scan("kill bear")
    sen = parser.parse_sentence(word_list)
    assert_equal('player', sen.subject)
    assert_equal('kill', sen.verb)
    assert_equal('bear', sen.object)
    word_list = lexicon.scan("the the the the")
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)
    assert_raises(parser.ParserError, parser.parse_sentence, [])

def test_numbers():
    word_list = lexicon.scan("kill 7 bear")
    sen = parser.parse_sentence(word_list)
    assert_equal(sen.subject, 'player')
    assert_equal(sen.verb, 'kill')
    assert_equal(sen.object, 'bear')
    word_list = lexicon.scan("cabinet kill the 42 bear")
    sen = parser.parse_sentence(word_list)
    assert_equal(sen.subject, 'cabinet')
