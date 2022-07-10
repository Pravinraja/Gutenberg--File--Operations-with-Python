import operator
f = open("gutenberg.txt", "r")
print(f.read())
def count_occurrences(fname,word):
    #fname = "gutenberg.txt"

    #word = "The"

    k = 0

    with open(fname, 'r') as f:

        for line in f:

            words = line.split()

            for i in words:

                if (i == word):
                    k = k + 1

    print("Occurrences of the word: " + word)

    print(k)

count_occurrences("gutenberg.txt", "the")
count_occurrences("gutenberg.txt", "said")
count_occurrences("gutenberg.txt", "fast")