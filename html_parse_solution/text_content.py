class TextContent:
    def __init__(self, text):
        super().__init__()
        self.parent = None
        self.text = text
        self.size = len(self.text)

    def get_size(self):
        return self.size

    def crop(self, size, max_len):
        if self.size > max_len:
            raise Exception("Can't fit content in one fragment")
        if self.size > size:
            return "", True
        else:
            return self.text, False

    def get_text(self):
        # return self.text # If you want the number of chars to match the one in the example
        return self.text.split() # It`s better to split because the fewer chars go into the network, the better
    
