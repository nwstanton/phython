import math

def calcAcc(proj, env):
    if env.isFrFall:
        return env.grav
    else:
        return proj.force / proj.mass

def calcKE(proj, env):
    proj.ke = env.sysEng - proj.pe
    return proj.ke

def calcPE(proj, env):
    proj.pe = proj.pos * proj.mass * env.grav
    return proj.pe

def setEngOfSys(proj, env):
    env.sysEng = calcPE(proj)

def calcBounceHt(proj, env):
    bounceHt = proj.pos * env.restCoef
    return bounceHt

def calcDrop(arg):
    pass

def calcTimeOfImpact(proj):
    timeOfImpact = math.sqrt((2*proj.pos)/proj.acc)
    return timeOfImpact

def updatePos(arg):
    newPos = calcBounceHt(arg)
    return newPos
