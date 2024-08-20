
def removeDuplicates_brute(nums)->set[int]:
    #Using set
    return list(set(nums)) # Time Complexity: NlogN + N, Space Complexity: O(n)
    #Using list comprehension
    #return [i for i in set(nums)]
    #Using dictionary
    #return list(dict.fromkeys(nums))
    # length = len(nums)
    # print(length)
    # cleanList = nums.copy()
    # for i in range(1,length-1):
    #     if nums[i] == nums[i-1]:
    #         print(nums[i])
    #         print(nums[i-1])
    #         cleanList.pop(i)
    #         print(cleanList)
    # return cleanList

def removeDuplicates_optimal(nums)->int:
    #Using two pointers approach Time Complexity: O(n), Space Complexity: O(1)
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
   
def main():
    nums = [1,1,2,2,3,3,4,5,6,6]
    print(removeDuplicates_brute(nums))
    print(removeDuplicates_optimal(nums))

if __name__ == '__main__':
    main()