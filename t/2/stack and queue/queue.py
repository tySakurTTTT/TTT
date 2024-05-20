from collections import deque

# 初始化队列
# 在 Python 中，我们一般将双向队列类 deque 当作队列使用
# 虽然 queue.Queue() 是纯正的队列类，但不太好用，因此不推荐
que: deque[int] = deque()

que.append(1)
que.append(2)
que.append(3)
que.append(4)
que.append(5)

front:int=que[0]
print(front)

pop:int=que.popleft()
print(pop)

size:int=len(que)
print(size)

is_empty:bool=len(que)==0
print(is_empty)