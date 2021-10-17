scores=input()
scores=scores.split(" ")
output=""
if (scores.count(scores[0])>1) or (scores.count(scores[1])>1):
	output="similar"
	if scores.count(scores[0])==3:
		output="same"
elif scores.count(scores[0])==1 and scores.count(scores[1])==1:
	output="distinct"
print(output)