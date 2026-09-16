import requests as req # requests library is a requirement, ensure you have it installed using pip install requests

target=input("Insert domain name/ip-address here")
dir_file="directories.txt"
def chk_url(url): # Checking response headers

    try:
        response = req.get(url, timeout=5)
        output = {
            "url": url,
            "SC": response.status_code,
            "Clen": len(response.content)
        }
        return output
    except req.exceptions.Timeout:
        print(f"Timedout at: {url}")
        return None
    except req.exceptions.RequestException as error:
        print(f"Error at: {url} -> {error}")
        return None

with open(dir_file,"r") as f: # Accessing directory wordlist,calling the check function and displaying the headers for user to analyze
    for directory in f.readlines():
        url=f"https://{target.strip()}/{directory.strip()}"
        value=chk_url(url)
        URL=value["url"]
        SC=value["Status-Code"]
        CLEN=value["Content-length"]
        print(f"URL:{URL},Status Code:{SC},Body length:{CLEN}")
        
