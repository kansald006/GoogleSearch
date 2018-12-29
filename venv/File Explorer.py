import os

path = os.getcwd()
print("CWD:", path)

# allfiles = list(files)
# print(type(allfiles))
# print(allfiles)
# String=str(allfiles)
# print(type(String))
song=0
doc=0
for root, dirs, files in os.walk("E:/new music"):
   for f in files:
       filename=os.path.join(root,f)
       if filename.endswith('.mp3'):
        song = song + 1
        print(filename,":",song)
print("Total Songs:" ,song)