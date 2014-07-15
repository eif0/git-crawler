#!/usr/bin/env python

# git-crawler - Git Email Crawler, and Information Disclosure Tool
# Written by eif0.
# Licenced under GPLv3
# Report git-crawler's bugs to eif0@hush.com


try:
    import sys
except:
    print("\n\nExecution error:\n\n  >> No python module named 'sys', please install it before running Xibalba.\n\n")
    quit()
    
if sys.version_info >= (3, 0):
    print("\n\nYou're running python3\n\nWe don't have a python3 port yet. Please run Xibalba with python2\n\n")
    sys.exit(2)
    
else:

    class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'    
    
    try:
        import os
        import getopt
        import subprocess
        import datetime
        import random
        import os.path

    except:
        e = sys.exc_info()[1]
        print("\n\nPython execution error: "+color.BOLD+str(e)+color.END+", please install it before running git-crawler.")
        print("\n\nPlease check git-crawler's python modules deps and install the one missing in your system:\n\n  - subprocess\n  - os\n  - sys\n  - random\n  - datetime\n  - getopt\n\n")
        sys.exit(2)
    

    def which(program):
        def is_exe(fpath):
            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                path = path.strip('"')
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file
        return None

    alldeps = ["python2", "man", "git"]
    for dep in alldeps:
        if (which(dep) == None):
            print("\n\nWARNING: Xibalba needs '"+color.BOLD+dep+color.END+"' to be installed in your system.\n\nPlease install '"+color.BOLD+dep+color.END+"' and try to run Xibalba again.\n\n")
            sys.exit(2)




    def CloneRepo(repo=None):
        tempdir = "/tmp/"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randrange(1000,9999))
        command = "git clone "+repo+" "+tempdir+" -q"
        os.system(command)
        return tempdir

    def RemoveRepo(tempdir=None):
        command = "rm -fr "+tempdir
        os.system(command)

    def MailCrawler(tempdir=None):
        command = "cd "+tempdir+";git log --pretty=format:'%ae%n%aE%n%ce%n%cE%n%ge%n%gE' > CrawlerResult"
        os.system(command)
        command = "grep -v '^$' "+tempdir+"/CrawlerResult | sort | uniq > "+tempdir+"/CrawlerResultParsed"
        os.system(command)
        with open(tempdir+"/CrawlerResultParsed") as file:
            mailsarray = file.readlines()
        return mailsarray
    
    
    if __name__ == "__main__":    
        try:
            opts, extra = getopt.getopt(sys.argv[1:], 'r:l:h', ['remote=','local=','help'])    
            if (extra != []):
                print("\n\nIt looks like you have added some non-valid params...\n\n")
                sys.exit(2)
        except:
            err = sys.exc_info()[1]
            print("\nWARNING: "+color.BOLD+color.UNDERLINE+str(err)+color.END)
            print("\nFor full documentation and help, use ["+color.BOLD+"-h"+color.END+', '+color.BOLD+"--help"+color.END+"] parameter\n\n")
            sys.exit(2)

        try:
            if (opts == []):
                print("\n\nIt looks like you forgot to add some params...\n")
                sys.exit(2)
        except:
            print("\nFor full documentation and help, use ["+color.BOLD+"-h"+color.END+', '+color.BOLD+"--help"+color.END+"] parameter\n\n")
            sys.exit(2)
            
        for code,param in opts:
            if code in ["-h","--help"]:
                pathname = os.path.dirname(sys.argv[0])
                os.system("man "+os.path.abspath(pathname)+"/MANPAGE")
                sys.exit(2)
            else:
                if code in ["-r","--remote"]:
                    dir = CloneRepo(param)
                    if (os.path.isfile(dir+"/.git/HEAD")):
                        mails = MailCrawler(dir)
                        print("\n")
                        cant = 0
                        for m in mails:
                            print("mail found: "+color.BOLD+color.UNDERLINE+m+color.END)
                            cant = cant+1
                        print("\n"+color.BOLD+color.UNDERLINE+"RESULT:"+color.END+" "+str(cant)+" mail(s) found!")
                        print("\n")                    
                        RemoveRepo(dir)
                    else:
                        print("\n\n"+color.UNDERLINE+"WARNING:"+color.END+color.BOLD+" "+param+color.END+" isn't a valid git repo url!\n\n")
                        sys.exit(2)
                        
                        
                elif code in ["-l","--local"]:
                    dir = param

                    if (os.path.isfile(dir+"/.git/HEAD")):
                        mails = MailCrawler(dir)
                        print("\n")
                        cant = 0
                        for m in mails:
                            print("mail found: "+color.BOLD+color.UNDERLINE+m+color.END)
                            cant = cant+1
                        print("\n"+color.BOLD+color.UNDERLINE+"RESULT:"+color.END+" "+str(cant)+" mail(s) found!")
                        print("\n")
                        os.system("rm -f "+dir+"/CrawlerResultParsed")
                        os.system("rm -f "+dir+"/CrawlerResult")
                    else:
                        print("\n\n"+color.UNDERLINE+"WARNING:"+color.END+color.BOLD+" "+dir+color.END+" isn't a valid git repo dir!\n\n")
                        sys.exit(2)
                        