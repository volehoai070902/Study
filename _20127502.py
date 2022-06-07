#Doc File
def ReadFile (Data):
    filein = open('input.txt', 'r')
    for lines in filein.readlines():
        a = []
        lines.strip()
        lines = lines.split()
        for l in lines:
            a.append(float(l))
        Data.append(a)
    filein.close()
#
def Create_inverse_matrix (inverse_matrix, m, n):
    for i in range (m):
        a = []
        for j in range (n):
            if ( i == j):
                a.append(1)
            else:
                a.append(0)
        inverse_matrix.append(a)
def Gauss_jordan (Data, inverse_matrix, m, n):
    if (m != n):
        return
    row = 0
    column = 0
    
    while row != m and column != n:
        if ( Data[row][column] == 0):
            for i in range (row + 1, m):
                if Data[i][column] != 0:
                    temp = Data[row]
                    Data[row] = Data[i]
                    Data[i] = temp
                    
                    temp = inverse_matrix[row]
                    inverse_matrix[row] = inverse_matrix[i]
                    inverse_matrix[i] = temp
                    
                    break

        if ( Data[row][column] != 1):
            temp = Data[row][column]
            if temp != 0:
                for j in range (column, n):
                    if (Data[row][j] != 0):
                        Data[row][j] = Data[row][j] / temp
                for j in range (n):
                    inverse_matrix[row][j] = inverse_matrix[row][j]/ temp
        
        for i in range (row + 1,m):
            temp = Data[i][column]
            for j in range (column, n):
                Data[i][j] = Data[i][j]*Data[row][column] - Data[row][j]*temp
            for k in range (n):
                inverse_matrix[i][k] = inverse_matrix[i][k]*Data[row][column]-inverse_matrix[row][k]*temp
                if Data[i][j] == -0.0:
                    Data[i][j] = 0.0
        print (Data)
        row += 1
        column+=1

    if Data[m-1][n-1] == 0:
        print ("Ma tran khong co nghich dao")
        return

    row = m - 1
    column = n - 1
    while row != 0:
        for i in range (row):
            temp = Data[i][column]
            if (temp != 0):
                Data[i][column] = Data[i][column]*Data[row][column] - Data[row][column]*temp
                for j in range (n):
                    inverse_matrix[i][j] = inverse_matrix[i][j]-inverse_matrix[row][j]*temp
        row-= 1
        column -= 1
    print(inverse_matrix)


Data = []
inverse_matrix = []
ReadFile(Data)
row = len(Data)
column = len(Data[0])


Create_inverse_matrix(inverse_matrix, row, column)
Gauss_jordan(Data, inverse_matrix, row, column)