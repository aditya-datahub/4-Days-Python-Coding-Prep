#Question 1 → Character Frequency

s = "programming"
freq={}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq)

# Question 2 → Total Word Frequency in a sentence
sentence = "data python data sql python"
words = sentence.split()
freq={}
for word in words:
    freq[word] = freq.get(word,0)+1
print(freq)


# Question 3 → First Non-Repeating Character
string = "aabbm"
for char in string:
    if string.count(char) == 1:
        print("First Non-Repeating:", char)
        break
else:
    print("Not Found!")