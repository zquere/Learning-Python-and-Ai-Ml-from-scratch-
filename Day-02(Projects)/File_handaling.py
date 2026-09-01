# making file_handaling program..
from pathlib import Path
import os 

#this is functing for doing all stuff
def createfile():
    try:
       name = input("please tell your file name:- ")
       path = Path(name)
       if not path.exists():
          with open(path, "w", encoding="utf-8") as fs:
            data = input("\nWhat you want to write: ")
            fs.write(data)
          print("file created successfully")

       else:
            print("Error File name already exists")
    except Exception as err:
        print(f"an error occured as {err}")
    

def readfile():
    try:
        name = input("\nFile_name as Read:-")
        path = Path(name)
        if path.exists():
         with open(path,"r") as fs:
             contant = fs.read()
             print(contant)

        else:
            print("file is exist...")

    except Exception as es:
        print(f"Error accure {es}")

def updatefile():
   try:
       name = input("\nFile_name for Update:-")
       path = Path(name)
       if path.exists():
          print("operation ")
          print("1. Renaming the file")
          print("2. Appending the content")
          print("3. overwriting the file")

          choise = int(input("\nchoose your option:-"))
          if choise == 1:
             newname = input("tell your new_file_name:- ")
             new_path = Path(newname)
             if not new_path.exists():
                path.rename(new_path)
                print("rename successfully...")

          elif choise == 2:
             with open(name,"a") as fs:
                data = input("what do you want to append:- ")
                fs.write("\n"+data)
             print("successfully appended")

          elif choise ==3:
             with open(path,"w") as fs:
                contant = input("file over_writing:- ")
                fs.write("\n"+contant)
             print("successfully overwrite...")
   except Exception as er:
     print(f"\nError occure {er}")

def deletefile():
  try:
    name = input("give file name :- ")
    path = Path(name)
    if path.exists():
       path.unlink()
       print("file deleating successfully")

    else:
       print("error file not found")

  except Exception as er:
     print(f"error occure {er}")


# first user input
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

a = int(input("\ntell your response :- "))

if a == 1:
    createfile()

if a == 2:
    readfile()

if a == 3:
    updatefile()

if a == 4:
    deletefile()

# Note - we can make more stuff like zip, un-zip and we need to run this software every time we can do looping  
#so for this in functing   when file didnt exist it exist() so we conntect  and write some more code for creating and exicuting thing...
