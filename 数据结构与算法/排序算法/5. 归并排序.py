"""
归并排序（MERGE-SORT）是利用归并的思想实现的排序方法。
该算法采用经典的分治（divide-and-conquer）策略。
分治法将问题分(divide)成一些小的问题然后递归求解，而治(conquer)的阶段则将分的阶段得到的各答案"修补"在一起，即分而治之。
"""

'''
时间复杂度: O(nlogn) 归递排序在排序过程中需要开辟中转空间，所以空间复杂度是大于希尔排序的
空间复杂度：O(n)
'''

a = [6, 4, 2, 1, 7, 5, 10, 22, 17, 23, 14, 3, 9, 16, 27, 33, 31, 22, 13, 6, 7]


# min = 0
# max = len(a) - 1
#
#
# # 分解递归
# def divide(seq, min, max):
#     # 递归终止条件
#     if max <= min:
#         return
#
#     mid = int((min + max) / 2)
#
#     # 递归调用。拆分序列
#     divide(seq, min, mid)
#     divide(seq, mid + 1, max)
#
#     # 合并序列。在合并的过程中实现排序
#     merge(seq, min, mid, max)
#
#
# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#
#     # 创建临时数组
#     L = list()
#     R = list()
#
#     # 拷贝数据到临时数组 arrays L[] 和 R[]
#     for i in range(0, n1):
#         L.append(arr[l + i])
#
#     for j in range(0, n2):
#         R.append(arr[m + 1 + j])
#
#     # 归并临时数组到 arr[l..r]
#     i = 0  # 初始化第一个子数组的索引
#     j = 0  # 初始化第二个子数组的索引
#     k = l  # 初始归并子数组的索引
#
#     # 从两个临时数组中依次取出较小的值放入到原数组
#     # 直到 有一个临时数组被取完
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     # 下面两个 while 就是说，哪个临时 数组 还有剩，就将剩下的直接拷贝给原数组
#     # 拷贝 L[] 的保留元素
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # 拷贝 R[] 的保留元素
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# if __name__ == '__main__':
#     divide(a, min, max)
#     print(a)


def divide(seq):
    m = len(seq)
    if m <= 1:
        return seq

    mid = m // 2

    r1 = divide(seq[0: mid])
    r2 = divide(seq[mid: m])

    return merge(r1, r2)


def merge(r1: list, r2: list):
    tmp = []

    while r1 and r2:
        if r1[0] < r2[0]:
            tmp.append(r1.pop(0))
        else:
            tmp.append(r2.pop(0))

    if r1:
        tmp.extend(r1)

    if r2:
        tmp.extend(r2)

    return tmp


if __name__ == '__main__':
    print(divide(a))
