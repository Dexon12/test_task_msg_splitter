from html_parse_solution.splitter import Splitter

test_string = """<div id="root"><strong>Line1</strong><ul class="list unordered some other class" id="some list"><li>This_will_fit</li><li>WATERMARK</li><li>next</li></ul></div>"""
first_part = """<div id="root"><strong>Line1</strong><ul class="list unordered some other class" id="some list"><li>This_will_fit</li></ul></div>"""
second_part = """<div id="root"><ul class="list unordered some other class" id="some list"><li>WATERMARK</li><li>next</li></ul></div>"""

watermark_index = test_string.index("WATERMARK") + len("WATERMARK") + 2

def test_splitter():
    s = Splitter(watermark_index)
    s.feed(test_string)
    s.flush()
    assert s.fragments[0] == first_part
    assert s.fragments[1] == second_part

test_splitter()
