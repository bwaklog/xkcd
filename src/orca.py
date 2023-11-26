import os
import re

def filter_transcript(transcript):
    filtered = "".join([
        i for i in transcript
        if i.isalpha() or i == " "
    ])
    return f"explain the xkcd comic with transcript {filtered}"

def generator(transcript, model):
    req = "curl http://localhost:11434/api/generate -d '{\"model\":\"orca-mini\",\"prompt\":\"" + transcript +"\",\"stream\": false }'"
    stream = os.popen(req)
    output = str(stream.read().strip())

    matchRE = r'"response":" .[a-zA-Z\ !@#$%^&*()+_=0-9\-\[\]\{\};:\',<.>/?\\\/]{1,}"'

    match = re.search(matchRE, output)

    match = re.search(matchRE, output)
    response = match.group()
    # response = response.partition("\"response\":")[2]
    print(response)

