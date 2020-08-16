# cook your dish here
arry = [3,5,-4,8,11,1,-1,6]
targetSum = 10


def two_sum(arry, targetSum): 
  nums = {}
  
  for number in arry: 
    possibleNum = targetSum - number
    if possibleNum in nums:
      return [possibleNum, number]
    else: 
      nums[number] = True
  return[]

result = two_sum(arry, targetSum)
print(result)
    


