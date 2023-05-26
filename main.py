import requests
import json
import sys


def get_latest_comic(verbose):
    exists = True
    # Check last saved latest checkpoint
    with open("latest.txt", "r") as f:
        comic = int(f.read())
    while exists:
        if verbose:
            print(f"    current comic =====> {comic}")
        req = requests.get(f"https://xkcd.com/{str(comic)}/info.0.json")
        if req.status_code != 404:
            # open latest.txt in write mode and write
            # the latest comic to file
            with open("latest.txt", "w") as f:
                f.write(str(comic))
                f.flush()
            comic += 1
        if req.status_code == 404:
            exists = False
            return comic - 1


def get_comic(verbose=False, comic="latest"):
    latest_comic = get_latest_comic(verbose)
    if comic.isdigit() and int(comic) > latest_comic:
        return f"ERROR, latest comic is {latest_comic}"

    if comic == "latest":
        comic_request = requests.get(
            f"https://xkcd.com/{str(latest_comic)}/info.0.json")
        return json.dumps(comic_request.json(), indent=4)
    else:
        comic_number = str(comic)
        comic_request = requests.get(
            f"https://xkcd.com/{comic_number}/info.0.json")
        return json.dumps(comic_request.json(), indent=4)


if __name__ == "__main__":
    comic = "latest"
    verbose = False
    args = sys.argv[1:]
    if len(args) > 1:
        if args[1] in ['-v', '--verbose']:
            verbose = True
        else:
            verbose = False
    else:
        verbose = False

    if args[0]:
        if args[0] in ['-l', '--latest']:
            comic = "latest"
        elif args[0].isdigit():
            comic = args[0]
    else:
        print(
            "Please specify a comic number or use the -l\
            (or --latest) flag to get the latest comic"
        )

    print(get_comic(verbose=verbose, comic=comic))
