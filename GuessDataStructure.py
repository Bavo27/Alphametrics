import sys
from collections import deque
import heapq

def guessTheDataStructure():
    for line in sys.stdin: # to loop over the inputs repeatedly
        numTimes = int(line.strip()) # read in number of lines
        stack = []
        queue = deque()
        priority_queue = []
        isStack = True
        isQueue = True
        isPriority = True
        for i in range(numTimes): # loop over that many times
            x,y = input().split()
            x = int(x.strip())
            y = int(y.strip())
            if x == 1:
                stack.append(y)
                queue.append(y)
                heapq.heappush(priority_queue, -y)
            elif x == 2:
                if isStack:
                    if len(stack) == 0 or stack.pop() != y:
                        isStack = False
                if isQueue:
                    if len(queue) == 0 or queue.popleft() != y:
                        isQueue = False
                if isPriority:
                    if len(priority_queue) == 0 or abs(heapq.heappop(priority_queue)) != y:
                        isPriority = False
            
        if isStack == False and isQueue == False and isPriority == False:
            print("impossible")
        elif isStack == True and (isQueue == False and isPriority == False):
            print("stack")
        elif isQueue == True and (isStack == False and isPriority == False):
            print("queue")
        elif isPriority == True and (isStack == False and isQueue == False):
            print("priority queue")
        else:
            print("not sure")

guessTheDataStructure()