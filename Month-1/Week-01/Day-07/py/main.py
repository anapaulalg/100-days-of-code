# Merge Sorted Array

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

def merge(nums1, nums2):
    countNums1 = len(nums1)
    countNums2 = 0
    for i in range(len(nums1)):
        print(i)
        if nums1[i] == 0:
            for j in range(len(nums2)):
                print(j)
                print("Nums1")
                print(countNums1)
                print("Nums2")
                print(countNums2)
                nums1[i + countNums2] = nums2[j]
                nums2.pop(j)
                countNums2 = countNums2 + 1
                print(nums1)

merge(nums1, nums2)