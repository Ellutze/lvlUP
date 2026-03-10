
import os


def lvl1(path=None,race="Human"):

    #Assuming randomisation if abilities not provided


    #Assuming point buy system if 

    return(CS)


def lvlUP(CS,path=None):

    #This function loads JSON of part if awailable, then it loads LVL up instructions for subclass, and allows user to level-up.


    return(CS)

def initiate(CS=None,path=None):

    if path == None:
        path = os.getcwd()

    if CS==None:
        CS = lvl1(path=path)
    else:
        CS = lvlUP(CS,path=path)
    
    #Save JSON 



if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description="lvlUP")
    parser.add_argument("-n","--name",type=str,help="Name of character, if not found, new character will be created.")
    parser.add_argument("-p","--path",type=str,help="Unless working in local libraries folder, specify location.")

    args = parser.parse_args()

    initiate(CS=args.name,
          path=args.path)




















