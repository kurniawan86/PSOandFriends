import random
import numpy as np

class Particle:
    position = []
    fitness = 0
    pbestPosition = []
    pbestFitness = 0
    velocity = 0
    ndim = None
    bound = None

    def __init__(self, ndim, bound=None):
        self.ndim = ndim
        self.bound = bound
        self.__initPosition()
        self.__initPbestPos()

    def __initPositionNoBound(self):
        gen = []
        for i in range(self.ndim):
            gen.append(random.random())
        return gen

    def __initPositionBound(self):
        gen = []
        mini = self.bound[0]
        maxi = self.bound[1]
        for i in range(self.ndim):
            ind = random.randint(mini, maxi-1)
            gen.append(ind)
        return gen

    def __initPosition(self):
        if self.bound==None:
            self.position = self.__initPositionNoBound()
        else:
            self.position = self.__initPositionBound()

    def __initPbestPos(self):
        pbestpos = 0
        pbestpos = self.position
        self.pbestPosition = pbestpos

    def initPbestFitness(self, fit):
        self.pbestFitness = fit

    def calculateVelocity(self, gbest, w):
        X = np.array(self.position)
        pbest = np.array(self.pbestPosition)
        gbest = np.array(gbest)
        velo1 = random.random()*(pbest-X)
        velo2 = random.random()*(gbest-X)
        result = w * self.velocity+velo1+velo2
        return result

    def updatePosition(self):
        position = self.position+self.velocity
        self.position = position

    def updatePbest(self, maximini):
        if maximini == 'min':
            self.__updatePbestMini()
        else:
            self.__updatePbestMax()

    def __updatePbestMax(self):
        if self.fitness > self.pbestFitness:
            self.pbestFitness = self.fitness
            self.pbestPosition = self.position

    def __updatePbestMini(self):
        if self.fitness < self.pbestFitness:
            self.pbestFitness = self.fitness
            self.pbestPosition = self.position