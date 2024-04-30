import sys



def get_file_contents(filename):
  """Reads the contents of a file with a .morse extension and returns it as a string."""
  try:
    with open(filename, 'r') as file:
        return file.read()
  except FileNotFoundError:
    print("Error: File not found.")
    return None
  except IOError:
    print("Error: An error occurred while reading the file.")
    return None

def read_morse_file():
  if len(sys.argv) != 2:
    print("Usage: python MorseCoding.py filename.morse")
    return
  
  filename = sys.argv[1]
  if not filename.endswith('.morse'):
    print("Error: The file must have a .morse extension.")
    return
  
  file_contents = get_file_contents(filename)
  if file_contents is not None:
    return(file_contents)
    


program = read_morse_file()
program = list(program)




class Node:
  def __init__(self, value):
    self.value = value
    self.left = None  # Left child
    self.right = None  # Right child

class BinaryTree:
  def __init__(self):
    self.root = None  # Root node

#####################################   THE TREE   ########################################
MorseCodingTree = BinaryTree()
MorseCodingTree.left = Node(None)
MorseCodingTree.left.left = Node(None)
MorseCodingTree.left.left.left = Node(None)
MorseCodingTree.left.left.left.left = Node("}")
MorseCodingTree.left.left.right = Node("WHILE")
MorseCodingTree.left.right = Node(None)
MorseCodingTree.left.right.left = Node("IF")
MorseCodingTree.left.right.right = Node("ELSE")
MorseCodingTree.right = Node(None)
MorseCodingTree.right.left = Node(None)
MorseCodingTree.right.left.left = Node(None)
MorseCodingTree.right.left.left.left = Node(None)
MorseCodingTree.right.left.left.left.left = Node("PLUS")
MorseCodingTree.right.left.left.left.right = Node("MINUS")
MorseCodingTree.right.left.left.right = Node(None)
MorseCodingTree.right.left.left.right.left = Node("MULT")
MorseCodingTree.right.left.left.right.right = Node(None)
MorseCodingTree.right.left.left.right.right.left = Node("MOD")
MorseCodingTree.right.left.left.right.right.right = Node("DIVIDE")
MorseCodingTree.right.right = Node(None)
MorseCodingTree.right.right.left = Node(None)
MorseCodingTree.right.right.left.left = Node("INT_ASSIGN")
MorseCodingTree.right.right.left.right = Node("STRING_ASSIGN")
MorseCodingTree.right.right.right = Node("PRINT")




state = []
block_stack = []
pc = 0


def varmap(var):
  for i in state:
    if i[0] == var:
      return i[1]
  return None

def assign(key, value):
  if varmap(key) != None:
    for i in state:
      if i[0] == key:
        state.remove(i)
  state.append((key,value))



def literalIn():
  literal = []
  global pc
  while True:
    if program[pc] != '0' and program[pc] != '1':
      pc += 1

    literal.append(program[pc])
    pc += 1

    last_items = literal[-4:]  # Slice the last 3 elements
    joined_string = ''.join(last_items)  # Join elements into a string
    if joined_string == "0000":
      joined_variable = ''.join(literal[:-4])
      return joined_variable
    

def intIn():
  binary_list = []
  global pc
  for i in range(16):

    if program[pc] != '0' and program[pc] != '1':
      pc += 1

    binary_list.append(int(program[pc]))
    pc += 1

  is_negative = binary_list[0] == 1
  # Convert the binary digits to their decimal equivalents and sum them
  decimal_value = 0
  for i in range(16):
    decimal_value += binary_list[i] * (2 ** (15 - i))

  # Handle negative numbers using two's complement
  if is_negative:
    decimal_value = - (decimal_value - (2 ** 16))

  return decimal_value


MorseCodeTree = BinaryTree()
MorseCodeTree.left = Node("E")
MorseCodeTree.left.left = Node("I")
MorseCodeTree.left.left.left = Node("S")
MorseCodeTree.left.left.left.left = Node("H")
MorseCodeTree.left.left.left.right = Node("V")
MorseCodeTree.left.left.right = Node("U")
MorseCodeTree.left.left.right.left = Node("F")
MorseCodeTree.left.right = Node("A")
MorseCodeTree.left.right.left = Node("R")
MorseCodeTree.left.right.left.left = Node("L")
MorseCodeTree.left.right.right = Node("W")
MorseCodeTree.left.right.right.left = Node("P")
MorseCodeTree.left.right.right.right = Node("J")
MorseCodeTree.right = Node("T")
MorseCodeTree.right.left = Node("N")
MorseCodeTree.right.left.left = Node("D")
MorseCodeTree.right.left.left.left = Node("B")
MorseCodeTree.right.left.left.right = Node("X")
MorseCodeTree.right.left.right = Node("K")
MorseCodeTree.right.left.right.left = Node("C")
MorseCodeTree.right.left.right.right = Node("Y")
MorseCodeTree.right.right = Node("M")
MorseCodeTree.right.right.left = Node("G")
MorseCodeTree.right.right.left.left = Node("Z")
MorseCodeTree.right.right.left.right = Node("Q")
MorseCodeTree.right.right.right = Node("O")



