'''
Multiplicar dos matrices
'''

def mult_mat(matone:list,mattwo:list)->list:
    size_one = len(matone)
    sizetwo = len(mattwo)
    sizethree = len(list(mattwo[0]))
    new_mat = []
    sum = 0
    for i in range(0,size_one):
        for j in range(0,sizethree):
            for k in range(0,sizetwo):
                sum += matone[i][k] * mattwo[k][j]
            new_mat.append(sum)
            sum = 0
        
    return new_mat
                     
def run():
    m1 = [
        [1,2,3],
        [4,5,6]
    ]
    m2 = [
        [-1,0],
        [0,1],
        [1,1]
    ]

    result = mult_mat(matone=m1,mattwo=m2)
    print(f'{result=}')

if __name__=='__main__':
    run()