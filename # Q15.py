# Q15. Word Frequency Counter

print("\n" + "=" * 50)
print("Q15. Word Frequency Counter")
print("=" * 50)

sentence = "I love python python"
print("Sentence:", sentence)

freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

print("Frequency:", freq)