def num1(n):
    if n < 1:
        return 0
    record = [0] * n
    return process1(0, record, n)

def process1(i, record, n):
    if i == n:
        return 1
    res = 0
    for j in range(n):
        if is_valid(record, i, j):
            record[i] = j  #能不能把record[i]放在第i行
            res += process1(i + 1, record, n)#深度优先
    return res

def is_valid(record, i, j):
    for k in range(i):
        if j == record[k] or abs(record[k] - j) == abs(i - k):
            return False
    return True

# Example usage:
n = 8
result = num1(n)
print(result)


def num2(n):
    if n < 1 or n > 32:
        return 0
    # n皇后问题，就用n位2进制数表示下一行位置上的限制位上为1代表能试
    upper_lim = -1 if n == 32 else (1 << n) - 1
    return process2(upper_lim, 0, 0, 0)

def process2(upper_lim, col_lim, left_dia_lim, right_dia_lim):
    if col_lim == upper_lim:
        return 1
    pos = 0
    most_right_one = 0
    # pos 代表能填皇后的位置，与upper_lim与运算为了屏蔽高位无关信息位上为1代表能试
    pos = upper_lim & (~(col_lim | left_dia_lim | right_dia_lim))
    res = 0
    while pos != 0:
        most_right_one = pos & (~pos + 1)  # 提取最右位置上的1来填皇后
        pos = pos - most_right_one  # 提取完把那个位减掉
        # 并将这个位加入到列限制，左对角线限制，右对角线限制中
        res += process2(upper_lim, col_lim | most_right_one,
                        (left_dia_lim | most_right_one) << 1,
                        (right_dia_lim | most_right_one) >> 1)
    return res

# Example usage:
n = 8
result = num2(n)
print(result)


