class ttt():
    # inp = input("7 | 8 | 9\n--+---+--\n4 | 5 | 6\n--+---+--\n1 | 2 | 3 \n")
    board = []
    b = {1:6, 2:7, 3:8, 4:3, 5:4, 6:5, 7:0, 8:1, 9:2}
    def __init__(self):
        # self.board = ['_' for x in range(9)]
        self.board = [' ' for x in range(9)]

    def check_win(self, mark):
        if {self.board[0], self.board[1], self.board[2]} == {mark} or {self.board[3], self.board[4], self.board[5]} == {mark} or {self.board[6], self.board[7], self.board[8]} == {mark} or {self.board[0], self.board[3], self.board[6]} == {mark} or {self.board[1], self.board[4], self.board[7]} == {mark} or {self.board[2], self.board[5], self.board[8]} == {mark} or {self.board[0], self.board[4], self.board[8]} == {mark} or {self.board[2], self.board[4], self.board[6]} == {mark}:
            return 1
        elif " " not in self.board:
            return 2
        else:
            return 0

    def update_board(self, inp, mark):
        print(mark)
        try:
            pos = self.b[int(inp)]
        except:
            print("error parsing input")
            return -1
        if self.board[pos] != " ": return -1
        # if self.board[pos] != "_": return -1
        print
        if mark == "ttt1":
            mark = "X"
        if mark == "ttt2":
            mark = "O"
        self.board[pos] = mark
        return self.check_win(mark)
        
