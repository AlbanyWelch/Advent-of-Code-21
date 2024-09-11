import re

class BingoBoard:
    def __init__(self, nums):
        self.board = [[[nums[x][y],False] for x in range(5)] for y in range(5)]

    def markNumber(self, num):
        for r in range(5):
            for c in range(5):
                if self.board[r][c][0] == num:
                    self.board[r][c][1] = True

    def checkBingo(self):
        for r in range(5):
            if all(self.board[r][i][1] for i in range(5)):
                return True
        for c in range(5):
            if all(self.board[i][c][1] for i in range(5)):
                return True
        return False
    
    def score(self,numCall):
        total = 0
        for r in range(5):
            for c in range(5):
                if not(self.board[r][c][1]):
                    total += self.board[r][c][0]
        return total*numCall


def initialiseBoards():
    with open("Day 4/data4.txt",'r') as file:
        data = file.read().strip().split("\n")
    nums = [int(i) for i in data[0].split(",")]

    boards = []
    l = 2
    while l < len(data):
        lines = data[l:l+5]
        x = [[int(i) for i in re.split(" +", line.strip())] for line in lines]
        boards.append(BingoBoard(x))
        l += 6

    return nums, boards

# first board to win and its score
def dayFour_P1(boards, numbers):
    score = -1
    for n in numbers:
        for b in boards:
            b.markNumber(n)
        for b in boards:
            if b.checkBingo():
                score = b.score(n)
                break
        if score != -1:
            break
    
    print(score)

# last board to win and its score
def dayFour_P2(boards, numbers):
    winners = []
    temp_boards = []
    for n in numbers:
        for b in boards:
            b.markNumber(n)
        for b in boards:
            if b.checkBingo():
                winners.append(b.score(n))
                temp_boards.append(b)
                boards.remove(b)

    print(winners[len(winners)-1])
    boards = temp_b.copy() # reset boards list

def main():
    nums, boards = initialiseBoards()
    dayFour_P1(boards, nums)
    dayFour_P2(boards, nums)

main()