left_lane=input().split(" ")
right_lane=input().split(" ")

left_car=0
right_car=0
lane=[]
# Solve the problem
while (left_car<len(left_lane)) and (right_car<len(right_lane)):
	lane.append(left_lane[left_car])
	lane.append(right_lane[right_car])
	left_car+=1
	right_car+=1
if left_car<len(left_lane):
	lane.extend(left_lane[left_car:])
if right_car<len(right_lane):
	lane.extend(right_lane[right_car:])

# Print the result
print(" ".join(lane))