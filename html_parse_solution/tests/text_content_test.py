from html_parse_solution.text_content import TextContent

test_string = "A quick brown fox jumps over the lazy dog"
MAX_LEN = 4096

def test_size():
    node = TextContent(test_string)
    assert len(test_string) == node.get_size()

def test_crop_correct():
    node = TextContent(test_string)
    crop_result = node.crop(len(test_string), MAX_LEN)
    assert crop_result[0] == test_string
    assert crop_result[1] == False

def test_crop_small():
    node = TextContent(test_string)
    crop_result = node.crop(4, MAX_LEN)
    assert crop_result[0] == ""
    assert crop_result[1] == True

def test_get_text():
    node = TextContent(test_string)
    assert test_string == node.get_text()
