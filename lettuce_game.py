import time
import random
inven = []
aa = 0
def 상추심기():
    global aa
    print("상추를 심었습니다.")
    time.sleep(1)
    a = random.randint(1, 1000)
    if a == 1000:
        print("심자마자 상추가 방사능에 피폭 당하였습니다.\n")
        inven.append("X-상추")
    if a == 1:
        print("심자마자 돈이 자라는 상추에 당첨 되었습니다.\n")
        aa += 1000
    else:
        print("상추가 정상적으로 자랐습니다.\n")
        aa += 100
while(1):
    b = input("수행 할 작업을 입력해주세요.\n>>>")
    if b == "상추심기":
        상추심기()
    elif b == "인벤토리":
        print(inven)
    elif b == "지갑":
        print(str(aa) + "원")