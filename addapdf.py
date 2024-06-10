import requests
import subprocess

def download(cmd):
    print(cmd)
    dl = subprocess.run(cmd, shell=True)
    return dl.returncode

def addaTokens():
    r = requests.get("https://raw.githubusercontent.com/Arvind0099/fdggididisjnabe/main/shdjshds.txt").text
    return reversed(r.split("\n"))

adda_c = None
failed_counter = 0

def download_adda_pdfs(name, link):
    global adda_c
    global failed_counter
    adda_pdf_cmd = 'aria2c "{link}" --header "cookie: {cook}" -o "{name}.pdf"'
    if failed_counter == 2:
        failed_counter = 0  #Reset Counter
        return 1
    if not adda_c:
        for i in addaTokens():
            if not i.startswith("eyJhbGciOiJIUzUxMiJ9"):
                continue
            cook = f"cp_token={i};cp_user_email=anjalisachan907@gmail.com;cp_user_name=Anjali%20Sachan"
            cmd = adda_pdf_cmd.format(link=link, name=name, cook=cook)
            if download(cmd) == 0:
                adda_c = cook
                break
            else:
                continue
    cmd = adda_pdf_cmd.format(link=link, name=name, cook=adda_c)
    dl = download(cmd)
    if dl != 0:
        failed_counter +=1
        adda_c = None
        download_adda_pdfs(name, link)
    return dl
