import random, statistics

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

count = 1
stats = getCharacterStats()
print(stats)