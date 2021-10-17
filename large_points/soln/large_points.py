# Good luck! Remember the points are *real*, not necessarily *integer*.
import math
n=int(input())
circles=[None]*n
for line in range(n):
    circles[line]=list(map(float,(input().split())))
m=int(input())
points=[None]*m
for line in range(m):
    points[line]=list(map(float,(input().split())))
for i in points:
    for j in circles:
        answer="Small"
        if (round(math.sqrt((i[0]-j[0])**2+(i[1]-j[1])**2),6)<=round(j[2],6)):
            answer="Large"
            break
    print(answer)
