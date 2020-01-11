
from datetime import datetime as dt
import math
import sys


def primeGen():
    prime=[]
    current=2
    while 1:
        isprime=True
        stopPoint=math.sqrt(current)
        for divisor in prime:
            if divisor > stopPoint:
                break
            if current%divisor==0:
                isprime=False
                break
        if isprime:
            prime.append(current)
            yield current
        current+=1
def PresentTime(timeObj):
    time=timeObj.days*24*60*60+timeObj.seconds+timeObj.microseconds/1000000
    if time<0.001:
        return "{} microseconds".format(time*1000000)
    if time<1:
        return "{} milliseconds".format(time*1000)
    return "{} seconds".format(time)
gen=primeGen()
value=int(input("Enter a number"))
inputvalue=value

primeIndex=1

currentPrime=next(gen)
results={}
hasBeenInterrupted=False
startTime=dt.now()
try:
    while value>1:
        print("\rPlease wait,now factorizing with...{}(The {}th prime)".format(currentPrime,primeIndex),end="")
        if value%currentPrime==0:
            value/=currentPrime
            if currentPrime not in results:
                results[currentPrime]=1
            else:
                results[currentPrime]+=1
        else:
            currentPrime=next(gen)
            primeIndex+=1
except KeyboardInterrupt:
    hasBeenInterrupted=True
timeDiff=dt.now()-startTime

if inputvalue in results:
    print("\r{} is prime.{}".format(inputvalue," "*100))
    print("Answer fund in {}".format(PresentTime(timeDiff)))
    sys.exit()
print("\r =".format(inputvalue),end="")
isFirstFactor=True
sortedPowers=sorted(list(results.keys()))[::-1]

for factor in sortedPowers:
    power = results[factor]
    if not isFirstFactor:
        print(" x ",end="")
    if power!=1:
        print("{}^{}".format(factor,power),end="")
    else:
        print("{}".format(factor),end="")
    isFirstFactor=False
if hasBeenInterrupted:
    print(" +{}(unfactorized)".format(int(vale)),end="")
print(" "*100)
print("Answer found in {}".format(PresentTime(timeDiff)))
