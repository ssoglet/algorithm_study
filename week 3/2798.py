import itertools
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card_num = list(map(int, input().split()))

combi_list = [sum(combi) for combi in itertools.combinations(card_num, 3) if sum(combi) <= m]
print(max(combi_list))