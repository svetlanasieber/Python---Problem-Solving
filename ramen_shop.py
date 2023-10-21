from collections import deque

bowls = list(map(int, input().split(',')))
customers = deque(map(int, input().split(',')))

while True:

    if len(bowls) == 0 or len(customers) == 0:
        break

    current_bowl = bowls.pop()
    current_customer = customers.popleft()

    if current_bowl > current_customer:
        current_bowl -= current_customer
        bowls.append(current_bowl)
    elif current_bowl < current_customer:
        current_customer -= current_bowl
        customers.appendleft(current_customer)

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(i) for i in bowls)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(i) for i in customers)}")