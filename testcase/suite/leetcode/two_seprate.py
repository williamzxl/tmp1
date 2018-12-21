# def binary_serach(l, item):
#     low = 0
#     high = len(l) - 1
#
#     while low <= high:
#         mid = int((low + high) / 2)
#         print("Low:", low, "High:",high, "Mid", mid)
#         guess = l[mid]
#         print("MID", mid, l[mid],guess)
#         if guess == item:
#             return mid
#         if guess < item:
#             low = mid + 1
#         if guess >= item:
#             high = mid - 1
# my = [1, 3, 5, 7, 9, 11,13,15, 17,19,21,22,24,26,27,32]
# print(binary_serach(my,11))


# from functools import reduce
# a = []
# for i in range(7):
#     a.append(2)
# print(a)
# b = reduce(lambda i,j:i*j , a)
# print(b)
# print(nums.remove(1))
# print(nums)
# nums2 = nums[-3:]
# nums = nums[:-3]
# print(nums2)
# print(nums)
# print(nums2 + nums)

# for i in range(1, k+1):
#     a = nums.pop(-1)
#     nums = [a] + nums
# print(nums)






# nums = [0,1,1,2, 3,4, 5,5]

# for i in range(0, len(nums) - 1):
#     if nums[i] in nums[i+1:]:
#         index = nums.index(i)
#         print("Index", index)
#         # nums.pop(index)
# print(nums)

# for i in range(len(nums) -1):
#     # print(i)
#     for j in nums[i+1:]:
#         if nums[i] == j:
#             nums.remove(j)
# print(nums)
# i = 0
# while i < len(nums) -1:
#     print("N",nums)
#     if nums[i] == nums[i+1]:
#         nums.remove(nums[i+1])
#     else:
#         i += 1
# print(nums)

nums = [7,1,5,3,6,4]
max = []
for i in range(len(nums) - 1):
    if nums[i + 1] > nums[i]:
        max1 = nums[i + 1] - nums[1]
        max.append(max1)

1 < 7:pass
5 < 7:pass
5 > 1:4
3 < 7: pass
3 > 1:2
3 < 5:pass
6 < 7:pass
6 > 1:5
6 > 5:1
6 > 3:3




