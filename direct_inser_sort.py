def quick_sort(arr, left, right):
    if left < right:
        # 划分操作
        pivot_index = partition(arr, left, right)
        # 对左右子序列分别递归进行快速排序
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
def partition(arr, left, right):
    # 选择最后一个元素作为枢轴
    pivot = arr[right]
    # 初始化指针 i 和 j
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            # 将小于枢轴的元素移到左边
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 将枢轴放到正确的位置上
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
if __name__ == '__main__':
    # 从键盘输入需要排序的数字
    print("请输入需要排序的数字，以空格隔开:")
    arr = list(map(int, input().split()))
    # 调用快速排序函数
    quick_sort(arr, 0, len(arr) - 1)
    # 输出排序后的结果
    print(arr)