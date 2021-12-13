from particlefile import Particle
from objectivefile import Objective
import matplotlib.pyplot as plt

class PSO:
    nSwarm = 0
    swarm = None
    obj = Objective()
    fit = []
    gbest = 0
    __maximini = 'min'
    __maxloop = 0
    bound = None
    nDim = 0
    w = 0
    function_name = None

    def __init__(self, nPop, nDim, inersia, maximini, maxloop, Function=None, bound=None):
        self.function_name = Function
        self.w = inersia
        self.nDim = nDim
        self.bound = bound
        self.__maximini = maximini
        self.__maxloop = maxloop
        self.nSwarm = nPop
        #########################
        self.initprocess()
        #########################
        self.mainloop()

    def initprocess(self):
        self.initPosition()
        self.calculateFitness()
        self.initPbestFitness()
        self.findGbest()
        self.calVelocity()
        self.updatePositionSwarm()

    def mainloop(self):
        gvalue = []
        for i in range(self.__maxloop):
            self.calculateFitness()
            self.updatePbest()
            self.findGbest()
            self.calVelocity()
            self.updatePositionSwarm()
            gvalue.append(self.swarm[self.gbest].pbestFitness)
        plt.plot(gvalue)
        plt.show()
        print("BEST VALUE :", gvalue[self.__maxloop-1])
        print("BEST Vaariable:", self.swarm[self.gbest].pbestPosition)

    def getVariableOptimal(self):
        return self.swarm[self.gbest].pbestPosition

    def initPosition(self):
        swarm = []
        for i in range(self.nSwarm):
            swarm.append(Particle(self.nDim, bound=self.bound))
        self.swarm = swarm

    def viewPosition(self):
        for i in range(self.nSwarm):
            print("no :", i, ": ",
                  self.swarm[i].position)

    def viewFitness(self):
        for i in range(self.nSwarm):
            print("fitness :", i+1, ": ",
                  self.swarm[i].fitness)

    def calculateFitness(self):
        if self.function_name == 'Rosenbrock':
            for i in range(self.nSwarm):
                fit = (self.obj.Rosenbrock2D(
                    self.swarm[i].position))
                self.swarm[i].fitness = fit
        elif self.function_name == 'koefesienDiesel':
            for i in range(self.nSwarm):
                fit = (self.obj.koefesienDiesel(
                    self.swarm[i].position))
                self.swarm[i].fitness = fit
        elif self.function_name == 'Sphere':
            for i in range(self.nSwarm):
                fit = (self.obj.Sphere(
                    self.swarm[i].position))
                self.swarm[i].fitness = fit
        elif self.function_name == 'SchwefelF7':
            for i in range(self.nSwarm):
                fit = (self.obj.SchwefelF7(
                    self.swarm[i].position))
                self.swarm[i].fitness = fit
        elif self.function_name == 'Step':
            for i in range(self.nSwarm):
                fit = (self.obj.Step(
                    self.swarm[i].position))
                self.swarm[i].fitness = fit
        elif self.function_name == 'Rastrigin':
            for i in range(self.nSwarm):
                fit = (self.obj.Rastrigin(
                    self.swarm[i].position))
                self.swarm[i].fitness = fit
        elif self.function_name == 'Ackley':
            for i in range(self.nSwarm):
                fit = (self.obj.Ackley(
                    self.swarm[i].position))
                self.swarm[i].fitness = fit

    def initPbestFitness(self):
        for i in range(self.nSwarm):
            self.swarm[i].initPbestFitness(
                self.swarm[i].fitness)

    def viewVelocity(self):
        for i in range(self.nSwarm):
            print("velo-",i+1,"=", self.swarm[i].velocity)

    def viewPbestFitness(self):
        for i in range(self.nSwarm):
            print("pbestF-",i+1,"=", self.swarm[i].pbestFitness)

    def viewPbestPositiion(self):
        for i in range(self.nSwarm):
            print("pbestP-",i+1,"=", self.swarm[i].pbestPosition)

    def __findGbestMax(self):
        max = self.swarm[0].fitness
        index = 0
        for i in range(self.nSwarm):
            if max < self.swarm[i].pbestFitness:
                max = self.swarm[i].pbestFitness
                index = i
        return index

    def __findGbestMin(self):
        mini = self.swarm[0].fitness
        index = 0
        for i in range(self.nSwarm):
            if mini > self.swarm[i].pbestFitness:
                mini = self.swarm[i].pbestFitness
                index = i
        return index

    def findGbest(self):
        if self.__maximini == 'max':
            self.gbest = self.__findGbestMax()
        else:
            self.gbest = self.__findGbestMin()

    def calVelocity(self):
        gbest = self.swarm[self.__findGbestMin()].pbestPosition
        for i in range(self.nSwarm):
            velo = self.swarm[i].calculateVelocity(
                gbest, self.w)
            self.swarm[i].velocity = velo

    def updatePositionSwarm(self):
        for i in range(self.nSwarm):
            self.swarm[i].updatePosition()

    def updatePbest(self):
        for i in range(self.nSwarm):
            self.swarm[i].updatePbest(self.__maximini)