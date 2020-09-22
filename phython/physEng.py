from phyUI import *
from phyEquat import *
import pygame
import time

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
#dict of gravity settings
gravSet = {
    "earth" : 9.801,
    "mars" : 3.711,
    "jupiter" : 24.790
}

#creating initial children
proj1 = projectile(1, materials[0], 0, 0, 0, 1, 0, 0, 0, 0)
surf = surface(materials[0], 0)
env = enviroment(9.801, 0, 0, 0, True, 0)

#dict of projectile data at time slices
#seconds : projectile data
projData = {
    0 : proj1
}

#dict of enviromet data at time slices
#seconds : env data
envData = {
    0 : env
}


#initalize all children as zero and wait to get selections from user

#after all user inputs have been taken and applied to the objects
#runSim() function should be called on button click of the "play" button
def runSim(proj, env, surf):
    pass