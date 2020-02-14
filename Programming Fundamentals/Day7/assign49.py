#PF-Tryout
import random

def biasedflip():
    if random.randrange(1,100) <= Probability_of_heads:
        print("Heads")
        results['heads'] +=1
    else:
        print("Tails")
        results['tails'] += 1


results = {
    'heads': 0,
    'tails': 0
}

i = 0
Probability_of_heads = 70
NumberOfTrials = 1000

while i < NumberOfTrials:
    biasedflip()
    i += 1

print("After {0} flips there was {1} Head(s) and {2} Tail(s)".format(NumberOfTrials,results['heads'],results['tails']))