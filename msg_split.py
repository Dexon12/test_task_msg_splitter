import argparse

from typing import Generator

from html_parse_solution.splitter import Splitter


def split_message(source: str, max_len: int) -> Generator[str, None, None]:
    splitter = Splitter(max_len)
    splitter.feed(source)
    splitter.flush()
    for fragment in splitter.fragments:
        yield fragment

def splitter_measure(html_content, max_len):
    frags = []
    for idx, frag in enumerate(split_message(html_content, max_len=max_len), start=1):
        print(f"Fragment #{idx}: {len(frag)} characters.")
        print(frag)
        frags.append(frag)
    return frags

if __name__ == '__main__':
    MAX_LEN = 4096
    parser = argparse.ArgumentParser(description='Splits HTML message into fragments.')
    parser.add_argument('--max-len', type=int, default=MAX_LEN, help='Maximum length of each fragment (excluding \\n).')
    parser.add_argument('source', type=str, help='Path to the source HTML file.')

    args = parser.parse_args()

    ARGS_MAX_LEN = args.max_len or MAX_LEN
    try:
        with open(args.source, 'r', encoding='utf-8') as f:
            html_content = f.read()
        # splitter_start = time.perf_counter()
        # splitter_frags = splitter_measure(html_content, args.max_len)
        # splitter_end = time.perf_counter()
        # print("splitter time: " + str(splitter_end - splitter_start))
        for number, fragment in enumerate(split_message(html_content, args.max_len), start=1):
            print(f'fragment #{number}: {len(fragment)} chars.')
            print(fragment)
    except Exception as e:
        print(f"Error: {e}")