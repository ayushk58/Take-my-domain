import requests
import sys
import time
import urllib
import os
import colorama
import subprocess
import optparse
import argparse

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   B = '\033[94m'
   G = '\033[92m'
   Y = '\033[93m'
   R = '\033[91m'
   BOLD = '\033[1m'
   W = '\033[0m' 
   END = '\033[0m'



def banner():
    print("""
===================================================== %s            
             ________              ____      
            |__    __|            |    \    
               |  |    __    __   | |\  \    
               |  |   |  \  /  |  | | |  |      
               |  |   | | \/ | |  | |/  /     
               |__|   |_|    |_|  |____/%s

            #Created by Ayush(LuciferXn)%s   

            #Domain Enumeration tool: Sublist3r
=====================================================          
    """ %  (color.Y , color.R, color.W) )


def banner2():
    print(color.BOLD+"\n[+] List Compiled\n"+color.END)
    time.sleep(1)
    print(color.BOLD+"[+] Waking up Servers\n"+color.END)
    time.sleep(1)
    print(color.BOLD+"[+] Starting Query\n\n"+color.END)
    time.sleep(1)


def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    parser=argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d google.com")
    parser.error= parser_error
    parser._optionals.title="OPTIONS"
    parser.add_argument('-u','--url',help="The domain of which you want to find the subdomains for")
    parser.add_argument('-o','--output',help="Outputs the deatils to the file")
    parser.add_argument('-c','--choice',help="Use 1 if only want to use it on a given list",default=0)
    return parser.parse_args()


def domain_finder(domain,file):
    subprocess.check_call(['python3','sublist3r.py','-d', domain,'-o',file])
    banner2()
    takeover_check(file)
    
def takeover_check(file):
    subdomain=open(file,'r')
    print("""
%s
    %sSITE DOMAIN\t\t\t\t\tSTATUS CODE\t\t\t\t\t  SERVER%s

        %s""" % (color.BOLD,color.B,color.Y,color.END))
    for url in subdomain:
        url=('https://'+url).strip("\n")
        try:
            status=requests.get(url)
            code=(status.status_code)
            if(code==404):
                print(color.R+url+"\t\t\t   "+color.BOLD+str(code)+"\t\t\t\t\t\t"+status.headers['server']+color.END+"\n")
            else:
                print(color.G+url+"\t\t\t   "+color.BOLD+str(code)+"\t\t\t\t\t\t"+status.headers['server']+color.END+"\n")
        except requests.exceptions.RequestException:
            print(color.Y+url+"\t\t\t   "+color.BOLD+"ERROR"+"\t\t\t\t\t"+"ERROR"+"\n"+color.END)

            

def console():
    banner()
    args=parse_args()
    domain=args.url
    file=str(args.output)
    choice=args.choice
    if '.txt' not in file:
        file=file+'.txt'
    else:
        file=file
    if choice==0:
        domain_finder(domain,file)
    else:
        takeover_check(file)
        

if __name__=="__main__":
    console()
    
