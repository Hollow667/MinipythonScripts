
# First, install wget by 'pip install wget'
import os
try:
    import wget
except:
    os.system('pip install wget')
starkislub = input("Give Download Link. \n")
pathdebc = input(r"Give Path Where This File should be Saved." + " \n")
print("Ok, Let me try to Download this.")
try:
  sedlyf = wget.download(starkislub, out = pathdebc)
  print(f"Downloaded Sucessfully in {sedlyf}.")
  print("---------- + ----------")
except Exception as e:
  print(f"I can't download it \nReason : {e}")
