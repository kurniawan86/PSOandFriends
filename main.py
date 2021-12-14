from objectivefile import Objective
from psofile import PSO
import pandas as panda
import numpy as np
import math

def testing(x):
    # load dataset from dataset_mesin
    file = panda.read_excel(open('dataset_mesin.xlsx', 'rb'))
    df = panda.DataFrame(
        file, columns=(['Pinj', 'Dimp', 'Dhole', 'Q']))
    dataset = np.array(df.values.tolist())  # array numpy dataset

    x1 = x[1]
    x2 = x[2]
    x3 = x[3]
    x0 = x[0]
    n = len(x)
    result = []
    for i in range(12):
        cal1 = x0
        cal2 = x1 * math.log(dataset[i][1])
        cal3 = x2 * math.log(dataset[i][2])
        cal4 = x3 * math.log(dataset[i][3])
        cal5 = cal1 + cal2 + cal3 + cal4
        result.append(math.exp(cal5))
    print(result)

# ini digunakan untuk running mesin deisel
#
if __name__ == '__main__':
    nPopulasi = 50
    nDim = 4
    inersia = 1
    maximini = 'min'
    maxloop = 100

    #function:
    # Rosenbrock : 2 Dimensi
    # Sphere : multi dimensi [-100,100]
    # SchwefelF7 : Multi-Dimensi [-500 500]
    # Step : multi Dimensi [-100, 100]
    # Rastrigin : mulitt dimensi[-5.12, 512]
    # Ackley : multi Dimensi [-32,32]

    # pso = PSO(nPopulasi, nDim, inersia, maximini, maxloop, Function='koefesienDiesel')
    # koefesien = pso.getVariableOptimal()
    #testing(koefesien)
    # x = [1,2,3,4]
    # obj = Objective()
    # obj.koefesienDiesel(x)

    testing([0.81721987,-0.00492383,0.66610404,1.16125217])