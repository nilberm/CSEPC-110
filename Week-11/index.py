with open("books.txt") as book_of_mormon:
  for line in book_of_mormon:
    line = line.strip()
    print(line)