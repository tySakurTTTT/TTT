def max_value1(weights, values, bag):
    return process1(weights, values, 0, 0, bag)

def process1(weights, values, i, already_weight, bag):
    if already_weight > bag:
        return 0
    if i == len(weights):
        return 0
    return max(
        process1(weights, values, i + 1, already_weight, bag),
        values[i] + process1(weights, values, i + 1, already_weight + weights[i], bag)
    )

def process2(weights, values, i, already_weight, already_value, bag):
    if already_weight > bag:
        return 0
    if i == len(weights):
        return already_value
    return max(
        process2(weights, values, i + 1, already_weight, already_value, bag),
        process2(weights, values, i + 1, already_weight + weights[i], already_value + values[i], bag)
    )

# 示例用法：
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
bag_capacity = 8

result1 = max_value1(weights, values, bag_capacity)
print("方法1的最大价值:", result1)

result2 = process2(weights, values, 0, 0, 0, bag_capacity)
print("方法2的最大价值:", result2)
#其中 process1 每个物品要么放入背包，要么不放，而 process2 则记录已经放入背包的价值。