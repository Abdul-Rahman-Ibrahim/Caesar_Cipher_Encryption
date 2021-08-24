def encrypt(message, key):
  
  #Create list of alphabets from a to z
  list_of_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                       "n","o","p","q","r","s","t","u","v","w","x","y","z"]
  
  encrypted_message = ""
  for ch in message:
    if ch.lower() in list_of_alphabets:
      
      i = list_of_alphabets.index( ch.lower() )
      new_ch = list_of_alphabets[(i+key) % 26]
      if ch.isupper():
        new_ch = new_ch.upper()
      encrypted_message += new_ch
      
    else:
      encrypted_message += ch
  
  return encrypted_message
