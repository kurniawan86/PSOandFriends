from objectivefile import Objective
from psofile import PSO
import pandas as panda
import numpy as np

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
    result = []
    for i in range(12):
        cal1 = dataset[i][0] ** x1
        cal2 = dataset[i][1] ** x2
        cal3 = dataset[i][2] ** x3
        result.append(x0 * cal1 * cal2 * cal3)
    print(result)


# ini digunakan untuk running mesin deisel
#
if __name__ == '__main__':
    nPopulasi = 5
    nDim = 4
    inersia = 1
    maximini = 'min'
    maxloop = 5
    pso = PSO(nPopulasi, nDim, inersia, maximini, maxloop, Function='koefesienDiesel')
    koefesien = pso.getVariableOptimal()
    testing(koefesien)
    # x = [1,2,3,4]
    # obj = Objective()
    # obj.koefesienDiesel(x)