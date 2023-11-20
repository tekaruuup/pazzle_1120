import itertools
from fractions import Fraction
import copy

def left_solve(x,y,sisoku,a):
    # 数字の並び替え
    for pazzle in itertools.permutations(x,len(x)):
        pazzle = list(pazzle)

        # 記号の並び替え
        for sisoku_k in itertools.product(sisoku,repeat=a):
            pazzle_r = copy.deepcopy(pazzle)
            while True:
                if len(pazzle_r) >= 2:
                    sisoku_list = []
                    for i in sisoku_k:

                        # 割り算特別処理
                        if i == '/':
                            if pazzle_r[1] ==0:
                                pazzle_r.clear()
                                break
                            elif type(pazzle_r[0]/pazzle_r[1]) == int:
                                pazzle1 = pazzle_r[0]/pazzle_r[1]
                            elif type(pazzle_r[0]/pazzle_r[1]) == float:
                                pazzle1 = Fraction(int(pazzle_r[0]),int(pazzle_r[1]))
                            elif pazzle_r[0].denominator != 1 or pazzle_r[1].denominator != 1:
                                pazzle_r.clear()
                                break
                        else:
                            pazzle1 = eval(f'{pazzle_r[0]} {i} {pazzle_r[1]}')
                        for delete in [1,0]:
                            pazzle_r.pop(delete)
                        pazzle_r.insert(0,pazzle1)
                        sisoku_list.append(i)
                        
                else:
                    break            
            # 正誤判定
            if pazzle1 == y:
                nn = 1
                for n,s in enumerate(sisoku_list):
                    pazzle = [str(x) for x in pazzle]
                    pazzle.insert(n + nn,s)
                    nn += 1
                pazzle_answ = ','.join(pazzle).replace(',','')
                break
            else:
                pazzle_answ = ''
                continue
        if pazzle1 ==y:
            break
        else:
            continue
    return pazzle_answ