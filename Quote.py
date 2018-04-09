class Quote:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author
    def __gt__(self, user2):
        if self.quote > user2.quote:
            return True
