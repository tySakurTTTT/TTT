def get_digit(num, d):
    # 获取数字 num 在十进制下第 d 位上的数
    for _ in range(d - 1):
        num //= 10
    return num % 10

def max_bits(arr):
    # 计算数组中的最大数有多少十进制位
    max_val = max(arr)
    result = 0
    while max_val != 0:
        result += 1
        max_val //= 10
    return result

def radix_sort(arr):
    if arr is None or len(arr) < 2:
        return

    def radix_sort_internal(begin, end, digit):#digit多少个十进制位，也代表入桶出桶的次数
        radix = 10
        bucket = [0] * (end - begin + 1)

        for d in range(1, digit + 1):
            count = [0] * radix#//用于记录当前位上等于0,...,等于9的各有多少个数

            for i in range(begin, end + 1):
                j = get_digit(arr[i], d)#//确认当位上的数是多少
                count[j] += 1#//等于该位上的数，统计加1

            # / 用于记录当前位上小于等于0, ..., 小于等于9的各有多少个数
            # // 同时也记录了当前位上等于0, ..., 等于9的数组最后一个数出桶后的位置
            for i in range(1, radix):
                count[i] = count[i] + count[i - 1]

            for i in range(end, begin - 1, -1):
                j = get_digit(arr[i], d)
                bucket[count[j] - 1] = arr[i]#/出桶后的位置上放该数
                count[j] -= 1

            for i in range(begin, end + 1):
                arr[i] = bucket[i - begin]

    digit = max_bits(arr)
    radix_sort_internal(0, len(arr) - 1, digit)

# 示例用法:
arr = [3, 1, 44, 12, 5, 9, 22, 6, 57, 389, 123]
radix_sort(arr)
print(arr)
