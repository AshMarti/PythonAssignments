num = int(input())
buses = list(map(int,input().split(' ')))
buses.sort()
buses.append(0)
to_combine = [buses[0]]

for i in range(1,num+1):
	if (buses[i] -1) == buses[i-1]:
		to_combine.append(buses[i])
	elif (buses[i] -1) != buses[i-1]:
		if len(to_combine)<=2:
			print((" ".join(list(map(str, to_combine)))), end = ' ')
		if len(to_combine) > 2:
			print(f'{to_combine[0]}-{buses[i-1]}', end = ' ')
		to_combine = [buses[i]]
