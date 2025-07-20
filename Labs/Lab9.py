def sum_even_numbers(nums):
    if len(nums) == 0:
        return 0

    if nums[0] % 2 != 0:
        return sum_even_numbers(nums[1:])
    
    elif nums[0] % 2 == 0:
        return nums[0] + sum_even_numbers(nums[1:])
        
a = sum_even_numbers([1,2,3,4,5,6,7,8,9,10])
print(a)