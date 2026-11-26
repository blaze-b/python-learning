from urllib.request import urlopen

with urlopen("http://sixty-north.com/c/t.txt") as story:
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        story_words.extend(line_words)

for word in story_words:
    print(word)
