import apiHelper
import fuzzyMode
import gigaChecker
import sys, os

HELP_FILE = "./help.txt"

# comic class : apiHelper.Comic

# default verbose value
verbose = False

# default comic request
# default : comic var stores the latest publication number
# comic = gigaChecker.get_latest(verbose=verbose)

flags = sys.argv[1:]
if verbose:
    print(flags)


def os_clear():
    if sys.platform in ['darwin', 'linux']:
        os.system("clear")
    else:
        os.system("cls")

os_clear()

if flags == []:
    print("No flags passed")
    os.system(f"cat {HELP_FILE}")

else:


    if flags[0] in ['-l', '--latest']:
        print("🚀 Getting Latest Comic")
        gigaChecker.update_storage()
        latest_num = gigaChecker.get_latest()
        comic = apiHelper.Comic(num=latest_num)
        comic.cli_display()


    elif flags[0] in ['-f', '--fuzzy']:
        print("🔍 Starting fuzzyMode")
        a = 1
        while a != 0:
            a = fuzzyMode.fuzzy_prompt()
            if type(a) == apiHelper.Comic:
                comic = a
                # comic object is now stored under varaible comic
                break


    elif flags[0] in ['-s', '--search']:
        print("🕵️ Starting Search")
        a = 1
        while a != 0:
            a = fuzzyMode.alt_serach()
            if type(a) == apiHelper.Comic:
                comic = a
                break

    elif flags[0].isdigit():
        print(f"🌐 Fetching comci {flags[0]}")
        # check availablity
        comic = apiHelper.Comic(num=int(flags[0]))
        comic.cli_display()
        # comic.comic_display(True)


    elif flags[0] in ['-h', '--help']:
        os.system(f"cat {HELP_FILE}")
        quit()


    else:
        os.system(f"cat {HELP_FILE}")
        quit()

if len(flags) > 1:
    print(flags)

    if set(flags).intersection(set(['-q', '--ql'])) != set():
        # code for running quick look/image opening feature
        print("Quicklook")
        if sys.platform == 'darwin':
            comic.comic_display(ql=True)
        else:
            comic.comic_display()

    if set(flags).intersection(set(['-s', '--save'])) != set():
        # code for running saving features
        print("Saving")
