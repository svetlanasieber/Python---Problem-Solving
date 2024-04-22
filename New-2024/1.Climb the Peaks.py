from collections import deque
conquered_peaks = []
days = 0
portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])
peak_dict = {"Vihren":80, "Kutelo":90, "Banski Suhodol":100, "Polezhan":60, "Kamenitza":70}

while portions and peak_dict:
    days += 1
    if days > 7:
        break
    daily_p, daily_s = portions.pop(), stamina.popleft()
    daily_result = daily_p + daily_s
    if daily_result >= list(peak_dict.values())[0]:
        peak = list(peak_dict.keys())[0]
        conquered_peaks.append(peak)
        peak_dict.pop(peak)

if not peak_dict:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print("Conquered peaks:")
    for item in conquered_peaks:
        print(f'{item}')
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

