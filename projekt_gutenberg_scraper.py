import os
from io import TextIOWrapper
from bs4 import BeautifulSoup
import requests


class ProjektGutenbergScraper:

    def scrape_chapter(self, url: str, txt_file: TextIOWrapper) -> TextIOWrapper:
        """
        Scrapes the text content from a chapter of a book of Projekt Gutenberg DE Website (www.projekt-gutenberg.org)
        :param url: The url to the book chapter
        :param txt_file: opened txt file to write chapter to
        :return: txt_file
        """

        html_text = requests.get(url).content
        soup = BeautifulSoup(markup=html_text, features='lxml')
        # The book text lies in the <p> tags
        paragraphs = soup.find_all("p")
        for paragraph in paragraphs:
            paragraph_text = paragraph.get_text(strip=True, separator=" ")
            if paragraph_text != "":
                txt_file.write(paragraph_text)
        return txt_file

    def scrape_book(self, url: str, txt_file: TextIOWrapper) -> TextIOWrapper:
        """
        Scrapes the text content from a book of Projekt Gutenberg DE Website (www.projekt-gutenberg.org)
        :param url: The url to the book
        :param txt_file: opened txt file to write book to
        :return txt_file
        """

        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        # Find all chapters from the table of contents
        table_of_contents = soup.select("body ul li a")
        # Exclude titlepage
        table_of_contents = table_of_contents[1:]
        for chapter in table_of_contents:
            chapter_url = url + chapter["href"]
            print("Scraping chapter: ", chapter_url)
            txt_file = self.scrape_chapter(chapter_url, txt_file)
        print()
        return txt_file

    def scrape_books(self, books):
        for url, file in books:
            # check if book has been scraped already
            if os.path.isfile(file):
                print("Book has already been scraped to:", file)
                continue
            with open(file, "w", encoding="utf-8") as txt_file:
                print("Scraping book by Richard Wagner: ", url)
                txt_file = self.scrape_book(url, txt_file)


if __name__ == '__main__':
    # Usage example
    # Books by composer Richard Wagner which are to be scraped from Projekt Gutenberg DE Website
    # define books as tuples of url and path with filename
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
