
from phyUI import *
from phyEquat import *
#parent classes
class projectile:
    def __init__(self, mass, mat, airRes, force, mome, pos, pe, ke, acc, v):
        self.mass = mass #in KG
        self.mat = mat
        self.airRes = airRes
        self.force = force
        self.mome = mome
        self.pos = pos # height in meters
        self.pe = pe
        self.ke = ke
        self.acc = acc
        self.v = v

class enviroment:
    def __init__(self, grav, surfOnsurf, time, restCoef, isFrFall, sysEng):
        self.grav = grav
        self.surfOnsurf = surfOnsurf
        self.time = time
        self.restCoef = restCoef
        self.isFrFall = isFrFall
        self.sysEng = sysEng

class surface:
    def __init__(self, mat, pos):
        self.mat = mat
        self.pos = pos

#list of materials
materials = ["wood", "steel"]
#dict of surf to surface friction coeficients
surfFriction = {
    "WoodOnWood" : .2,
    "WoodOnSteel" : .35,
    "SteelOnSteel" : .57
}
#dict of resittitution coeficients
resttitution = {
    "WoodOnWood" : .5,
    "WoodOnSteel" :.53,
    "SteelOnSteel" : .56
}
#creating initial children
proj1 = projectile(1, materials[0], 0, 0, 0, 1, 0, 0, 0, 0)
surf = surface(materials[0], 0)
env = enviroment(9.8, 0, 0, 0, True, 0)
#initalize all children as zero and wait to get selections from user
