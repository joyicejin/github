
import copy
class Matrix:
    def __init__(self, row, column, fill=0.0):
        self.shape = (row, column)  #5
        self.row = row #5
        self.column = column #5
        self._matrix = [[fill] * column for i in range(row)]

        # 返回元素m(i, j)的值:  m[i, j]
    def __getitem__(self, index):
        if isinstance(index, int):
            return self._matrix[index]
        elif isinstance(index, tuple):
            return self._matrix[index[0]][index[1]]
            # 设置元素m(i,j)的值为s:  m[i, j] = s

    def __setitem__(self, index, value):
        if isinstance(index, int):
           self._matrix[index ] = copy.deepcopy(value)
        elif isinstance(index, tuple):
            c= int(value)
            a=int(index[0])
            b=int(index[1])
            self._matrix[a][b] = c


if __name__ == '__main__':
    matShape=input().split()
    n=int(matShape[0])
    m=int(matShape[1])
    M = Matrix(n, n, fill=0)
    for i in range(m):
        print(i)
        operShape=input().split()
        length=len(operShape)
        operType=operShape[0]
        if(operType=='Add'):
            assert length==4
            M.__setitem__((operShape[1],operShape[2]),operShape[3])
        elif(operType=="Sum"):
            assert length==5
            x1= int(operShape[1])
            y1 = int(operShape[2])
            x2 = int(operShape[3])
            y2 = int(operShape[4])
            sum = 0
            for j in range(x2-x1+1):
               sum+=M.__getitem__((x1+j,y1+j))
            print(sum)

