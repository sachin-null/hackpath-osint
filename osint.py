#!/usr/bin/env python3
# ============================================================
#   HACKPATH OSINT TOOL v2
#   Created by: Sachin Ser | HackPath
#   Works on: Termux | Linux | Kali
#   Run: python3 osint.py
#   No extra install needed — Pure Python!
#   GitHub: github.com/sachin-null/hackpath-osint
# ============================================================

import os,sys,json,socket,urllib.request,urllib.parse,urllib.error,re,time

class C:
    R='\033[91m';G='\033[92m';Y='\033[93m'
    B='\033[94m';M='\033[95m';CY='\033[96m'
    W='\033[97m';DIM='\033[2m';X='\033[0m';BOLD='\033[1m'

def clear(): os.system('clear' if os.name!='nt' else 'cls')

def banner():
    clear()
    print(C.CY+C.BOLD)
    print("  ___  ___ ___ _  _ _____    _____ ___   ___  _")
    print(" / _ \\/ __|_ _| \\| |_   _|  |_   _/ _ \\ / _ \\| |")
    print("| (_) \\__ \\| || .` | | |      | || (_) | (_) | |__")
    print(" \\___/|___/___|_|\\_| |_|      |_| \\___/ \\___/|____|")
    print(C.X)
    print(C.CY+" +------------------------------------------+")
    print(" |  "+C.CY+C.BOLD+"OSINT TOOL v2"+C.CY+"  .  "+C.Y+"Sachin Ser"+C.CY+"            |")
    print(" |  "+C.DIM+"HackPath | Termux . Linux . Kali"+C.CY+"        |")
    print("  |  "+C.R+"Educational / Authorized use only!"+C.CY+"     |")
    print(" +------------------------------------------+"+C.X)
    print()

def sep(t=""):
    if t: print(f"\n{C.CY}{'='*14} {C.Y}{t}{C.CY} {'='*14}{C.X}")
    else: print(f"{C.DIM}{'-'*50}{C.X}")

def ok(m):    print(f"{C.G}[+] {m}{C.X}")
def err(m):   print(f"{C.R}[-] {m}{C.X}")
def inf(m):   print(f"{C.CY}[*] {m}{C.X}")
def fld(k,v): print(f"  {C.Y}{k:<22}{C.X}: {C.W}{v}{C.X}")
def pause():  input(f"\n{C.DIM}Press Enter...{C.X}")
def inp(p):   return input(f"{C.CY}  {p} > {C.X}").strip()

def fetch(url,timeout=8):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=timeout) as r:
            return json.loads(r.read().decode())
    except: return None

def fetch_text(url,timeout=8):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=timeout) as r:
            return r.read().decode(errors='replace')
    except: return None

# ══════════════════════════════════════════
#   1. MY IP INFO
# ══════════════════════════════════════════
def my_ip():
    sep("MY IP INFO")
    inf("Fetching your IP...")
    data=fetch("http://ip-api.com/json/?fields=status,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query,mobile,proxy,hosting")
    if not data:
        data=fetch("https://ipapi.co/json/")
    if not data:
        err("No internet!"); pause(); return
    fld("IP",           data.get('query',data.get('ip','N/A')))
    fld("Country",      data.get('country',data.get('country_name','N/A')))
    fld("Region",       data.get('regionName',data.get('region','N/A')))
    fld("City",         data.get('city','N/A'))
    fld("Postal",       data.get('zip',data.get('postal','N/A')))
    fld("Latitude",     str(data.get('lat',data.get('latitude','N/A'))))
    fld("Longitude",    str(data.get('lon',data.get('longitude','N/A'))))
    fld("Timezone",     data.get('timezone','N/A'))
    fld("ISP",          data.get('isp','N/A'))
    fld("Org",          data.get('org','N/A'))
    fld("ASN",          data.get('as',data.get('asn','N/A')))
    fld("Mobile",       str(data.get('mobile','N/A')))
    fld("Proxy/VPN",    str(data.get('proxy','N/A')))
    lat=data.get('lat',data.get('latitude',''))
    lon=data.get('lon',data.get('longitude',''))
    if lat and lon:
        print(f"\n  {C.CY}Maps:{C.X} https://maps.google.com/?q={lat},{lon}")
    pause()

