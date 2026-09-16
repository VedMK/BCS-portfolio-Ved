import requests as req

target=input("Insert domain name/ip-address here")
dir_file="directories.txt"

def chk_url(url): # Checking response headers
    response=req.get(url,timeout=5)
    output={
        "url":url,
        "Status-Code":response.status_code,
        "Content-length":len(response.content)
        }
    return output

with open(dir_file,"r") as f: # Accessing directory wordlist,calling the check function and displaying the headers for user to analyze
    for directory in f.readlines():
        url=f"https://{target.strip()}/{directory.strip()}"
        value=chk_url(url)
        URL=value["url"]
        SC=value["Status-Code"]
        CLEN=value["Content-length"]
        print(f"URL:{URL},Status Code:{SC},Body length:{CLEN}")
        
