from typing import List

class Program:
    def __init__(self,start,end):
        self.start=start
        self.end=end

def best_arrange(progarms:List[Program],start:int) -> int:
    # 会议按结束时间，有小到大排列
    progarms.sort(key=lambda x:x.end)
    result=0
    for program in programs:
# 看当前会议的开始时间有没有比上一个安排的会议结束时间要晚，如果是，则安排此会议，并更新结束时间
          if start<=program.start:
              result+=1
              start=program.end
    return result


if __name__ == "__main__":
    # Example usage:
    programs = [Program(1, 3), Program(2, 5), Program(3, 6), Program(5, 8), Program(7, 9)]
    start_time = 1
    result = best_arrange(programs, start_time)
    print(result)
