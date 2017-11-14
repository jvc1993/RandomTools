import subprocess
import os

branchPath = '/Users/johcollins/Documents/Firmware/firmware'
branchCommands = ["git", "branch"]
remoteDelete = ["git", "push", "origin", "--delete"]
localDelete = ["git", "branch", "-D"]
local = True
remote = True
branches = []

def deleteBranches(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, cwd=branchPath)
        output = process.communicate()[0]
        return_code = process.wait()
        print output
    except:
        print "something went wrong"

if os.path.isfile("branchList.txt"):
    #do some shit to delete the branches
    branchList = open("branchList.txt", 'r')

    for line in branchList:
        if line == "=== REMOVE BEFORE FLIGHT ===\n":
            print "WARNING!!! YOU DIDN'T REVIEW THE FILE, ABORTING"
            print "\n================================"
            print "Review branchList.txt and remove the '=== REMOVE BEFORE FLIGHT ===' tag, then rerun to clean branches" 
            print "================================"
            exit()

        for split in line.split():
            if remote == True:
                print "///////////////////////////// REMOTE"
                deleteBranches(remoteDelete + [split])
            if local == True:
                print "//////////////////////////// LOCAL"
                deleteBranches(localDelete + [split])
            


    #remove the file
    print "Removing branchList.txt"
    os.remove("branchList.txt")
    print "Done"
else: 
    #remove the old file file
    if os.path.isfile("branchList.txt"):
        print "** Removing old branchList.txt"
        os.remove("branchList.txt")

    print "** Creating clean branchList.txt"
    branchList = open("branchList.txt", 'w')
    branchList.write("=== REMOVE BEFORE FLIGHT ===\n")

    try:
        process = subprocess.Popen(["git", "branch"], stdout=subprocess.PIPE, cwd=branchPath)
        output = process.communicate()[0]
        print "** Writing Branches"

        for split in output.split():
            if split != '*' and split != ' ' and split != '\n':
                branchList.write(split + "\n")


        #branchList.write(output)
        branchList.close()



        print "** Done generating branchList"
        print "\n================================\n"
        print "Review branchList.txt and remove the '=== REMOVE BEFORE FLIGHT ===' tag, then rerun to clean branches" 
        print "\n================================\n"

    except:
        print "ERROR: please check to see if your branchPath is a valid git repo"
        branchList.close()
        os.remove("branchList.txt")

