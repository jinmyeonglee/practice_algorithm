import operator
T = int(input())

class dot(): # a class for storing dots
    x = 0
    y = 0
    slope = 0.0
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    def setSlope(self, standard):
        try: self.slope = ((self.y - standard.y) / (self.x - standard.x))
        except: self.slope = 0.0
    def getDistance(self, another):
        return (self.x - another.x)**2 + (self.y - another.y)**2

for t in range(T):
    n = int(input())
    arr = [] # a list of class dot
    stack = [] # for making convex hull
    min_x, min_y = 10000001, 10000001
    indexLowestDot = 0

    for i in range(n): # get inputs and set dot with picking the lowest dot
        x, y = map(int, input().split())
        arr.append(dot(x, y))
        if(x <= min_x and y < min_y):
            min_x, min_y = x, y #select the lowest dot
            indexLowestDot = i

    arr[0], arr[indexLowestDot] = arr[indexLowestDot], arr[0] # swap
    for i in range(1, n): # set each slope
        arr[i].setSlope(arr[indexLowestDot])
    arr.sort(key=operator.attrgetter('slope'))
    # sort by slope. python sorting is the stable one,
    # so can keep the lowest dot to be the first in arr
    # let's start making a convex hull
    stack.append(arr[0])
    stack.append(arr[1])
    for i in range(2, n):
        v1 = (stack[-1].x - stack[-2].x, stack[-1].y - stack[-2].y) # make a vector
        v2 = (arr[i].x - stack[-2].x, arr[i].y - stack[-2].y)
        if(((v1[0]*v2[1]) - (v2[0]*v1[1])) > 0): # if the new dot is in right side
            stack.append(arr[i])
        else:
            stack.pop()
            stack.append(arr[i])
    # end!!!
    x_mins = []
    x_mins.append(dot(10000001, 0))
    x_maxs = []
    x_maxs.append(dot(-10000001, 0))
    y_mins = []
    y_mins.append(dot(0, 10000001))
    y_maxs = []
    y_maxs.append(dot(0, -10000001))

    for i in range(len(stack)):
        if(stack[i].x < x_mins[-1].x):
            x_mins.pop()
            x_mins.append(stack[i])
        elif(stack[i].x == x_mins[-1].x):
            x_mins.append(stack[i])
        if(stack[i].x > x_maxs[-1].x):
            x_maxs.pop()
            x_maxs.append(stack[i])
        elif(stack[i] == x_maxs[-1].x):
            x_maxs.append(stack[i])

        if(stack[i].y < y_mins[-1].y):
            y_mins.pop()
            y_mins.append(stack[i])
        elif(stack[i].y == y_mins[-1].y):
            y_mins.append(stack[i])
        if(stack[i].y > y_maxs[-1].y):
            y_maxs.pop()
            y_maxs.append(stack[i])
        elif(stack[i] == y_maxs[-1].y):
            y_maxs.append(stack[i])

    x_maxs.sort(key=operator.attrgetter('y'))
    x_mins.sort(key=operator.attrgetter('y'))
    y_maxs.sort(key=operator.attrgetter('x'))
    y_maxs.sort(key=operator.attrgetter('x'))

    max = 0
    ans = ()
    temp = dot.getDistance(x_maxs[0], x_mins[-1])
    if(temp > max): max, ans = temp, (x_maxs[0], x_mins[-1])
    temp = dot.getDistance(x_maxs[-1], x_mins[0])
    if(temp > max): max, ans = temp, (x_maxs[-1], x_mins[0])
    temp = dot.getDistance(y_maxs[-1], y_mins[0])
    if(temp > max): max, ans = temp, (y_maxs[-1], y_mins[0])
    temp = dot.getDistance(y_maxs[0], y_mins[-1])
    if(temp > max): max, ans = temp, (y_maxs[0], y_mins[-1])

    print(ans[0].x, ans[0].y, ans[1].x, ans[1].y)
