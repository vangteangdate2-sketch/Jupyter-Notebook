scores = [45,70,85,35,90,60,50,95]
# assume a passing score is 50

# 1) create a list of passing scores
passing_score = list(filter(lambda x: x >= 50, scores))
print("Passing Score:", passing_score)

# 2) create a list Failing failing scores
failing_score = list(filter(lambda x: x <= 50, scores))
print("Failing Score:", failing_score)

# 3) count the passing students
passing_count = len(passing_score)
print(passing_count)

# 4) calculate the avg of passing score only
avg_passing = sum(passing_score) / len(scores)
print(avg_passing)

# 5) create a list of excellent scores
excellent_score = list(filter(lambda x: x >= 80, scores))
print("excellent Score:", excellent_score)