# ══════════════════════════════════════════
#   2. IP LOOKUP
# ══════════════════════════════════════════
def ip_lookup():
    sep("IP ADDRESS LOOKUP")
    ip=inp("Enter IP address")
    if not ip: err("Empty!"); pause(); return
    if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',ip):
        err("Invalid IP!"); pause(); return
    inf(f"Looking up {ip}...")
    data=fetch(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
    if not data or data.get('status')=='fail':
        data=fetch(f"https://ipapi.co/{ip}/json/")
    if not data: err("Lookup failed!"); pause(); return
    ok(f"Results for: {C.Y}{ip}")
    fld("IP",           data.get('query',data.get('ip','N/A')))
    fld("Continent",    data.get('continent','N/A'))
    fld("Country",      data.get('country',data.get('country_name','N/A')))
    fld("Country Code", data.get('countryCode',data.get('country_code','N/A')))
    fld("Region",       data.get('regionName',data.get('region','N/A')))
    fld("City",         data.get('city','N/A'))
    fld("ZIP",          data.get('zip',data.get('postal','N/A')))
    fld("Latitude",     str(data.get('lat',data.get('latitude','N/A'))))
    fld("Longitude",    str(data.get('lon',data.get('longitude','N/A'))))
    fld("Timezone",     data.get('timezone','N/A'))
    fld("ISP",          data.get('isp','N/A'))
    fld("Org",          data.get('org','N/A'))
    fld("ASN",          data.get('as',data.get('asn','N/A')))
    fld("Reverse DNS",  data.get('reverse','N/A'))
    fld("Mobile",       str(data.get('mobile','N/A')))
    fld("Proxy/VPN",    str(data.get('proxy','N/A')))
    fld("Hosting",      str(data.get('hosting','N/A')))
    lat=data.get('lat',data.get('latitude',''))
    lon=data.get('lon',data.get('longitude',''))
    if lat and lon:
        print(f"\n  {C.CY}Maps:{C.X} https://maps.google.com/?q={lat},{lon}")
    if inp("\nSave? [y/N]").lower()=='y':
        fname=f"ip_{ip.replace('.','_')}.txt"
        with open(fname,'w') as f:
            for k,v in data.items(): f.write(f"{k}: {v}\n")
        ok(f"Saved → {fname}")
    pause()

# ══════════════════════════════════════════
#   3. DOMAIN INFO
# ══════════════════════════════════════════
def domain_info():
    sep("DOMAIN INFORMATION")
    domain=inp("Enter domain (e.g. google.com)")
    domain=domain.replace('http://','').replace('https://','').split('/')[0].strip()
    if not domain: err("Empty!"); pause(); return
    inf(f"Analyzing: {domain}")

    # DNS resolve
    try:
        ip=socket.gethostbyname(domain)
        fld("Domain",    domain)
        fld("IP Address",ip)
        ok("Domain resolves!")
    except:
        err("DNS resolution failed!")
        fld("Domain",domain)

    # IP location
    try:
        ip=socket.gethostbyname(domain)
        data=fetch(f"http://ip-api.com/json/{ip}")
        if data and data.get('status')!='fail':
            sep("SERVER INFO")
            fld("Country",   data.get('country','N/A'))
            fld("City",      data.get('city','N/A'))
            fld("ISP",       data.get('isp','N/A'))
            fld("Org",       data.get('org','N/A'))
    except: pass

    # DNS records
    sep("DNS RECORDS")
    for dtype in ['A','MX','NS','TXT','CNAME','AAAA']:
        try:
            data=fetch(f"https://dns.google/resolve?name={domain}&type={dtype}")
            if data and data.get('Answer'):
                answers=[a.get('data','') for a in data['Answer']]
                fld(dtype,', '.join(str(a) for a in answers[:2])[:60])
            else:
                print(f"  {C.DIM}{dtype:<8}: Not found{C.X}")
        except:
            print(f"  {C.DIM}{dtype:<8}: Error{C.X}")

    # HTTP headers
    sep("HTTP HEADERS")
    for scheme in ['https','http']:
        try:
            req=urllib.request.Request(f"{scheme}://{domain}",headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=5) as r:
                h=dict(r.headers)
                for hdr in ['Server','X-Powered-By','Content-Type','X-Frame-Options','Strict-Transport-Security','X-Content-Type-Options']:
                    val=h.get(hdr,h.get(hdr.lower(),'—'))
                    if val!='—': fld(hdr,str(val)[:55])
                break
        except: continue

    # Quick checks
    sep("QUICK CHECKS")
    checks=[
        (f"https://{domain}/robots.txt",    "robots.txt"),
        (f"https://{domain}/sitemap.xml",   "sitemap.xml"),
        (f"https://{domain}/admin",         "/admin"),
        (f"https://{domain}/.git/HEAD",     "/.git exposed"),
        (f"https://{domain}/wp-login.php",  "WordPress login"),
        (f"https://{domain}/phpmyadmin",    "phpMyAdmin"),
    ]
    for url,label in checks:
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=4) as r:
                code=r.getcode()
                if code==200: print(f"  {C.G}✓ {label:<25}{C.X} {C.Y}Found! ({code}){C.X}")
                else: print(f"  {C.DIM}✗ {label:<25} ({code}){C.X}")
        except urllib.error.HTTPError as e:
            print(f"  {C.DIM}✗ {label:<25} ({e.code}){C.X}")
        except: print(f"  {C.DIM}✗ {label:<25} (timeout){C.X}")

    print(f"\n  {C.CY}Shodan:{C.X}    https://shodan.io/search?query={domain}")
    print(f"  {C.CY}VirusTotal:{C.X} https://virustotal.com/gui/domain/{domain}")
    print(f"  {C.CY}Whois:{C.X}      https://who.is/whois/{domain}")
    pause()

