import csv

wordfilepath = r'C:\Users\matts\Projects\GitHub\GreekLearningApp\greek-learning-app\python\datasets\ell_news_2024_10k-words-sanitised.txt'


class Word:

    def __init__(self, display, sortcode, frequency):
        self.display = display
        self.sortcode = sortcode
        self.frequency = frequency

    def __str__(self):
        return f'{str(self.sortcode)}: {self.display} ({str(self.frequency)})'


wordlist = []


with open(wordfilepath, encoding='utf-8') as wordsfile:
    reader = csv.reader(wordsfile, delimiter='|')
    for row in reader:
        d = row[1]
        s = int(row[0])
        f = int(row[2])
        w = Word(d, s, f)
        wordlist.append(w)


for i in range(0, 5):
    print(wordlist[i])