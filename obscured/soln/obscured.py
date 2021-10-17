line = list(map(int, input().split()))
heights = line[:]
height = -1
maxindex = 0
n=len(line)

for index in range(n):
    if line[index]>height:
        height = heights[index]
        maxindex = index
        line[index] = 'X'
    else:
        j = index -1
        while heights[index] > heights[j]:
            j = int(line[j])
        line[index] = str(j)

line=" ".join(line)
print(line)

"""line = list(map(int, input().split()))
height = -1
n=len(line)

for index in range(n):
    if line[index]>height:
        height = line[index]
        print('X', end = '')
    else:
        for j in range(index, 0, -1):
            if line[index]<=line[j-1]:
                print(str(j-1), end = '')
                break
    if index != (n-1):
        print(' ', end = '')
    if index == (n-1):
        print(' ')"""

