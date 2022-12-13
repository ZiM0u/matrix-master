class Matrix:
    def __init__(self, row=3,collumn=3):
        self.data=[]
        for line in range(collumn):
            row_list= []
            for line in range(row):
                row_list.append(0)
            self.data.append(row_list)
            
        #self.data = [[0,0,0],
                    # [0,0,0],
                   #  [0,0,0]]

         
    def __len__(self):
        return len(self.data)*len(self.data[0])

    def __getitem__(self,pos):
        return self.data[pos[0]][pos[1]]

    def __setitem__(self,pos,value):
        self.data[pos[0]][pos[1]]= value
        return value

    def __str__(self):
        result =""
        for row in self.data:
            result+=str(row)+"\n"
        return result
            

    def __add__(self,operand):
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                self.data[y][x] += (operand[y,x])
        return self

    def __sub__(self,operand):
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                self.data[y][x] -= (operand[y,x])
        return self

    def __mul__(self,operand):
        if type(operand)==int:
            for i in range(len(self.data)):
                for l in range(len(self.data[0])):
                    print(i)
                    print(l)
                    self.data[i][l]*=operand
        return self.data
    

    def transpose(self):
        tmp = Matrix(len(self.data),len(self.data[0]))
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                tmp[x,y]=self.data[y][x]
        return tmp
                    
