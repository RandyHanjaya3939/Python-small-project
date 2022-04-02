from datetime import date, datetime, time

end_time = datetime(2021,1,1,20)

blocksites = ['www.facebook.com','facebook.com']

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect ="127.0.0.1"

def block():
    if datetime.now() < end_time:
        print("Block sites")
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in blocksites:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")

    else:
        print("unblock site")
        with open(hosts_path, 'r+') as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in blocksites):
                    hostsfile.write(line)
            hostsfile.truncate()

if __name__ == "__main__":
    block()