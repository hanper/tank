import sys

class Cradle(object):
    def __init__(self):
        self.look = NULL

    def getChar(self):
        self.look = input()

    def error(msg):
        print("\n Error:", msg)

    def abort(msg):
        self.error(msg)
        sys.quit()
