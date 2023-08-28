from cryptography.fernet import Fernet

def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

pw_master = input('Please enter your master password: ')
key = load_key() + pw_master.encode() #bytes match bytes
fer = Fernet(key)


'''
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)''' #the ''' writes it out

#this is where the write key was, only need to run it once.

def view():
  with open('passwords.txt', 'r') as f:
    for line in f.readlines():
      data = (line.rstrip()) 
      user, passw = data.split('|')
      print('Username: ', user, '| Password: ', fer.decrypt(passw.encode()).decode())
  

def add():
  name = input('Account username: ')
  pwd = input("Password: ")

  with open('passwords.txt', 'a') as f: #this opens the file and closes it when done
    f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n') #linebreak


while True:
  mode = input('Press a to add a new password.  Press b to view existing passwords.  Press q to quit. ').lower()
  if mode == "q":
        break

  if mode == "b":
        view()
  elif mode == "a":
        add()
  else:
      print("Invalid entry.  Learn to read.")
      continue