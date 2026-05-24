s="silent"
t="listen"

freq1={}
for ch in s:
    freq1[ch] = freq1.get(ch,0)+1
print(freq1)

freq2={}
for ch in t:
    freq2[ch] = freq2.get(ch,0)+1
print(freq2)

if freq1==freq2:
    print("Anagram")
else:
    print("Not Anagram")
