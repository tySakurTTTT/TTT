def printAllSubsquence(str):
    chs=list(str)
    process(chs,0)

def process(chs ,i):
    if (i==len(chs)):
        print(''.join(chs))
        return

    # 第i位上的字符打印
    process(chs,i+1)
    tmp=chs[i]
    # 第i位上的字符不打印
    chs[i]=""
    process(chs,i+1)
    chs[i]=tmp

def function(str):
    chs=list(str)
    process_with_list(chs,0,[])

def process_with_list(chs,i ,res):
    if i==len(chs):
        print_list(res)
        return

    res_keep=res.copy()
    res_keep.append(chs[i])
    process_with_list(chs,i+1,res_keep)

    res_no_include = res.copy()
    process_with_list(chs, i + 1, res_no_include)


def print_list(lst):
    print(''.join(lst))


# 示例用法
printAllSubsquence("abc")
function("abcd")


#打印字符串全排列，不重复

def process(chs,i,res):
    if i==len(chs):
        # 将所有结果记录到res中
        res.append(''.join(chs))
        return

    # 用来记录这个字符有没有试过，为了去掉重复的
    # 例如aaabb，交换0位置和0位置时，会记录
    visit=[False]*26
    for j in range(i,len(chs)):
        if not visit[ord(chs[j])-ord("a")]:
            visit[ord(chs[j]) - ord('a')] = True
            swap(chs, i, j)
            process(chs, i + 1, res)
            swap(chs, i, j)

def swap(chs, i, j):
            chs[i], chs[j] = chs[j], chs[i]
# 示例用法
result = []
process(list("aaabb"), 0, result)
print(result)

