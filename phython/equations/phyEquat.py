import math

def calcAcc(projectile, enviroment):
    if env.isFrFall:
        proj1.acc = env.grav
    else:
        proj1.acc = proj1.force / proj1.mass

def calcKE(arg):
    pass

def calcPE(arg):
    pass

def calcBounceHt(arg):
    bounceHt = proj1.pos * env.restCoef

def calcDrop(arg):
    pass

def calcTimeOfImpact(arg):
    timeOfImpact = math.sqrt((2*proj1.pos)/proj1.acc)
