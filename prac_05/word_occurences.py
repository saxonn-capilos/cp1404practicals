"""
Word Occurences
Estimate: 30 minutes
Actual: 29 minutes
"""

sentence = "this is a collection of words of nice words this is a fun thing it is"
words = sentence.split()
word_to_count = dict.fromkeys(words, 0)
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
word_to_count = dict(sorted(word_to_count.items()))
longest_word = max(len(word) for word in word_to_count)
for word, count in word_to_count.items():
    print(f"{word:{longest_word}} : {count}")