# ══════════════════════════════════════════
#   4. DNS LOOKUP
# ══════════════════════════════════════════
def dns_lookup():
    sep("DNS LOOKUP")
    target=inp("Enter domain or IP")
    if not target: err("Empty!"); pause(); return
    try:
        ip=socket.gethostbyname(target)
        fld("Forward DNS",f"{target} → {ip}")
    except: fld("Forward DNS","Failed")
    try:
        host=socket.gethostbyaddr(target)
        fld("Reverse DNS",f"{target} → {host[0]}")
    except: fld("Reverse DNS","Not found")

    sep("ALL RECORDS")
    for rtype in ['A','AAAA','MX','NS','TXT','CNAME','SOA','PTR','SRV']:
        try:
            data=fetch(f"https://dns.google/resolve?name={target}&type={rtype}",timeout=5)
            if data and data.get('Answer'):
                for ans in data['Answer'][:2]:
                    fld(rtype,str(ans.get('data',''))[:65])
            else:
                print(f"  {C.DIM}{rtype:<8}: Not found{C.X}")
        except: print(f"  {C.DIM}{rtype:<8}: Error{C.X}")
    pause()

# ══════════════════════════════════════════
#   5. PORT SCANNER
# ══════════════════════════════════════════
def port_scanner():
    sep("PORT SCANNER")
    target=inp("Enter IP or domain")
    if not target: err("Empty!"); pause(); return
    print(f"\n  {C.G}[1]{C.X} Top 20 ports  {C.G}[2]{C.X} Custom  {C.G}[3]{C.X} Top 100")
    choice=inp("Choice")

    common={21:'FTP',22:'SSH',23:'Telnet',25:'SMTP',53:'DNS',
            80:'HTTP',110:'POP3',143:'IMAP',443:'HTTPS',445:'SMB',
            3306:'MySQL',3389:'RDP',5900:'VNC',8080:'HTTP-Alt',
            8443:'HTTPS-Alt',27017:'MongoDB',6379:'Redis',
            5432:'PostgreSQL',1433:'MSSQL',11211:'Memcached'}
    top100=[21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,
            1723,3306,3389,5900,8080,8443,9090,9200,27017,6379,
            5432,1433,8888,2181,4848,7001,9000,8161,2375,5000,
            5001,8500,9092,2379,10250,6443,2049,5901,8009,8020,
            9001,7000,7002,4567,9043,10000,10001,8888,3000,4000,
            4444,5555,6666,7777,8888,9999,1080,3128,8118,8888]

    if choice=='1':   ports=common
    elif choice=='2':
        raw=inp("Ports (e.g. 80,443,8080)")
        try: ports={int(p.strip()):'Custom' for p in raw.split(',')}
        except: err("Invalid!"); pause(); return
    elif choice=='3': ports={p:'Service' for p in top100}
    else: err("Invalid!"); pause(); return

    inf(f"Scanning {len(ports)} ports on {target}...")
    open_ports=[]
    for port,service in ports.items():
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((target,port))==0:
                print(f"  {C.G}[OPEN]{C.X}   {C.Y}{port:<6}{C.X} {C.W}{service}{C.X}")
                open_ports.append(port)
            s.close()
        except KeyboardInterrupt: break
        except: pass

    sep("SUMMARY")
    fld("Target",       target)
    fld("Scanned",      str(len(ports)))
    fld("Open",         str(len(open_ports)))
    if open_ports:
        fld("Open ports",   str(open_ports))
        print(f"\n  {C.CY}Nmap verify:{C.X} nmap -sV -p {','.join(map(str,open_ports))} {target}")
    pause()

