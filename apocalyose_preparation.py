from collections import deque

textile = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

patch = 30
bandage = 40
medkit = 100

dic_count = {
'Patch': 0,
'Bandage': 0,
'MedKit': 0
}

while True:

    if len(textile) == 0 and len(medicaments) == 0:
        print("Textiles and medicaments are both empty.")
        break

    if len(textile) == 0:
        print("Textiles are empty.")
        break

    if len(medicaments) == 0:
        print("Medicaments are empty.")
        break

    current_textile = textile.popleft()
    current_medicaments = medicaments.pop()

    sum_text_medical = current_textile + current_medicaments

    if sum_text_medical == patch:
        dic_count['Patch'] += 1
    elif sum_text_medical == bandage:
        dic_count['Bandage'] += 1
    elif sum_text_medical == medkit:
        dic_count['MedKit'] += 1
    elif sum_text_medical > medkit:
        dic_count['MedKit'] += 1
        diff = abs(medkit - sum_text_medical)
        next_medical = medicaments.pop()
        next_medical += diff
        medicaments.append(next_medical)
    else:
        current_medicaments += 10
        medicaments.append(current_medicaments)


for key, value in sorted(dic_count.items(), key=lambda x: (-x[1], x[0])):
    if value != 0:
        print(f'{key} - {value}')
if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicaments))}")
if textile:
    print(f"Textiles left: {', '.join(str(x) for x in textile)}")