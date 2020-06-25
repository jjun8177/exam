def get_count(input_str):
    pass

# tester provided
def test_sample():
    assert get_count("abracadabra") == 5
    assert get_count("") == 0
    assert get_count("bcd,! ?") == 0
    assert get_count("pear tree") == 4
    assert get_count("o a kak ushakov lil vo kashu kakao") == 13
