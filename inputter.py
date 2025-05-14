class InputParser(object):
    def __init__(self, break_point="Y"):
        self._break_point = break_point

    def run(self):
        i = input("Enter the magic key: ")
        if i == self._break_point:
            print("YOU guessed the magic key")
            return None
        else:
            return self.run()

if __name__ == "__main__":
    inputter = InputParser(break_point="broccoli")
    inputter.run()
