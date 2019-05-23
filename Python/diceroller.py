import random, statistics

def avg(L):
  return (sum(L)/len(L),0)[len(L) == 0]

def roll(maxVal, rolls):
  return [random.choice(range(1,maxVal+1)) for roll in range(rolls)]

def getAttribute():
  rolls = []
  rolls += roll(6,4)
  rolls.remove(min(rolls))
  return rolls

def getCharacterStats():
  stats = []
  for i in range(0, 6):
    stats.append(sum(getAttribute()))
  return stats

stats = getCharacterStats()
while avg(stats)<15:
  stats=getCharacterStats()
print(stats)