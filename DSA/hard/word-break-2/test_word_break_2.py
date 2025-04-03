import pytest
from word_break_2 import WordBreak2

@pytest.mark.parametrize(
    "s, wordDict, expected",
    [
        ("catsanddog", ["cat","cats","and","sand","dog"], ["cats and dog","cat sand dog"]),
        ("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"], ["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
        ("catsandog", ["cats","dog","sand","and","cat"], []),
        ("", ["cat", "dog"], [""]),
        ("cat", ["cat"], ["cat"]),
        ("aaaa", ["a", "aa", "aaa", "aaaa"], ["a a a a", "a a aa", "a aa a", "aa a a", "aa aa", "aaa a", "a aaa", "aaaa"]),
        ("aaaaaaaa", ["aaaa","aaa","aa"], ["aaaa aaaa", "aaa aaaaa", "aa aaaaaa", "aaaaaa aa"])
    ]
)
def test_pascal_triangle(s, wordDict, expected):
    actual = WordBreak2().wordBreak(s, wordDict)
    assert sorted(actual) == sorted(expected)