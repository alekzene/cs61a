# FIXED Cannot open 'shakespeare.txt'

# opens 'shakespeare.txt' and names it shakes
shakes = open('C:/Users/user/Favorites/Downloads/shakespeare.txt')

# In this context, token is any string before/after every whitespace.
# While text refers to 'shakespeare.txt'

# reads the whole text and splits it per token and names it text
text = shakes.read().split()

# prints an array of the first 25 tokens in the text
text [:25]

# prints the no. of tokens in the text
len(text)

# counts the no. of occurrences of 'the' in the text
text.count('the')

# divides the no. of commas by the text length and names it comma_percentage
comma_percentage = text.count(',') / len(text)

# creates a set of all words used in the text and names it words
words = set(text)

# checks if a word is present in the set
'forsooth' in words # returns True
'the' in words # returns True

# prints the no. of elements in the set (AKA the number of unique words in the text)
len(words)

# reverses the string 'draw'
'draw'[::-1]

# prints all palindrome words present in the text with more than 4 characters
{w for w in words if w == w[::-1] and len(w) > 4}
# w for w in words means that w is an element in words
# w == w[::-1] means that w is equal to its reverse
# len(w) > 4 means that the length of w is greater than 4

# prints all four-character words with a reversed counterpart in the text
{w for w in words if w[::-1] in words and len(w) == 4}

# creates a set of all words in a dictionary, reads them and splits them into tokens
# FIXME 'str' object has no attribute 'read'
# text = open('/usr/share/dict/words'.read().split())
words = set(text)

# prints all six-character words with a reversed counterpart in the dictionary
{w for w in words if w[::-1] in words and len(w) == 6}
# a different set of words appear because words is now a set of words from a different source material

# NOTES
# len() is a function
# set(text) is an object

# TIP : These commands are best used in the IDLE.


