#MIT - All will conform

#flip the cap puzzle 
def performOnepassConform(caps):
  caps = caps + [caps[0]]
  for i in range(1,len(caps)):
    if caps[i] != caps[i-1]:
      if caps[i] != caps[0]:
        print "Flip ",i, 
      else:
        print " through ",i-1

if __name__ == "__main__":
  caps = ['F','F','B','F','B','B','F','F','B','B']
  performOnepassConform(caps)
