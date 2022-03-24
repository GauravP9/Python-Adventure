alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Caeser code but here both the functions are combined in single function and executed

def cipher(plain_text,shift_amount):
  cipher=""
  
for char in plain_text:
  if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      cipher += alphabet[new_position]
  else:
      cipher += char
  print(f"Here's the {direction}d result: {cipher}")

  for char in plain_text:
    position=alphabet.index(char)
    if direction=="encode":
     cipher+=alphabet[actual_shift]
        
    else:
      cipher+=alphabet[actual_shift]
        
  print(f"The {direction} word is {cipher}")

cipher(plain_text=text,shift_amount=shift)
