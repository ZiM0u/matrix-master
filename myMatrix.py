class Matrix:
    def __init__(self):
        self.data = [[0,0,0],
                     [0,0,0],
                     [0,0,0]]

         
    def __len__(self):
        return len(self.data)*len(self.data[0])

    def __getitem__(self,pos):
        return self.data[pos[0]][pos[1]]

    def __setitem__(self,pos,value):
        self.data[pos[0]][pos[1]]= value
        return value

    def __str__(self):
        return str(self.data)

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
