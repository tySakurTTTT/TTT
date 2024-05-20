def process(chs,i):
    if i==len(chs):
        return 1 # 之前的决定是有效的，返回一种组合方式

    if chs[i]=='0':
        return 0

    if chs[i]=='1':
        res=process(chs,i+1)
        if i+1<len(chs):
            res+=process(chs,i+2)
        return res

    if chs[i]=='2':
        res = process(chs, i + 1)
        if i + 1 < len(chs) and '0' <= chs[i + 1] <= '6':
            res += process(chs, i + 2)
        return res

        # 以上条件都不满足，说明字符不是0、1、2，直接前进到下一个字符
    return process(chs, i + 1)

# 示例用法：
input_chars = "123"
result = process(input_chars, 0)
print("组合方式总数:", result)