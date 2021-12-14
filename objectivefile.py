import math
import pandas as panda
import numpy as np

class Objective:
    def __init__(self):
        pass

    def Step(self, x):
        print('step')
        tot = 0
        for i in range (len(x)):
            tot = tot + math.pow((x[i]+0.5),2)
        return tot

    def Rosenbrock2D(self, x):
        x1 = x[0]
        x2 = x[1]
        temp1 = math.pow(math.pow(x1, 2) - x2, 2)
        temp2 = math.pow(x1-1, 2)
        return 100*temp1-temp2

    def Sphere(self, x):
        n = len(x)
        tot = 0
        for i in range(n):
            tot = tot + math.pow(x[i],2)
        return tot

    def SchwefelF7(self, x):
        chromosome = x
        alpha = 418.982887
        fitness = 0
        for i in range(len(chromosome)):
            fitness = fitness-chromosome[i] * math.sin(math.sqrt(math.fabs(chromosome[i])))
        return float(fitness) + alpha * len(chromosome)

    def Rastrigin(self, x):
        tot = 0
        for i in range(len(x)):
            tot += math.pow(x[i],2)-10*math.cos(2*math.pi*x[i])+10
        return tot

    def Ackley(self, x):
        n = len(x)
        res1 = 0
        res2 = 0
        for i in range(n):
            res1 += math.pow(x[i],2)
            res2 += math.cos(2*math.pi*x[i])
        res1 = res1 / n
        res2 = res2 / n
        return -20*math.exp(-20*res1-math.exp(res2))+20+math.e


    def koefesienDiesel(self, x):
        # load dataset from dataset_mesin
        file = panda.read_excel(open('dataset_mesin.xlsx', 'rb'))
        df = panda.DataFrame(
            file,columns=(['Pinj','Dimp','Dhole','Q']))
        dataset = np.array(df.values.tolist())  #array numpy dataset

        # initialization variable
        n = dataset.shape[0]
        x1 = x[1]
        x2 = x[2]
        x3 = x[3]
        x0 = x[0]

        # data modeling
        # Q = C.Pinj^a.Dimp^b.Dhole^c

        #calculate result from optimization algorithm
        result = []
        for i in range(n):
            cal1 = dataset[i][0]**x1
            cal2 = dataset[i][1]**x2
            cal3 = dataset[i][2]**x3
            result.append(x0*cal1*cal2*cal3)

        #calculate error (objective function)
        error = []
        for i in range(n):
            error.append(abs(result[i]-dataset[i][3]))
        return (sum(error))

    def koefesienDiesel2(self, x):
        # load dataset from dataset_mesin
        file = panda.read_excel(open('dataset_mesin.xlsx', 'rb'))
        df = panda.DataFrame(
            file, columns=(['Pinj', 'Dimp', 'Dhole', 'Q']))
        dataset = np.array(df.values.tolist())  # array numpy dataset

        # initialization variable
        n = dataset.shape[0]
        x1 = x[1]
        x2 = x[2]
        x3 = x[3]
        x0 = x[0]

        # data modeling
        # Q = C.Pinj^a.Dimp^b.Dhole^c

        # calculate result from optimization algorithm
        result = []
        for i in range(n):
            cal1 = x0
            cal2 = x1*math.log(dataset[i][1])
            cal3 = x2*math.log(dataset[i][2])
            cal4 = x3*math.log(dataset[i][3])
            cal5 = cal1 + cal2 + cal3 + cal4
            result.append(math.exp(cal5))

        # calculate error (objective function)
        error = []
        for i in range(n):
            error.append(abs(result[i] - dataset[i][3]))
        return (sum(error))