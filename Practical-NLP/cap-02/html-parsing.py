from bs4 import BeautifulSoup
from urllib.request import urlopen

myurl = (
    "https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python"
)

html = urlopen(myurl).read()
soupified = BeautifulSoup(html, "html.parser")
question = soupified.find("div", {"class": "question"})
questiontext = question.find("div", {"class": "s-prose js-post-body"})

print(questiontext.get_text().strip())

answers = soupified.find("div", {"id": "answers"})
answer = answers.find("div", {"id": "answer-415519"})

print(answer.get_text())
