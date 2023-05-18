nums = input("Введіть список чисел, розділених комами: ").split(',')
nums = [int(num.strip()) for num in nums]  

zeros_count = nums.count(0)  
nums = [num for num in nums if num != 0]  
nums += [0] * zeros_count 

print(nums)