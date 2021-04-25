import time
import random
import lettuce_game
def 상추():
    print ("상추.")

def 상추_출력(s1):
    print(s1)

def 상추_만약(*s1):
    if s1[1] == "==":
        if s1[0] == s1[2]:
            if s1[3] == "상추":
                상추()
            elif s1[3] == "상추_출력":
                상추_출력(s1[4])
            else:
                print("상추 맛있음.")
    if s1[1] == "<":
        if s1[0] < s1[2]:
            if s1[3] == "상추":
                상추()
            elif s1[3] == "상추_출력":
                상추_출력(s1[4])
            else:
                print("상추 맛있음")
    if s1[1] == ">":
        if s1[0] > s1[2]:
            if s1[3] == "상추":
                상추()
            elif s1[3] == "상추_출력":
                상추_출력(s1[4])
            else:
                print("상추 맛있음")
def 삼겹살():
    print("상추에 싸먹으면 맛있음.")

def 상추_변수(name,s1, value):
    name = {
        s1 : value
    }
    return name[s1]
def 상추_게임():
    inven = []
    lettuce_game()
상추_게임()