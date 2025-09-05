roster = [
    ["Alice",  [85, 92, 88]],
    ["Bob",    [70, 76, 81]],
    ["Diana",  [95, 91, 93]],
    ["Joshua", [89, 90, 87]],
] 



for name, scores in roster:
    total = 0
    for score in scores:
        total += score
    avg = total / len(scores)
    print (name, "- avg:", avg, "high:", max(scores), "low:", min(scores))