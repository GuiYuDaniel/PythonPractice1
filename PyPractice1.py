'''矩阵的转置，相乘，求逆'''
# _*_ coding:utf-8 _*_


import sys,copy,csv


# 类0...工具
class Tool:

    def getfirstone(self,matrix,m):# 寻找matrix矩阵第m列中，包括m行以下第一个非零行，没有则返回-1
        L=len(matrix)
        for i in range(m,L):
            if matrix[i][m]!=0:
                return i
        return -1

    def eyes(self,m):# m*m维1
        a=[[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            a[i][i]=1
        return a

    def hangchangeone(self,matrix,b,m):# 用matrix第m行m列为主元，造第m列的上三角
        _c=matrix[m][m]
        L=len(matrix)
        matrix[m][m]=1
        for i in range(L):
            b[m][i]=b[m][i]/_c
        for i in range(m+1,L):
            matrix[m][i]=matrix[m][i]/_c# m行随主元变

        for i in range(m+1,L):# m行以下所有按照m减一次
            _d=matrix[i][m]
            for j in range(L):
                matrix[i][j]=matrix[i][j]-matrix[m][j]*_d
                b[i][j]=b[i][j]-b[m][j]*_d

        return matrix,b

    def hangchangetwo(self,matrix,b,L):# 把上三角对角化
        if L is 1:
            return matrix,b
        else:
            for i in range(L-1,0,-1):
                for j in range(i-1,-1,-1):
                    for k in range(L):
                        b[j][k]=b[j][k]-b[i][k]*matrix[j][i]
                    matrix[j][i]=0
            return matrix,b

    def matrixtestone(self,matrix):# 矩阵检查1
        if type(matrix) is not list:
            print(str(matrix)+'根本就不是矩阵！请确认是否输入正确')
            sys.exit(0)
        if matrix == []:
            print(str(matrix) + '根本就不是矩阵！请确认是否输入正确')
            sys.exit(0)
        for i in matrix:
            if type(i) is not list:
                print(str(matrix)+'根本就不是矩阵！请确认是否输入正确')
                sys.exit(0)
            if i == []:
                print(str(matrix) + '根本就不是矩阵！请确认是否输入正确')
                sys.exit(0)
            for j in i:
                if type(j) is float:
                    pass
                elif type(j) is int:
                    pass
                else:
                    print(str(matrix)+'根本就不是矩阵！请确认是否输入正确')
                    sys.exit(0)

    def matrixtesttwo(self,matrix):# 矩阵检查2，每行等长
        _L=len(matrix[0])
        for i in matrix:
            if len(i)!=_L:
                print('矩阵每行元素个数要相等，请检查行'+str(i)+'与第一行不匹配')
                sys.exit(0)


# 类1...纠错
class Test:

    def transposition(self,matrix):# m*n矩阵检查
        Tool.matrixtestone(Tool,matrix)
        Tool.matrixtesttwo(Tool,matrix)

    def inverse(self,matrix):# n*n矩阵检查
        Tool.matrixtestone(Tool, matrix)
        Tool.matrixtesttwo(Tool, matrix)
        if len(matrix)!=len(matrix[0]):
            print('只有方阵才可能求逆,请调整'+str(matrix))
            sys.exit(0)

    def accumulate(self,a,b):
        Tool.matrixtestone(Tool, a)
        Tool.matrixtestone(Tool, b)
        Tool.matrixtesttwo(Tool, a)
        Tool.matrixtesttwo(Tool, b)
        if len(a[0])!=len(b):
            print('左边矩阵的列数要和右边矩阵的行数相等才能相乘，请调整左边'+str(a)+'或者右边'+str(b))
            sys.exit(0)


# 类2...执行
class Cal:

    def transposition(self,matrix):
        _m=len(matrix)
        _n=len(matrix[0])
        result=[[0 for i in range(_m)] for j in range(_n)]
        for i in range(_m):
            for j in range(_n):
                result[j][i]=matrix[i][j]
        return result

    def inverse(self,matrix):# 初等行变换法
        matrixnew=copy.deepcopy(matrix)
        _m=len(matrix)
        result=Tool.eyes(Tool,_m)
        for i in range(_m):
            hang=Tool.getfirstone(Tool,matrixnew,i)
            if hang is -1:
                print('抱歉，这个矩阵'+str(matrix)+'行列式为零，没有逆')
                sys.exit(0)
            elif hang is not i:
                matrixnew[i]=[matrixnew[i][j]+matrixnew[hang][j] for j in range(_m)]
                result[i]=[result[i][j]+result[hang][j] for j in range(_m)]
            _c=matrixnew[i][i]
            matrixnew,result=Tool.hangchangeone(Tool,matrixnew,result,i)# 上三角化
        matrixnew,result=Tool.hangchangetwo(Tool,matrixnew,result,_m)# 对角化
        return result

    def accumulate(self,a,b):
        _m=len(a)
        _n=len(a[0])
        _k=len(b[0])
        result=[[0 for i in range(_k)] for j in range(_m)]
        for m in range(_m):
            for k in range(_k):
                d=0
                for n in range(_n):
                    c=a[m][n]*b[n][k]
                    d+=c
                result[m][k]=d
        return result


# 用户输入部分...
dowhat='相乘'# 可选'转置'，'相乘'，'求逆'
matrixa=[[1,2],[3,4]]# 被'转置'，'求逆'的矩阵。或者'相乘'左边的矩阵
matrixb=[[-2,1],[1.5,-0.5]]# '相乘'右边的矩阵
csvpath='C:\\'# 保存路径（可选）
filename='myresult'# 文件名（可选）


# 主函数...
def main():
    print('欢迎来到求转置，逆，相乘的程序')
    if dowhat=='转置':
        Test.transposition(Test,matrixa)
        result=Cal.transposition(Cal,matrixa)
        print('矩阵'+str(matrixa)+'的转置结果是'+str(result))
    elif dowhat=='求逆':
        Test.inverse(Test,matrixa)
        result=Cal.inverse(Cal,matrixa)
        print('矩阵'+str(matrixa)+'的求逆结果是'+str(result))
    elif dowhat=='相乘':
        Test.accumulate(Test,matrixa,matrixb)
        result=Cal.accumulate(Cal,matrixa,matrixb)
        print('矩阵'+str(matrixa)+'和矩阵'+str(matrixb)+'的乘积结果是'+str(result))
    else:
        print('请在dowhat中输入转置，相乘，或者求逆')
        sys.exit(0)

    # 将结果保存为csv文件（可选），需提供路径
    #with open(csvpath+filename+'.csv','wb') as myfile:
    #    csvfile=csv.writer(myfile)
    #    csvfile.writerows(result)


# 运行
if __name__ == '__main__':
    main()



