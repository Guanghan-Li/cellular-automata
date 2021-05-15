"""
Cellular Automata is a type of simulation,
where you apply a set of rules to each generation and depending on those rules a 'cell' lives, dies or is born.
The simulation I made has each row be a generation and running that simulation over multiple generations
produces a pattern.
"""
# Returns the amount of width needed given the number of generations.
def getWidth(number_of_generations):
  return ((number_of_generations+1) * 2) + 1

# Turns a decimal number to a binary number and adds 0s to get 8 binary digits
def numToBin(number):
  binary_number = bin(number)[2:]
  padding = 8-len(binary_number)
  return '0'*padding + binary_number

# Takes a number, turns it into a binary number and then produces a rule set,
# which is a dictionary stating which configuration should lead to a living cell.
def makeRuleSet(rule):
  configurations = ['111', '110', '101', '100', '011', '010', '001', '000']
  binary_number = numToBin(rule)
  return dict( zip(configurations, binary_number) )

# Makes a new generation by taking the current one and a rule set.
# It loops over the generations and looks at 3 cells at a time and depending on the rule set it will make a cell with a 1 or 0
def makeNewGeneration(current_generation, rule_set):
  next_generation = [0]
  
  for i in range(len(current_generation)-2):
    triple = current_generation[i:i+3]
    triple = ''.join([str(num) for num in triple])
    next_cell = int(rule_set[triple])
    next_generation.append(next_cell)
  
  next_generation.append(0)
  return next_generation

# Returns a string that is a single row of
# characters using two generations from or simulation.
def generateRow(top_gen, bottom_gen):
  top_half = u'\u2580'
  bottom_half = u'\u2584'
  full = u'\u2588'
  empty = ' '
  row = ""
  for k in range(len(top_gen)):
    top_cell = top_gen[k]
    bottom_cell = bottom_gen[k]

    if top_cell == 0 and bottom_cell == 0:
      row += empty
    elif top_cell == 1 and bottom_cell == 0:
      row += top_half
    elif top_cell == 0 and bottom_cell == 1:
      row += bottom_half
    elif top_cell == 1 and bottom_cell == 1:
      row += full
  
  return row

# Loops over all of our generations, two at a time.
def printCells(generations):
  output = ""

  for i in range(0,len(generations)-1,2):
    top_gen = generations[i]
    bottom_gen = generations[i+1]

    row = generateRow(top_gen, bottom_gen)
    
    output += row + "\n"
  
  print(output)

# Takes in the number of generations and the rule represented as a decimal.
# Generates the rules set and then runs the simulation for the amount of generations is reached.
def runSimulation(number_of_generations, rule):
  width = getWidth(number_of_generations)
  start = [0] * width
  start[width//2] = 1
  generations = [start]
  rule_set = makeRuleSet(rule)

  for i in range(number_of_generations-1):
    new_gen = makeNewGeneration(generations[-1], rule_set)
    generations.append(new_gen)
  
  return generations


number_of_generations = int(input("How many generations: "))
rule =  int(input("Which rule, 0-255 : "))
generations = runSimulation(number_of_generations, rule)
printCells(generations)
