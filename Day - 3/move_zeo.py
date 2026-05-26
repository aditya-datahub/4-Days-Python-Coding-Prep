nums = [0,1,0,3,12]

insert_position = 0

for num in nums:

    if num != 0:
        nums[insert_position] = num
        insert_position += 1

while insert_position < len(nums):
    nums[insert_position] = 0
    insert_position += 1

print(nums)