# Take-my-domain
A Subdomain enumeration tool, that uses open source tool "Sublist3r" to find a list of domains and use python to find the server and whether the sub-domain can be take over


Ever frustated while checking for sub-domain takeover ??

Using SubF1nd3r, You can now get access to the server satus code along with the servers that host the site, which will save you a lot of time by not making you visit each and every sub-domain.

![test](https://user-images.githubusercontent.com/77789017/120081660-9f0de180-c0b6-11eb-9b9c-12c1a4a8477a.png)


USAGE:

For enumerating a domain and finding the server status
```
python3 SubF1nd3r.py -u example.com -o example.txt 

```

For enumerating a already given file containing the list of sub-domains

```
python3 SubF1nd3r.py -o file.txt --choice/-c 1

Using 1 as choice will let the program know that the file already exists and it will skip the enumeration part
```
