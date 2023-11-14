import apiHelper
import fuzzyMode
import gigaChecker
import subprocess, sys, os

HELP_FILE = "../help.txt"

# comic class : apiHelper.Comic

# default verbose value
verbose = False

# default comic request
# default : comic var stores the latest publication number
# comic = gigaChecker.get_latest(verbose=verbose)

flags = sys.argv[1:]
if verbose:
    print(flags)

if sys.platform in ['darwin', 'linux']:
    os.system("clear")
else:
    os.system("cls")

if flags == []:
    print("No flags passed")
    os.system(f"cat {HELP_FILE}")

else:


    if flags[0] in ['-l', '--latest']:
        print("🚀 Getting Latest Comic")
        latest_num = gigaChecker.get_latest()
        comic = apiHelper.Comic(num=latest_num)


    elif flags[0] in ['-s', '--search']:
        print("🔍 Starting fuzzyMode")
        

    elif flags[0].isdigit():
        print(f"🌐 Fetching comci {flags[0]}")
        # check availablity
        comic = apiHelper.Comic(num=int(flags[0]))
        comic.cli_display()
        comic.comic_display(True)


    elif flags[0] in ['-h', '--help']:
        os.sysconf(f"cat {HELP_FILE}")
        quit()


    else:
        os.sysconf(f"cat {HELP_FILE}")
        quit()

if len(flags) > 1:
    print(flags)

    if set(flags).intersection(set(['-q', '--ql'])) != set():
        # code for running quick look/image opening feature
        print("Quicklook")

    if set(flags).intersection(set(['-s', '--save'])) != set():
        # code for running saving features
        print("Saving")
