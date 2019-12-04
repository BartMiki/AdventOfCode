import numpy as np


def task_1(code):
    task1_code = np.copy(code)
    task1_code[1] = 12
    task1_code[2] = 2

    computer = IntComputer(task1_code)
    result = computer.interpret()
    print("Task #1 result:", result[0])

def task_2(code):
    for noun in range(100):
        for verb in range(100):
            copy = code.copy()
            copy[1] = noun
            copy[2] = verb
            response = IntComputer(copy).interpret()[0]
            if response == 19690720:
                print("Task #2 result:", 100 * noun + verb)
                return

def main():
    code = np.loadtxt("data/day_02.txt", delimiter=",", dtype="int32")
    task_1(code)
    task_2(code)
    

class IntComputer:
    def __init__(self, code):
        self._code = np.copy(code)
        self._pointer = 0 
        self._operations = {
            1: self._add,
            2: self._mul
        }
    
    def interpret(self):
        while not self.is_done():
            opcode = self._code[self._pointer]
            self._operations[opcode]()
            
        return self._code.copy()

    def is_done(self):
        return self._code[self._pointer] == 99

    def _binary_function(self, function):
        ix1 = self._code[self._pointer + 1]
        ix2 =  self._code[self._pointer + 2]
        iy = self._code[self._pointer + 3]

        self._code[iy] = function(self._code[ix1], self._code[ix2])
        self._pointer += 4

    def _add(self):
        self._binary_function(lambda x1, x2: x1 + x2)

    def _mul(self):
        self._binary_function(lambda x1, x2: x1 * x2)

    def _opcode(self):
        return self._code[self._pointer]

if __name__ == "__main__":
    main()
