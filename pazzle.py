import pattern_1
import pattern_2
import pattern_3


def quizu(x, y):
    a = len(x)-1
    sisoku = ['+','-','*','/']
    flg = 0

    pazzle_answ = pattern_1.left_solve(x, y, sisoku,a)
    
    # 左から解けなかったものをこれで解く
    if pazzle_answ == '':
        pazzle_answ =  pattern_2.merge_solve(x,y,sisoku,a)
        flg =+ 1
    
    if flg == 0:
        pazzle_answ = 'パターン1:', pazzle_answ
    else:
        pazzle_answ = 'パターン2:', pazzle_answ
    return pazzle_answ

    
x = [int(i) for i in input().split(' ')]
y = int(x[-1])
x = x[:-1]
answer = quizu(x,y)
print(answer)