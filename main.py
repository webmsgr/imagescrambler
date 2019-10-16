import math
from hilbertcurve.hilbertcurve import HilbertCurve
from PIL import Image
import numpy
def checksides(length):
    if length == 2:
        return False
    try:
        return length == 2**round(math.log(length,2))
    except Exception:
        return False

def gethilbert(length):
    return int(math.log(length,2))

def getcurve(length,dim):
    return HilbertCurve(gethilbert(length),dim)

def twoto1(inarr):
    sidelen = int(math.sqrt(len(inarr)*len(inarr[0])))
    if checksides(sidelen):
        incurve = getcurve(sidelen,2)
        outarray = [""]*sidelen**2
        for s,_ in enumerate(outarray):
            print("{0[0]},{0[1]} -> {1}".format(incurve.coordinates_from_distance(s),s))
            x,y = incurve.coordinates_from_distance(s)
            outarray[s] = inarr[y][x]
        return outarray
    else:
        raise Exception("Side length does not fit the requirements of 2^n = {} where n is an int".format(sidelen))
def oneto2(inarr):
    sidelen = int(math.sqrt(len(inarr)))
    if checksides(sidelen):
        incurve = getcurve(sidelen,2)
        outarray = []
        for i in range(sidelen):
            outarray.append([""]*sidelen)
        for s in range(sidelen**2):
            print("{0[0]},{0[1]} <- {1}".format(incurve.coordinates_from_distance(s),s))
            x,y = incurve.coordinates_from_distance(s)
            outarray[y][x] = inarr[s]
        return outarray
    else:
        raise Exception("Side length does not fit the requirements of 2^n = {} where n is an int".format(sidelen))


def pagesto2(pages):
    out = []
    for page in pages:
        out.append(twoto1(page))
    return out

def imagtopages(img,sidelen):
    img = numpy.array(img).tolist()
    pgs = blankpages(sidelen,-1)
    for y,row in enumerate(img):
        for x,data in enumerate(row):
            print(data)
            pgs[0][y][x] = data[0]
            pgs[1][y][x] = data[1]
            pgs[2][y][x] = data[2]
    return pgs

def blankpages(length,blnk=0):
    out = []
    for j in range(length):
        r = []
        for i in range(length):
            r.append([blnk for g in range(length)])
        out.append(r)
    return out


img = Image.open("32x32.jpg")
img = imagtopages(img,32)
freespace = 0
for oned in img:
    for twod in oned:
        for threed in twod:
            if threed == -1:
                freespace += 1
print("in a 32 by 32 image, there are {} bytes of freespace".format(freespace))