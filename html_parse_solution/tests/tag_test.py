from html_parse_solution.text_content import TextContent
from html_parse_solution.tag import Tag

test_string = "A quick brown fox jumps over the lazy dog"
MAX_LEN = 4096

def test_without_data():
    t = Tag("strong", [])
    res_text = "<strong></strong>"
    assert t.get_size() == len(res_text)
    assert t.get_text() == res_text

def test_with_data():
    t = Tag("strong", [])
    t.add_child(TextContent(test_string))
    res_text = f"<strong>{test_string}</strong>"
    assert t.get_size() == len(res_text)
    assert t.get_text() == res_text

def test_no_cropping():
    t = Tag("strong", [])
    t.add_child(TextContent(test_string))
    res_text = f"<strong>{test_string}</strong>"
    crop_result = t.crop(len(res_text) + 5, MAX_LEN)
    assert crop_result[0] == res_text
    assert crop_result[1] == False

def test_cropping_rejected():
    t = Tag("strong", [])
    t.add_child(TextContent(test_string))
    res_text = f"<strong>{test_string}</strong>"
    crop_result = t.crop(len(res_text) - 5, MAX_LEN)
    assert crop_result[0] == "<strong></strong>"
    assert crop_result[1] == True

def test_cropping_partial():
    # split first nesting level
    correct_crop_1 = [
        '<div id="main"><div id="first">Div1 content</div></div>',
        '<div id="main"><div id="second"><span>Span1 content</span><span>Span2 content</span></div></div>'
    ]
    # split second nesting level
    correct_crop_2 = [
        '<div id="main"><div id="first">Div1 content</div><div id="second"><span>Span1 content</span></div></div>',
        '<div id="main"><div id="second"><span>Span2 content</span></div></div>'
    ]

    def generate_test_tag():
        root = Tag("div", [("id", "main")])
        first = Tag("div", [("id", "first")])
        first.add_child(TextContent("Div1 content"))
        root.add_child(first)
        second = Tag("div", [("id", "second")])
        span1 = Tag("span", [])
        span1.add_child(TextContent("Span1 content"))
        second.add_child(span1)
        span2 = Tag("span", [])
        span2.add_child(TextContent("Span2 content"))
        second.add_child(span2)
        root.add_child(second)
        return root

    first_test = generate_test_tag()
    crop_result = first_test.crop(len(correct_crop_1[0]), MAX_LEN)
    assert crop_result[0] == correct_crop_1[0]
    assert crop_result[1] == True
    assert first_test.get_text() == correct_crop_1[1]

    second_test = generate_test_tag()
    crop_result = second_test.crop(len(correct_crop_2[0]), MAX_LEN)
    assert crop_result[0] == correct_crop_2[0]
    assert crop_result[1] == True
    assert second_test.get_text() == correct_crop_2[1]
