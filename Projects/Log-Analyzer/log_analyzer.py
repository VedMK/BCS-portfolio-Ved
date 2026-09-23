print("TXT file must be in csv format-> DATE/DATETIME/TIME,IP,USER,STATUS")
file=input("Enter file name or type default to use sample log.txt")


def check_ip(file):
    try:
        with open(file) as f:
            failed_ip={}
            for line in f.readlines():
                line=line.strip()
                if not line:
                    continue
                log=line.split(",")
                if len(log)==4:
                    if log[3].strip().lower()=="failed":
                        failed_ip[log[1]]=failed_ip.get(log[1],0)+1
                else:
                    print(f"Log at '{line}' was in incorrect format and was skipped")
            return failed_ip
    except FileNotFoundError:
        print("That file doesn't exist, exitting.")
        exit()


def sus_ips(failed_ips):
    sus_ips=[]
    if len(failed_ips)==0:
        print("No ip found in failed_ips")
        exit()
    else:
        for ip in failed_ips:
            if failed_ips[ip]>=5:
                sus_ips.append(ip)
        if len(sus_ips)==0:
            print("No suspicious IPs detected")
            exit()
        else:
            return sus_ips



if file.strip()=="default":
    file="log.txt"
    failed_ips=check_ip(file)
    sus_ips=sus_ips(failed_ips)
    for ip in sus_ips:
        print(f"The ip at {ip} is suspicious with 5 or more failed log-in attempts")
else:
    file=file+".txt"
    failed_ips=check_ip(file)
    sus_ips=sus_ips(failed_ips)
    for ip in sus_ips:
        print(f"The ip at {ip} is suspicious with 5 or more failed log-in attempts")
