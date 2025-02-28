#Only works if file is run same directory as text file

def filetodict(filename):
    fin = open(filename)
    words = dict()
    i=0
    for word in fin:
        word = word.strip()
        words[word] = i
        i=i+1
    return words

words = filetodict('words.txt')