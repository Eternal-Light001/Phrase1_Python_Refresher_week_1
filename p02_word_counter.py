# Create a function with def that sentence a the argument or parameter
# Split the sentence fro the def and count the words
# Count the words that it is the same
# Create a dictionary that accept Ket:value. The word name and the time it appear.
# function should be outside the def code so it can accept and run.

# TEST TABLE
# """
# {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}

def word_count(sentence):
    words = sentence.split(" ",)
    
    count = { }

    for word in words:
        if word in count:
            count[word] = count[word] + 1

        else:
            count[word] = 1

    return count

if __name__ == "__main__":
    output = word_count("the cat and the dog and the bird")
    print(output)   












