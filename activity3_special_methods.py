class BookPages:
    def __init__(self, pages):
        self.pages = pages

    # for print()
    def __str__(self):
        return f"{self.pages} pages"

    # for + operator
    def __add__(self, other):
        return BookPages(self.pages + other.pages)


# Test
book1 = BookPages(120)
book2 = BookPages(85)

print(book1)          # 120 pages
result = book1 + book2
print(result)         # 205 pages