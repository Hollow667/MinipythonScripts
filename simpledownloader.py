# First, install wget by 'pip install wget'
import os
import wget

starkislub = input("Give Download Link. \n")
pathdebc = input(r"Give Path Where This File should be Saved. \n")
print("Ok, Let me Download this.")
try:
  sedlyf = wget.download(starkislub, out = pathdebc)
  print("Downloaded Sucessfully in {sedlyf}.")
  print("---------- + ----------")
except Exception as e:
  print("I can't download it \nReason : {e}")
