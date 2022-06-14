cell = [0]
cell_idx = 0

while True:
    us = input("BrainBomb: ")

    if '+' in us:
      plus_count = us.count('+')
      cell[cell_idx] += plus_count
     
    elif '-' in us:
      minus_count = us.count('-')
      cell[cell_idx] -= minus_count
    elif '>' in us:
      more_than = us.count('>')
      cell_idx += more_than
      if len(cell) <= cell_idx:
          cell.append(0)
    elif '<' in us:
      less_than = us.count('<')
      cell_idx -= less_than
      if cell_idx < 0:
          cell_idx = 0
    elif '.' in us:
      print(chr(cell[cell_idx]))
    elif ',' in us:
      cell[cell_idx] = ord(input("BrainBomb: "))
    elif '[' in us:
     if cell[cell_idx] == 0:
          us = us[1:]
          while ']' not in us:
              us = input("BrainBomb: ")
    elif '#' in us:
      hashcount = us.count('#')
      cell[cell_idx] *= hashcount
    elif '$' in us:
      dollarcount = us.count('$')
      cell[cell_idx] //= dollarcount
    elif '!' in us:
      cell[cell_idx] = 0
    elif '@' in us:
      cell[cell_idx] = int(input("BrainBomb: "))
    elif '^' in us:
      cell[cell_idx] = cell[cell_idx] ** 2
    elif '/' in us:
      print(cell)
    elif '?' in us:
      print(cell_idx)
    elif '\t' in us:
      continue
    elif us is None or us == '': 
      continue
    else:
      print("BrainBomb: Unknown command '" + us + "'")
