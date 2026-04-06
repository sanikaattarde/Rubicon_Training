import os
import sys


def DirectoryWatcher(path):
    # isabs check is given path is absolute path or not
    # if it os not a absolute path then convert it into absolute path
    flag=os.path.isabs(path)
    # here convert relative path to absolute path

    if flag == False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)   
    # checks given path is valid directory

    if exists:
        for foldername , subfolder , filename in os.walk(path):
            print("Current folder is :- "+foldername)
            for subf in subfolder:
                print("Sub folder of "+foldername + " is :-" + subf)
            for filen in filename:
                print("File inside "+ foldername+ " is :-" + filen)
            print(' ')

    else:
        print("Invalid path")

def main():
    print("Application name :- "+ sys.argv[0])
    # provide only one argument

    if (len(sys.argv) !=2):
        print("Error: Invalid number of arguments")
        exit()

    # -h and -H used for help mesg
    if (sys.argv[1] =="-h") or (sys.argv[1]=="-H"):
        print("This script is used to traverse specific directory")
        exit()

    # it displays following msg for absolutr path
    if(sys.argv[1]=="-u") or (sys.argv[1]=="-U"):
        print("usage: ApplicationName AbsolutePath_of_Directory")
        exit()
    try:
        DirectoryWatcher(sys.argv[1])
    except ValueError:
        print("Error: Invalid datatype of input")
    
    except Exception:
        print("Error : Invalid input")

if __name__=="__main__":
    main()