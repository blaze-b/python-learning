"""Retrieve and print words from a URL."""

from urllib.request import urlopen

DEFAULT_URL = "http://sixty-north.com/c/t.txt"


def fetch_words(url=DEFAULT_URL):
    """Fetch a list of words from the URL."""
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            story_words.extend(line_words)
    return story_words


def print_words(words):
    """Print each word on its own line."""
    for word in words:
        print(word)


def main(url=DEFAULT_URL):
    """Fetch words from *url* and print them."""
    words = fetch_words(url)
    print_words(words)


if __name__ == "__main__":
    main()
