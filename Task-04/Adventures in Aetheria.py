'''Clem adores the mystical land of the Entrati. Among all the wondrous towns there, Clem has a special fondness for the magical town of Aetheria
However, Aetheria is rumored to be facing some magical disturbances, making it perilous for Clem to settle there. Thus, Clem sets out on a journey to find another town to call home. Clem values efficiency and wishes to minimize travel time during his quest. Consequently, he will choose the town that requires the least time to reach. If there are multiple towns with the same minimum travel time, Clem will stay in Aetheria, where his heart lies.
You are aware of the time needed to travel to each town, except for Aetheria. Your mission is to determine the town where Clem will journey or whether he will decide to stay in his beloved town of Aetheria.
'''
n = int(input())
dist = list(map(int, input().split()))
min_dist = min(dist)

if dist.count(min_dist) > 1:
    print("Still Aetheria")
else:
    Clems_choices = [i for i, d in enumerate(dist) if d == min_dist][0] + 1
    print(Clems_choices)
