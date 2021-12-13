import math
import pandas as panda
import numpy as np

class Objective:
    def __init__(self):
        pass

    def Rosenbrock2D(self, x):
        x1 = x[0]
        x2 = x[1]
        temp1 = math.pow(math.pow(x1, 2) - x2, 2)
        temp2 = math.pow(x1-1, 2)
        return 100*temp1-temp2

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