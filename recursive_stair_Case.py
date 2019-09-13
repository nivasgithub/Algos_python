def num_ways_bottom_up(n):
    if n == 0 or n == 1:
        return 1
    nums = [0] * (n + 1)
    #print(nums.length)
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n + 1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]

def num_ways_x_bottom_up(n, x):
    if n == 0: return 1
    nums = [0] * (n + 1)
    nums[0] = 1
    for step in range(1, n + 1):
        total = 0
        for eStep in x:            
            if step - eStep >= 0:
                total = total + nums[step - eStep]
        print("With step: " + str(step) + " the total possible ways are: " + str(total))
        nums[step] = total
        total = 0
    return nums[n]

print("Steps from 0 to n are " + str(num_ways_bottom_up(5)))
print("Steps from 0 to n with eligibile steps are " + str(num_ways_x_bottom_up(5, [1,3,5])))