# ══════════════════════════════════════════
#   6. EMAIL HEADER ANALYZER
# ══════════════════════════════════════════
def email_header():
    sep("EMAIL HEADER ANALYZER")
    print(f"{C.DIM}  Paste headers (empty line to finish):{C.X}\n")
    lines=[]
    while True:
        try:
            l=input()
            if not l.strip(): break
            lines.append(l)
        except EOFError: break
    if not lines: err("No headers!"); pause(); return
    text='\n'.join(lines)

    # Extract info
    ips=list(set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)))
    ips=[ip for ip in ips if not ip.startswith(('127.','192.168.','10.','172.'))]
    emails=list(set(re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+',text)))
    domains=list(set(re.findall(r'(?:from|by)\s+([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',text,re.I)))

    sep("EXTRACTED")
    fld("IPs",     ', '.join(ips[:5]) if ips else 'None')
    fld("Emails",  ', '.join(emails[:3]) if emails else 'None')
    fld("Domains", ', '.join(domains[:3]) if domains else 'None')

    sep("SECURITY CHECKS")
    checks=[
        ('Received-SPF: fail' in text,   "SPF FAIL"),
        ('DKIM=fail' in text,            "DKIM FAIL"),
        ('X-Spam-Status: Yes' in text,   "Marked as SPAM"),
        (len(ips)>3,                     "Multiple IPs (relay chain)"),
        ('@' in text and 'Received:' not in text,"Missing Received header"),
    ]
    for bad,msg in checks:
        if bad: print(f"  {C.R}⚠ {msg}{C.X}")
        else:   print(f"  {C.G}✓ {msg} OK{C.X}")

    if ips:
        inf(f"Looking up: {ips[0]}")
        data=fetch(f"http://ip-api.com/json/{ips[0]}")
        if data:
            fld("Sender Country",data.get('country','N/A'))
            fld("Sender ISP",    data.get('isp','N/A'))
    pause()

# ══════════════════════════════════════════
#   7. URL ANALYZER
# ══════════════════════════════════════════
def url_analyzer():
    sep("URL ANALYZER")
    url=inp("Enter URL")
    if not url: err("Empty!"); pause(); return
    if not url.startswith('http'): url='https://'+url
    p=urllib.parse.urlparse(url)
    domain=p.netloc; path=p.path; params=p.query

    sep("URL BREAKDOWN")
    fld("Protocol",   p.scheme)
    fld("Domain",     domain)
    fld("Path",       path if path else '/')
    fld("Parameters", params if params else 'None')
    fld("Fragment",   p.fragment if p.fragment else 'None')

    sep("SAFETY CHECK")
    flags=[]
    if re.match(r'\d+\.\d+\.\d+\.\d+',domain):
        flags.append(("IP instead of domain!",C.R))
    sus=['login','signin','account','verify','secure','update','confirm',
         'bank','paypal','amazon','apple','microsoft','suspended','urgent']
    found=[w for w in sus if w in url.lower()]
    if found: flags.append((f"Suspicious keywords: {', '.join(found)}",C.Y))
    if len(url)>100: flags.append((f"Long URL ({len(url)} chars)",C.Y))
    if len(domain.split('.'))>4: flags.append(("Many subdomains",C.Y))
    if p.scheme!='https': flags.append(("HTTP only — NOT encrypted!",C.R))
    if '%' in url: flags.append(("URL encoded chars",C.Y))
    if '@' in domain: flags.append(("@ in URL — redirect trick!",C.R))

    for msg,color in flags:
        print(f"  {color}⚠ {msg}{C.X}")
    if not flags: print(f"  {C.G}✓ No obvious phishing indicators{C.X}")

    risk=len([f for f in flags if f[1]==C.R])
    if risk==0:   r=f"{C.G}LOW RISK ✅{C.X}"
    elif risk<=1: r=f"{C.Y}MEDIUM RISK ⚠️{C.X}"
    else:         r=f"{C.R}HIGH RISK 🚨{C.X}"
    print(f"\n  Risk: {r}")
    print(f"\n  {C.CY}VirusTotal:{C.X} https://virustotal.com/gui/url/{urllib.parse.quote(url)}")
    pause()

# ══════════════════════════════════════════
#   8. SUBDOMAIN FINDER
# ══════════════════════════════════════════
def subdomain_finder():
    sep("SUBDOMAIN FINDER")
    domain=inp("Enter base domain (e.g. example.com)")
    if not domain: err("Empty!"); pause(); return

    common_subs=['www','mail','ftp','admin','api','dev','test','staging',
                 'app','mobile','m','blog','shop','store','portal','vpn',
                 'remote','ns1','ns2','smtp','pop','imap','cpanel','whm',
                 'webmail','forum','support','help','docs','cdn','static',
                 'assets','media','img','images','secure','login','auth',
                 'dashboard','panel','git','gitlab','github','jenkins',
                 'ci','jira','confluence','wiki','status','monitor',
                 'grafana','kibana','elastic','mysql','db','database']

    inf(f"Checking {len(common_subs)} subdomains for {domain}...")
    found=[]
    for sub in common_subs:
        full=f"{sub}.{domain}"
        try:
            ip=socket.gethostbyname(full)
            print(f"  {C.G}✓ {full:<40}{C.X} {C.Y}{ip}{C.X}")
            found.append((full,ip))
        except:
            print(f"  {C.DIM}✗ {full}{C.X}")

    sep("FOUND")
    ok(f"{len(found)} subdomains found!")
    if found:
        print(f"\n  {C.CY}Subdomains:{C.X}")
        for sub,ip in found:
            print(f"  {C.W}{sub}{C.X} → {C.Y}{ip}{C.X}")

    if found and inp("\nSave? [y/N]").lower()=='y':
        fname=f"subdomains_{domain}.txt"
        with open(fname,'w') as f:
            for sub,ip in found: f.write(f"{sub} → {ip}\n")
        ok(f"Saved → {fname}")
    pause()

# ══════════════════════════════════════════
#   9. WHOIS LOOKUP
# ══════════════════════════════════════════
def whois_lookup():
    sep("WHOIS LOOKUP")
    domain=inp("Enter domain")
    if not domain: err("Empty!"); pause(); return

    inf(f"Checking WHOIS for {domain}...")

    # Try WHOIS via RDAP (free, no library needed)
    data=fetch(f"https://rdap.org/domain/{domain}")
    if data:
        sep("DOMAIN INFO")
        fld("Name",       data.get('ldhName',domain))
        fld("Status",     ', '.join(data.get('status',[])))

        events=data.get('events',[])
        for ev in events:
            action=ev.get('eventAction','')
            date=ev.get('eventDate','')[:10]
            if 'registration' in action: fld("Registered",date)
            if 'expiration' in action:   fld("Expires",date)
            if 'last changed' in action: fld("Updated",date)

        entities=data.get('entities',[])
        for ent in entities:
            vcards=ent.get('vcardArray',[])
            if len(vcards)>1:
                for v in vcards[1]:
                    if v[0]=='fn': fld("Registrant",v[3])
                    if v[0]=='org': fld("Organization",v[3])
                    if v[0]=='email': fld("Email",v[3])
    else:
        inf("RDAP failed, try online:")
        print(f"\n  {C.CY}WHOIS online:{C.X}")
        print(f"  {C.W}https://who.is/whois/{domain}{C.X}")
        print(f"  {C.W}https://whois.domaintools.com/{domain}{C.X}")
        print(f"  {C.W}https://www.whois.com/whois/{domain}{C.X}")
    pause()

# ══════════════════════════════════════════
#   10. GOOGLE DORKS
# ══════════════════════════════════════════
def google_dorks():
    sep("GOOGLE DORKS GENERATOR")
    target=inp("Enter domain or keyword")
    if not target: err("Empty!"); pause(); return

    sep("GENERATED DORKS")
    dorks=[
        (f'site:{target}',                           "All indexed pages"),
        (f'site:{target} inurl:admin',               "Admin pages"),
        (f'site:{target} intitle:login',             "Login pages"),
        (f'site:{target} filetype:pdf',              "PDF files"),
        (f'site:{target} filetype:xls OR filetype:xlsx',"Excel files"),
        (f'site:{target} filetype:doc OR filetype:docx',"Word files"),
        (f'site:{target} filetype:sql',              "SQL files"),
        (f'site:{target} filetype:log',              "Log files"),
        (f'site:{target} inurl:config',              "Config files"),
        (f'site:{target} inurl:backup',              "Backup files"),
        (f'site:{target} inurl:password',            "Password pages"),
        (f'site:{target} inurl:api',                 "API endpoints"),
        (f'site:{target} "index of"',                "Directory listings"),
        (f'site:{target} intext:"error" OR intext:"exception"',"Error pages"),
        (f'"{target}" email OR contact',             "Contact info"),
        (f'"{target}" site:pastebin.com',            "Pastebin leaks"),
        (f'"{target}" site:github.com',              "GitHub mentions"),
        (f'inurl:{target} filetype:env',             ".env files"),
    ]

    for dork,desc in dorks:
        print(f"  {C.Y}{desc:<30}{C.X}")
        print(f"  {C.W}{dork}{C.X}")
        enc=urllib.parse.quote(dork)
        print(f"  {C.DIM}https://google.com/search?q={enc}{C.X}\n")

    if inp("Copy all to file? [y/N]").lower()=='y':
        fname=f"dorks_{target.replace('.','_')}.txt"
        with open(fname,'w') as f:
            for dork,desc in dorks:
                f.write(f"# {desc}\n{dork}\n\n")
        ok(f"Saved → {fname}")
    pause()

# ══════════════════════════════════════════
#   MAIN MENU
# ══════════════════════════════════════════
def main():
    while True:
        banner()
        print(f"  {C.BOLD}MENU{C.X}\n")
        print(f"  {C.CY}[1]{C.X}  My IP Info")
        print(f"  {C.CY}[2]{C.X}  IP Address Lookup")
        print(f"  {C.CY}[3]{C.X}  Domain Information")
        print(f"  {C.CY}[4]{C.X}  DNS Lookup")
        print(f"  {C.CY}[5]{C.X}  Port Scanner")
        print(f"  {C.CY}[6]{C.X}  Email Header Analyzer")
        print(f"  {C.CY}[7]{C.X}  URL Analyzer")
        print(f"  {C.CY}[8]{C.X}  Subdomain Finder  {C.G}★ NEW{C.X}")
        print(f"  {C.CY}[9]{C.X}  WHOIS Lookup      {C.G}★ NEW{C.X}")
        print(f"  {C.CY}[10]{C.X} Google Dorks      {C.G}★ NEW{C.X}")
        print(f"  {C.R}[0]{C.X}  Exit\n")
        print(f"{C.DIM}  python3 osint.py | HackPath v2{C.X}\n")

        ch=input(f"{C.CY}HackPath OSINT > {C.X}").strip()
        menu={'1':my_ip,'2':ip_lookup,'3':domain_info,'4':dns_lookup,
              '5':port_scanner,'6':email_header,'7':url_analyzer,
              '8':subdomain_finder,'9':whois_lookup,'10':google_dorks}
        if ch in menu: menu[ch]()
        elif ch=='0':
            print(f"\n{C.CY}Bye! 👋{C.X}\n"); sys.exit(0)
        else: print(f"{C.R}Invalid!{C.X}")

if __name__=='__main__':
    try: main()
    except KeyboardInterrupt:
        print(f"\n\n{C.CY}Bye! 👋{C.X}\n"); sys.exit(0)
