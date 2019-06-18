import sys

if __name__ == '__main__':
    money = 20000
    split = sys.stdin.readline().strip().split(' ')
    check = False
    for token in split:
        distance = int(token)
        if(distance < 4 or distance > 178):
            print(money)
            check = True
            break
        if(distance <= 40):
            temp = 720
        else:
            distance -= 40
            temp = (distance // 8) * 80 + 720
            if(distance % 8 != 0): temp += 80
        if(money - temp < 0):
            print(money)
            check = True
            break
        else: money -= temp
    if(check == False): print(money)
