# Smallest number
nums = [5,2,9,1,7]
smallest=nums[0]
for num in nums:
    if num<smallest:
        smallest=num
print("Smallest number among all the numbers:",smallest)

# Sum of all numbers
nums = [1,2,3,4]
total=0
for num in nums:
    total+=num
print("Sum of all the elements:",total)

# Count Even Numbers
nums = [1,2,4,7,8]
count=0
for num in nums:
    if num%2==0:
        count+=1
print("Total Even numbers:",count)

# Reverse List/String
s="Hi I am Aditya"
words= s.split()
print(words)
reverse_words=" ".join(words[::-1])
print(reverse_words)
