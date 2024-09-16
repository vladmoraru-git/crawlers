
n = int(input("Enter the number of participants: "))

scores = list(map(int, input("Enter the scores separated by space: ").split()))

unique_scores = list(set(scores))

unique_scores.sort(reverse=True)

runner_up = unique_scores[1]

print(f"The runner-up score is: {runner_up}")
