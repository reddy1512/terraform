from operator import truediv

nums = [34,56,23,42,9,21]
print(len(nums))
for i in range(1,len(nums)):
    print(f"iteration: {i}")
    key = nums[i]
    j = i -1
    print(f"j value: {j}, key:{key}")
    while j>=0 and nums[j] > key:
        print(f"While loop iteration: {j}")
        nums[j + 1] = nums[j]
        j-=1
        print(nums)
    print("-----------------------")
    nums[j+1] =key
    print(nums)
    print("***************************************************8")


# iteration 1 : i=1, key 56, j=0, nums[j] = 34 > key 36 -- false, nums[j+1] = 56 = key
# iteration 2 : i=2, key 23, j=i-1--2-1=1,
# j=1,nums[j] = 56> key 23,
# enter into while loop: nums[j+1] = nums[j] 56-- now nums[j+1] = 56, [34,23,56]
# j=j-1 = 0 & nums[0] 34> key 23 nums[j+1] = nums[j]34 -- nums[j+1] = nums[1] = 34, j-=1 = j=-1
# loop fails comes outcome [23,34,56,42,9,21]
# iteration 3 : nums[i] = nums[3] = 42 = key, j=i-1 = 2
# enter into while loop: j>=0 & nums[j] 56 > key 42 -- true
# nums[j+1] = nums[3] = nums[j] 56, j-=1 , j=1 = [23,34,42,56,9,21]
# 4 iteratio: i=4, key = 9, j=3
# enter the while loop: n[j] 56 > key: nums[j+1(4)] 9 = nums[j] 56, j=2,
# nums[j] 42 > key 9: nums[j+1(3)] =