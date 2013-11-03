import sys

class Navigator(object):
    def __init__(self, board):
        self.board = board

    def navigate(self):
        pass

data = sys.stdin.readlines()
for line in data:
    print line
