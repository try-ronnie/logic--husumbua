Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.


answer i gave out :
    
    lass Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs.length <= 200 and strs[ea]
        seen = {}
        for each in strs:
            split_word = each.split() # this returns a list but a list of the single word
            for letter in split_word:
                if letter in seen:
                    seen[letter] += 1 
                seen[letter] = 0
        if seen[letter] >= 1:
            return seen[letter],
    

        # list .. iterate over each word
        # check the first letters and store them somewhere 
        # then we need like a dict most-likely to store the or add the value pair ont how manytimes the word single letter has been used
        # if the prefixes of the next iteration are in the dict then just add to the value pair which will be how many times its been seen

but one thing atleast i knew is that my code was wrong ... first i didnt have a wy to ensure that the incoming list length is not more than 200 and lessa

But the real question was:
“Where do they stop matching?”