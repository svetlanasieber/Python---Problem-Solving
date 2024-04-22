from collections import deque
textiles = deque([int(x) for x in input().split(" ")])
medicaments = [int(x) for x in input().split(" ")]
med_dict = {}
item_dict = {"Patch":30, "Bandage":40, "MedKit":100}

while textiles and medicaments:
    bandage = textiles.popleft()
    pill = medicaments.pop()
    result = bandage + pill
    if result > 100:
        med_diff = result - 100
        temp_med = medicaments.pop()
        medicaments.append(temp_med + med_diff)
        if "MedKit" in med_dict:
            med_dict["MedKit"] += 1
        else:
            med_dict["MedKit"] = 1
    elif result not in item_dict.values():
        medicaments.append(pill + 10)
    else:
        med_item = "".join(k for k, v in item_dict.items() if v == result)
        if med_item in med_dict:
            med_dict[med_item] += 1
        else:
            med_dict[med_item] = 1
if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
if not textiles and medicaments:
    print("Textiles are empty.")
if not medicaments and textiles:
    print("Medicaments are empty.")
result = sorted(med_dict.items(), key=lambda x:(-x[1],x[0]))
for k, v in result:
    print(f"{k} - {v}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments])}")


