n,m =map(int,input().split())
items=list(map(int,input().split()))

#n=number of boxes
#m=number of items
#items=the number of each item that exists
#open fewest amount of boxes

items.sort()
boxestoopen=n-items[0]+1
print(boxestoopen)