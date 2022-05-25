# Projekt-Gutenberg-Scraper
A simple Web Scraper designed to scrape a book with given url from [Projekt Gutenberg DE](https://www.projekt-gutenberg.org/).\
Writes book content to .txt file which can be used for different NLP analyzation tasks or simply for reading.


## Usage example
```
# Books by composer Richard Wagner which are to be scraped from Projekt Gutenberg DE Website
# define books as tuples of url and path to result file

book_one = wagner_oper_und_drama, wagner_oper_und_drama_file = \
    "https://www.projekt-gutenberg.org/wagner/operdram/", "scraped_books/Oper_und_Drama.txt"

book_two = wagner_mein_leben_part_one, wagner_mein_leben_part_one_file = \
    "https://www.projekt-gutenberg.org/wagner/meinleb1/", "scraped_books/Mein_Leben_1.txt"

book_three = wagner_mein_leben_part_two, wagner_mein_leben_part_two_file = \
    "https://www.projekt-gutenberg.org/wagner/meinleb2/", "scraped_books/Mein_Leben_2.txt"

books = [book_one, book_two, book_three]

# Instantiate Scraper
scraper = ProjektGutenbergScraper()

# Scrape books
scraper.scrape_books(books)
```