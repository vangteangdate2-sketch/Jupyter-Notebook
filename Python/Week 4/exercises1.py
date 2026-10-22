scores = [75,80,65,90,85,70]

# a) display the entire list
print(scores)

# b) display the first score
print(scores[0])

# c) display the last score
print(scores[-1])

# d) display the third score
print(scores[2])

# e) display the number of scores
print(len(scores))

# f) calculate the total and average score
total = sum(scores)
avg = total / len(scores)
print("total:",total,"average",avg)

# g) sort
scores.sort()
print(scores)

# h) reverse
scores.reverse()
print(scores)

# i) display the first three number
print(scores[0:3])

# j) display every second number
print(scores[::2])

# add 5 mark to every list
extra = [score + 5 for score in scores]
print(extra)








