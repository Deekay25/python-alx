"""
- so queues works similar to stacks
- the difference you pop from the first element that goes in
- it goes with Fist In First out FIFO phenomenon
"""


# stack = []

# # enque
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# print(stack)

# #deque
# # with stacks I will use pop() with no argument
# # with ques I will use pop(0)
# stack.pop(0)
# stack.pop(0)
# print(stack)

# -the downside to the above using the lists is  when you pop it goes through each list
# - to change their index which will be very slow for a pretty big list
# - solution to it in python
from collections import deque

data = deque()
data.append(1)
data.append(2)
data.append(2)
print(data)
data.popleft() # no need to pass zero
print(data)