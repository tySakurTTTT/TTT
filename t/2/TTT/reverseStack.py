def reverse(stack):
    if not stack:
        return

        # 弹出栈底元素并获取其值
    i =  getAndRemoveLastElement(stack)

    # 逆序剩余元素
    reverse(stack)

    # 将栈底元素推到栈顶
    stack.append(i)


def getAndRemoveLastElement(stack):
    # 弹出栈顶元素
    result=stack.pop()

    if not stack:
        return result
    else:
        last=getAndRemoveLastElement(stack)
        stack.append(result)
        return last

stack = [1, 2, 3, 4, 5]
reverse(stack)
print("逆序后的栈:", stack)
