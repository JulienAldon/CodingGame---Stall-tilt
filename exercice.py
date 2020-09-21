import sys
import math
import collections

def fall(speed, radius):
    """given speed and radius return if you fall or not"""
    s = optiSpeed(radius)
    if (speed > s):
        return True
    else:
        return False

def optiSpeed(minR):
    """given min radius return the opti speed"""
    speed = math.sqrt(math.atan(60) * (minR * 9.81))
    return (math.ceil(speed))

if __name__ == "__main__":
    n = int(input())
    v = int(input())
    ranking = collections.OrderedDict()
    finalRanking = collections.OrderedDict()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    speeds = []
    bends = []
    if (v > 13):
        print("v must be less than 13.")
        sys.exit(-1)
    if (n < 0):
        print("n must be positive.")
        sys.exit(-1)
    for i in range(n):
        current = int(input())
        if (current > 0 and current < 70):
            speeds.append(current)
        else:
            print("error speed is too high.")
            sys.exit(-1)
    for i in range(v):
        bends.append(int(input()))

    i = 0
    # create ranking
    for s in speeds:
        ranking[letters[i]] = s
        i +=1
    # sort
    ranking = collections.OrderedDict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))
    finalRanking = ranking.copy()
    falls = [[]]
    # get falls in list
    for key, value in ranking.items():
        i = 0
        for b in bends:
            falls.append([])
            if(fall(value, b)):  
                falls[i].append((key, value))
                finalRanking.pop(key, None)
                break
            i += 1
    tmp = []
    orderedFalls = []
    [tmp.append(x) for x in falls if x not in tmp] # delete doubles
    tmp.reverse()
    orderedFalls = [i for a in tmp for i in a] # create the last ranking (all the falls)

    # display
    print(optiSpeed(min(bends)))
    print("y")
    finalRanking.update(dict(orderedFalls))
    for key, value in finalRanking.items():
        print(key)
