class TicTacToeBoard:
    def get_field(self):
        return self.field
    
    def __init__(self):
        self.count = 0
        self.field = [['-', '-', '-'], 
                ['-', '-', '-'],
                ['-', '-', '-']]
        
    
    def make_move(self, row, col):
        if self.field[row-1] [col-1] != ('X' or '0'):
            self.count+=1
            if self.count %2 ==0: #это игрок 2
                self.field[row-1][col - 1] = '0'
            else: #Игрок 1
                self.field[row-1][col-1] = 'X'
        else:
            print('Ячейка занята')
            
    def Check_field(self):
        if self.field[0][0] == self.field[0] [1] == self.field[0][2] != '-':
            if self.field[0][0] =='X':
                print('Победитель - игрок 1')
                return 'X'
            elif self.field[0][0] =='0':
                print('Победитель игрок 2')
                return '0'
        #Проверка по грозинотали 
        for f in range(3):
            if self.field[0][f] == self.field[1][f] == self.field[2][f]!='-':
                if self.field[0][f] =='X':
                    print('Победитель игрок 1')
                    return 'X'
                if self.field[0][f] == '0':
                    print('Победитель игрок 2')
                    return '0'
        #Проверка по диагоналям 
        if self.field[0][0] == self.field[1][1] == self.field[2][2]!='-':
            if self.field[0][0] == 'X':
                print('Победитель - игрок 1')
                return 'X'
            else:
                print('Победитель - игрок 2')
                return '0'
        if self.field[0][2] == self.field[1][1] == self.field[2][0] != '-':
            if self.field[0][2] =='X':
                print('Победитель - игрок 1')
                return 'X'
            else:
                print('Победитель  - игрок 2')
                return '0'
        elif '-' not in self.p[0] and \
                '-' not in self.p[1] and \
                '-' not in self.p[2]:
                print('Ничья')

board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1)) 
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
print(board.Check_field())