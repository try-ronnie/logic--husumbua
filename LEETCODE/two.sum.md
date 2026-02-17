Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



answer given : i used nested loops to add each until the value is the same as target
```
class Solution(object): def twoSum(self, nums:list, target:int): """ :type nums: List[int] :type target: int :rtype: List[int] """ nums_list = nums tar = target list_output = [] for i in nums_list: for each in nums_list: res = i + each if res == tar: list_output.append(i) list_output.append(each) else: pass
```
but this case i had the following errors :
    1. i didnt return the indices ... ireturned the numbers themselves
    2. i had the run time of O(n^2) and the required time complexity was 0(2n)

solution and learning points :
1. **question logic**: the func has 2 inputs 
            num - list of interger
            target - number we want to reach 
        the sum of any 2 numbers in the list should be returned with their respective indices(positioning on the list)

2. we use a dict to store the value and its positioning on the list .... (the good thing about dicts you store key value pairs ..... and also it doesnt allow duplicates)

3. we then use the for loop to loop over the list to perform the required operation.
``` for i , num in enumarate (list):```
    enumarate method gives both the value and the index of the value hence 2 variables in the for loop , 
        so first loop variable (i)- index
        second    variables (num)
    its the cleaner version of 
        ```for i in range(len(nums)):                                                   num = nums[i]```


4. then we reason that the target - num(the number we iterate over) = complement ..
then we know that the number left should be paired with the one on the list to reach the target 
so instead of checking every number we ask then in the dict weve stored whether it has the complement left
we store this complement as its own variable
```
complement = target - num
```


5. we then check the dict keys to see if the complement is in the seen values ... if seen in the values it means that the complement and th num exist meaing the shoud be paired only if in the dict memory


loop logic - in every loop :
                1. we need to assign the number to a dict ...(if its the first number and the complement isnt there it will run the the next digit
                )
                2. if the complement is there then it means that the number is in the list and it can be paired with the num we are iterating over ( num changes every loop but the target is the same .... so if the complement is in the dict meaning it was in the list and we looped over it.... meaning that the current num we are looping over can be paired witht he complement value stored in the dict since it was a num (a number we looped ogver in one of the loops))
                3. then we need to return both indices value of the two number that pair up (sum up)to target

 
*range logic*
```
num = [2,3,6,9,0,9]

for 