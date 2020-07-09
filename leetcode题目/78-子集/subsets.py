"""
题目描述：
给定一组 不含重复元素 的数组nums，返回该数组的所有可能得子集（幂集），解集不能包含重复的子集。
解法1.递归

"""
def subsets(nums):
    output = [[]]
    for num in nums:
        print(num)
        output += [curr + [num] for curr in output]
        print('this line:', output)
    return output

print(subsets([0,1,2]))
