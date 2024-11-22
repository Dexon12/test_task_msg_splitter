from html_parse_solution.text_content import TextContent

# Эти теги можно дробить
BLOCK_TAGS = [
    "p",
    "b",
    "strong",
    "i",
    "ul",
    "ol",
    "div",
    "span"
]

class Tag:
    def __init__(self, tag, attrs):
        super().__init__()
        self.parent = None
        self.tag = tag
        self.attrs = attrs
        self.children = []
        self.closed = False
        # Reconstruct the start tag and save it as a text child, so it can be handled like all other tag elements
        start_tag = "<" + tag
        for pair in attrs:
            start_tag += " " + pair[0] + "=\"" + pair[1] + "\""
        start_tag += ">"
        self.children.append(TextContent(start_tag))
        # Reconstruct the end tag and save it as a text child, so it can be handled like all other tag elements
        end_tag = "</" + tag + ">"
        self.children.append(TextContent(end_tag))

    def add_child(self, child):
        # Need to insert it as the penultimate element to avoid shifting the closing tag
        self.children.insert(len(self.children)-1, child)
        child.parent = self
        return child

    def get_size(self):
        result = 0
        for tag in self.children:
            result += tag.get_size()
        return result

    def get_text(self):
        # This function returns the entire tag as a whole
        result = ""
        for child in self.children:
            result += child.get_text()
        return result

    def crop(self, size, max_len):
        self_size = self.get_size()
        # If the tag fits within the size, return it entirely
        if self_size <= size:
            return self.get_text(), False

        # If it doesn't fit and isn't a block-level tag, we won't return anything and will indicate that the limit has been reached
        if self.tag not in BLOCK_TAGS:
            if self_size > max_len:
                raise Exception("Can't fit content in one fragment")
            else:
                return "", True

        # # This is a check in case even the opening/closing tags don't fit within the size
        # Similar to the previous one
        start_tag_size = self.children[0].size
        close_tag_size = self.children[len(self.children) - 1].size
        if size < start_tag_size + close_tag_size:
            return "", True

        # Directly place the opening tag into result
        result = self.children[0].get_text()
        # And in remaining_size, we immediately remember that we also have a mandatory closing tag
        remaining_size = size - start_tag_size - close_tag_size
        max_len_without_start_end_tag = max_len - start_tag_size - close_tag_size
        # Skip the first element and don't reach the last one (overcautious, actually it wouldn't get there anyway)
        for i in range(1, len(self.children)):
            tag = self.children[i]
            # Recursive crop
            crop_result = tag.crop(remaining_size, max_len_without_start_end_tag)
            if crop_result[1]:
                # Reached the limit, remember that the nested tag was returned
                result += crop_result[0]
                # Add the closing tag
                result += self.children[len(self.children) - 1].get_text()
                # And remove from the children array those that were included in the resulting message
                # At the same time, do not touch the opening/closing tags, they will be needed in the next message
                new_children = [self.children[0]]
                for j in range(i, len(self.children) - 1):
                    new_children.append(self.children[j])
                new_children.append(self.children[len(self.children) - 1])
                self.children = new_children
                break
            else:
                # If the limit has not been reached, simply note how much the available space in the message has decreased and append the text
                result += crop_result[0]
                remaining_size -= len(crop_result[0])
        return result, True
