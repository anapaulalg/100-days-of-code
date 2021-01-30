# Merge Sorted Array



def merge(nums1, nums2):
    countNums1 = len(nums1)
    countNums2 = 0
    for i in range(len(nums1)):
        if nums1[i] == 0:
            for j in range(len(nums2)):
                nums1[i] = nums2[j]
                nums2.pop(j)
                countNums2 = countNums2 + 1
                break
    mergedArray = nums1
    mergedSorted = sorted(mergedArray)
    print(mergedSorted)

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    merge(nums1, nums2)


