words_compare_list = []

def spliting(word):
    word = list(word)
    if word[-1] == '\n':
        word.remove(word[-1])
    return word

def annagram(wordlist):
    for word in wordlist:
        spliting(word)
        print(word)
    # return wordlist

with open('words_list.md','r', encoding="UTF-8") as f:
    for line in f.readlines():
        chars = spliting(line)
        words_compare_list.append(chars)
        match = annagram(words_compare_list)
        print(match, end='')
