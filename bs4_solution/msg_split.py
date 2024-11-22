import argparse
import time

from bs4 import BeautifulSoup, Tag, NavigableString
from typing import Generator, List


MAX_LEN = 4096

BLOCK_TAGS = {
    'p', 'b', 'strong', 'i', 'ul', 'ol', 'div', 'span',
    'header', 'nav', 'main', 'section', 'footer',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'html', 'main', 'body'
}

NOT_CLOSING_TAGS = {
    'img', 'br', 'input', 'meta', 'link', 'hr', 'area', 'base', 
    'col', 'embed', 'source', 'track', 'wbr', 'param'
}

NOT_PROCCESIBLE_TAGS = {'script', 'style'}

ARGS_MAX_LEN = MAX_LEN


def clone_tag(soup: BeautifulSoup, source: Tag):
    if (isinstance(source, NavigableString)):
        return NavigableString(source.get_text())
    
    clone = soup.new_tag(source.name)
    for attr in source.attrs:
        clone[attr] = source[attr]
    return clone


def try_split_tag(soup: BeautifulSoup, source: Tag, remaining_length: int, max_length: int):
    tag_length = len(str(source))
    if source.name not in BLOCK_TAGS:
        if tag_length > max_length:
            raise Exception(f"This tag - {source.name} is bigger than max length")
        else:
            return source, True
    
    copy = clone_tag(soup, source)
    empty_tag_length = len(str(copy))
    if empty_tag_length > remaining_length:
        # leave no tag, this can't be splitted
        return source, True
    
    remaining_length -= empty_tag_length
    tags = list(source.children)
    source.clear()
    index = 0
    while True:
        child_tag = tags[index]
        child_tag_length = len(str(child_tag))
        if child_tag_length <= remaining_length:
            index = index + 1
            remaining_length -= child_tag_length
        else:
            second_part, skip = try_split_tag(soup, child_tag, remaining_length, max_length - empty_tag_length)
            separation_index = index if skip else index+1
            for i in range(0, separation_index):
                source.append(tags[i])
            if not skip:
                copy.append(second_part)
            for i in range(separation_index, len(tags)):
                copy.append(tags[i])
            return copy, False


def bs4_split(source: str, max_len: int) -> Generator[str, None, None]:
    remaining_length = max_len
    soup = BeautifulSoup(source, "html.parser")
    tags = list(soup.children)
    current_fragment = []

    while len(tags) > 0:
        tag = tags[0]
        tag_length = len(str(tag))
        if tag_length <= remaining_length:
            current_fragment.append(str(tag))
            tags.pop(0)
            remaining_length -= tag_length
        else:
            nextTag, skip = try_split_tag(soup, tag, remaining_length, max_len)
            if not skip:
                current_fragment.append(str(tag))
                tags.pop(0)
                tags.insert(0, nextTag)
            yield "".join(current_fragment)
            current_fragment = []
            remaining_length = max_len    
    yield "".join(current_fragment)


def bs4_measure(html_content, max_len):
    frags = []
    for idx, frag in enumerate(bs4_split(html_content, max_len), start=1):
        print(f"Fragment #{idx}: {len(frag)} characters.")
        print(frag)
        frags.append(frag)
    return frags
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Splits HTML message into fragments.')
    parser.add_argument('--max-len', type=int, default=MAX_LEN, help='Maximum length of each fragment (excluding \\n).')
    parser.add_argument('source', type=str, help='Path to the source HTML file.')

    args = parser.parse_args()

    ARGS_MAX_LEN = args.max_len or MAX_LEN
    try:
        with open(args.source, 'r', encoding='utf-8') as f:
            html_content = f.read()

        bs4_start = time.perf_counter()
        bs4_frags = bs4_measure(html_content, args.max_len)
        bs4_end = time.perf_counter()
        print("BS4 time: " + str(bs4_end - bs4_start))
    except Exception as e:
        print(f"Error: {e}")