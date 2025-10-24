import os

val = int(input("Enter the number of text files which you want to change : "))
print("This will take text files as input and convert it to other types")
ftype = input("Enter the type of file which you want it will convert the all files as you mentioned in the type: ")
for i in range(1,val+1):
    os.rename(f"file{i}.txt",f"file{i}.{ftype}")

print(f"{val} files are converted")
  