def strIn():
  identifier = []
  str = []
  morseCode = MorseCodeTree


  global pc


  while True:


    if program[pc] != '0' and program[pc] != '1':
      pc += 1

    identifier.append(program[pc])

    if identifier == ['0', '0', '0']:
      joined_string = ''.join(str) 
      pc += 1
      return joined_string
    if identifier == ['1', '0', '0']:
      str.append(morseCode.value)
      morseCode = MorseCodeTree
      identifier = []
    if identifier == ['1', '1', '0']:
      morseCode = morseCode.left
      identifier = []
    if identifier == ['1', '1', '1']:
      morseCode = morseCode.right
      identifier = []
    
    pc += 1

    





def checkForElse():
  global pc
  try:
    i = 0
    while True:
      if program[pc+i] == '1':
        return False
      if program[pc+i] == '0':
        i+=1
        break
      i+=1
    while True:
      if program[pc+i] == '0':
        return False
      if program[pc+i] == '1':
        i+=1

        break
      i+=1
    while True:
      if program[pc+i] == '0':
        return False
      if program[pc+i] == '1':
        pc += i+1

        return True
      i+=1
  except:
    return False
  

def whileEvaluate():
  global pc

  try:
    i = 0

    while True:
      if program[pc+i] == '0':
        pc += i+1
        condition1 = varmap(literalIn())
        condition2 = varmap(literalIn())
        if condition1 < condition2: return True
        else: return False
      if program[pc+i] == '1':
        i+=1
        break
      i+=1
    while True:
      if program[pc+i] == '0':
        pc += i+1
        condition1 = varmap(literalIn())
        condition2 = varmap(literalIn())
        if condition1 != condition2: return True
        else: return False
      if program[pc+i] == '1':
        pc += i+1
        condition1 = varmap(literalIn())
        condition2 = varmap(literalIn())
        if condition1 == condition2: return True
        else: return False
      i+=1
  except:
    return False
  


def resetMapping():
  global mapping
  mapping = MorseCodingTree
  global mapped
  mapped = False


mapping = MorseCodingTree
mapped = False


while pc < len(program):
    
    
  # try:
    if program[pc] == '0':   
      mapping = mapping.left
    elif program[pc] == '1':  
      mapping = mapping.right
    else:
      pc += 1
      continue

    pc += 1
      
    if mapping.value is not None:

      if mapping.value == "}":
        if block_stack[-1][0] == "loop":
          pc = block_stack[-1][1] - 1
          resetMapping()
          continue
        else:
          try:
            if checkForElse():
              if block_stack[-1][1]:
                block_stack[-1] = ("if", False)
              else:
                block_stack[-1] = ("if", True)

              resetMapping()
              continue
            else:
              block_stack.pop()
              resetMapping()
              continue
          except:
            block_stack.pop()
            resetMapping()
            continue

      if(len(block_stack) != 0):
        if((block_stack[-1][1]) == False):
          if mapping.value == "IF":
            block_stack.append(("if", False))
            literalIn()
            literalIn()
            resetMapping()
            continue

          # print(program[pc-4:pc+100])
          match mapping.value:
            case "PLUS" | "MINUS" | "MULT" | "MOD" | "DIVIDE":
              literalIn()
              literalIn()

            case "INT_ASSIGN":
              literalIn()
              intIn()

            case "STRING_ASSIGN":
              literalIn()
              strIn()

            case "PRINT":
              literalIn()

            case _:
              z = 1

          resetMapping()
          continue

      match mapping.value:

        case "WHILE":
          whilepc = pc-3
          evaluates = whileEvaluate()
          if evaluates:
            if len(block_stack) != 0:
              if block_stack[-1][1] != whilepc:
                block_stack.append(("loop", whilepc))  
            else:
              block_stack.append(("loop", whilepc))   
 
          else:
            block_stack.pop()
            block_stack.append(("if", False))

        case "IF":
          condition1 = literalIn()
          condition2 = literalIn()
          if varmap(condition1) == varmap(condition2):
            block_stack.append(("if", True))
          else:
            block_stack.append(("if", False))
        
        case "PLUS":
          var1 = literalIn()
          var2 = literalIn()
          assign(var1, varmap(var1) + varmap(var2))

        case "MINUS":
          var1 = literalIn()
          var2 = literalIn()
          assign(var1, varmap(var1) - varmap(var2))

        case "MULT":
          var1 = literalIn()
          var2 = literalIn()
          assign(var1, varmap(var1) * varmap(var2))

        case "MOD":
          var1 = literalIn()
          var2 = literalIn()
          assign(var1, varmap(var1) % varmap(var2))
        
        case "DIVIDE":
          var1 = literalIn()
          var2 = literalIn()
          assign(var1, varmap(var1) / varmap(var2))

        case "INT_ASSIGN":
          variable = literalIn()
          intValue = intIn()
          assign(variable, intValue)

        case "STRING_ASSIGN":
          variable = literalIn()
          strValue = strIn()
          assign(variable, strValue)

        case "PRINT":
          variable = literalIn()
          print(varmap(variable))

        case _:
          print("ERROR")

      resetMapping()

  # except:
  #   print("Error")