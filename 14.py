for x in '0123456789ABCDEFGHIJKLM':
  number = int(f"7{x}38596", 23) + int(f"14{x}36", 23) + int(f"61{x}7", 23)
  if number % 22 == 0:
    print(x, number / 22)