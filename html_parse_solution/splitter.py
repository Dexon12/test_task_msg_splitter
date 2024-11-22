from html.parser import HTMLParser
from html_parse_solution.text_content import TextContent
from html_parse_solution.tag import Tag

class Splitter(HTMLParser):
    def __init__(self, max_length):
        super().__init__()
        self.max_length = max_length
        self.chunks = []
        self.chunk = None
        # Here are stored the processed fragments (plain text, closed top-level tags)
        self.fragments = []

    def handle_starttag(self, tag, attrs):
        tag = Tag(tag, attrs)
        # If there is no open tag
        if self.chunk is None:
            # That's tag will top-level tag
            self.chunk = tag
            # self.chunks.append(self.chunk)
        else:   
            # Otherwise, add a new tag to the current open tag and mark it as the most recently found.
            # This ensures that nesting is preserved.
            self.chunk = self.chunk.add_child(tag)
        # self.check_size()

    def handle_data(self, data):
        node = TextContent(data)
        # If there is no open tag
        if self.chunk is None:
            self.chunks.append(node)
        else:
            # This tag is part of that open tag
            self.chunk.add_child(node)
        # self.check_size()

    def handle_endtag(self, tag):
        if self.chunk is None or self.chunk.tag != tag:
            # If we have  
            # If a closing tag arrives to us immediately, then this don't good HTML
            raise Exception("Corrupted HTML")
        else:
            # Otherwise, we consider the very last tag closed, and now the last open tag is its parent
            if self.chunk.parent == None:
                self.chunks.append(self.chunk)
            self.chunk = self.chunk.parent
            # self.check_size()

    def process(self):
        size = 0
        index = 0
        while index < len(self.chunks) and size < self.max_length:
            tag = self.chunks[index]
            size += tag.get_size()
            index = index + 1

        if size >= self.max_length:
            # In result, we will collect the message itself
            result = ""
            # index - index in array
            index = 0
            # remaining_size - how much size we have
            remaining_size = self.max_length
            while remaining_size > 0 and index < len(self.chunks):
                # Cropping, subtracting the size from remaining_size
                crop_result = self.chunks[index].crop(remaining_size, self.max_length)
                remaining_size -= len(crop_result[0])
                result += crop_result[0]
                # The second element of crop_result indicates whether we have reached the full limit or if we can try further
                if crop_result[1]:
                    break
                else:
                    index = index + 1
           # Everything after the reached limit needs to be saved for the next message
            self.chunks = self.chunks[index:]
            # self.emit(result)
            self.fragments.append(result)
        else:
            result = ""
            for chunk in self.chunks:
                result += chunk.get_text()
            self.fragments.append(result)
            self.chunks = []

    def flush(self):
        while len(self.chunks) > 0:
            self.process()
