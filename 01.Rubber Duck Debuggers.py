from collections import deque
all_time = deque([int(x) for x in input().split(" ")])
tasks = [int(x) for x in input().split(" ")]
duck_dick = {"Darth Vader Ducky" : 0, "Thor Ducky" : 0,
             "Big Blue Rubber Ducky" : 0, "Small Yellow Rubber Ducky" : 0}
result_dict = {"Darth Vader Ducky" : 60, "Thor Ducky" : 120,
               "Big Blue Rubber Ducky" : 180, "Small Yellow Rubber Ducky" : 240}

while all_time and tasks:
    check_time = all_time[0]
    check_task = tasks[-1]
    result = check_time * check_task

    if result > result_dict["Small Yellow Rubber Ducky"]:
        tasks[-1] -= 2
        one_time = all_time.popleft()
        all_time.append(one_time)
    else:
        one_time = all_time.popleft()
        task = tasks.pop()
        result = one_time * task

        if result <= result_dict["Darth Vader Ducky"]:
            duck_dick["Darth Vader Ducky"] += 1

        elif result_dict["Darth Vader Ducky"] < result <= result_dict["Thor Ducky"]:
            duck_dick["Thor Ducky"] += 1

        elif result_dict["Thor Ducky"] < result <= result_dict["Big Blue Rubber Ducky"]:
            duck_dick["Big Blue Rubber Ducky"] += 1

        else:
            duck_dick["Small Yellow Rubber Ducky"] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for k, v in duck_dick.items():
    print(f'{k}: {v}')


