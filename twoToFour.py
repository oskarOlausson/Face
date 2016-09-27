
from math import exp

class Solver():

    def __init__(self):
        #self.test = testList()
        _=0


    def ai(self,test,learningRate):
        w1 = 0.5
        w2 = 0.5
        w3 = 0.5
        w4 = 0.5

        for i in range(0,5000):
            number = 0

            in1 = test[number+0]
            in2 = test[number+1]
            net1 = in1 * w1 + in2 * w2
            net2 = in1 * w3 + in2 * w4

            out1 = 1 / (1 + exp(-net1))
            out2 = 1 / (1 + exp(-net2))

            facit = test[number+2]

            w1_to_out1 = (out1 - facit) * out1 * (1 - out1) * in1
            w1 = w1-(w1_to_out1*learningRate)
            print("w1 ",w1)

            w2_to_out1 = (out1 - facit) * out1 * (1 - out1) * in2
            w2 = w2 - (w2_to_out1 * learningRate)
            print("w2 ", w2)

            w3_to_out2 = (out2 - facit) * out2 * (1 - out2) * in1
            w3 = w3 - (w3_to_out2 * learningRate)
            print("w3 ", w3)

            w4_to_out2 = (out2 - facit) * out2 * (1 - out2) * in2
            w4 = w4 - (w4_to_out2 * learningRate)
            print("w4 ", w4)

            if out1>out2:
                weSay = True
                print("bigger")
            else:
                weSay = False
                print("smaller")

            correct = (weSay == facit)

            print(correct)
            print()



if __name__ == "__main__":
    solver = Solver()

    # 3>2 --> True
    test = [3,2,1]

    solver.ai(test,3)






def testList():
    test = list()
    #0 to 3!
    for first in range(0, 4):
        for second in range(0, 4):
            if first>=second: test.append((first,second,True))
            else: test.append((first,second,False))
