import json

new_tools = [
    # Info Gathering
    ('nmap', 'Nmap', 'Network exploration tool and security / port scanner', 'infogathering'),
    ('zenmap', 'Zenmap', 'Official Nmap Security Scanner GUI', 'infogathering'),
    ('dnsenum', 'dnsenum', 'Performs DNS enumeration', 'infogathering'),
    ('dnsrecon', 'dnsrecon', 'DNS Enumeration Script', 'infogathering'),
    ('fierce', 'Fierce', 'DNS reconnaissance tool', 'infogathering'),
    ('maltego', 'Maltego', 'Open source intelligence and forensics application', 'infogathering'),
    ('netcat', 'Netcat', 'Networking utility for reading/writing network connections', 'infogathering'),
    ('recon-ng', 'Recon-ng', 'Web Reconnaissance framework', 'infogathering'),
    ('theHarvester', 'theHarvester', 'E-mail, IPv4/IPv6, subdomain and open ports scanner', 'infogathering'),
    ('whois', 'Whois', 'Intelligent WHOIS client', 'infogathering'),
    ('hping3', 'hping3', 'Active Network Smashing Tool', 'infogathering'),
    ('spiderfoot', 'SpiderFoot', 'Automated OSINT reconnaissance', 'infogathering'),
    
    # Vuln Analysis
    ('lynis', 'Lynis', 'Security auditing tool', 'vulnanalysis'),
    ('nikto', 'Nikto', 'Web server scanner', 'vulnanalysis'),
    ('openvas', 'OpenVAS', 'Open Vulnerability Assessment System', 'vulnanalysis'),
    ('unix-privesc-check', 'Unix-Privesc-Check', 'Script to check for simple privilege escalation vectors', 'vulnanalysis'),
    ('wpscan', 'WPScan', 'WordPress vulnerability scanner', 'vulnanalysis'),
    ('skipfish', 'Skipfish', 'Active web application security reconnaissance tool', 'vulnanalysis'),
    ('wapiti', 'Wapiti', 'Web application vulnerability scanner', 'vulnanalysis'),
    ('sslyze', 'SSLyze', 'Fast and powerful SSL/TLS scanning library', 'vulnanalysis'),
    
    # Web Apps
    ('burpsuite', 'Burp Suite', 'Web vulnerability scanner', 'webapps'),
    ('commix', 'Commix', 'Automated All-in-One OS Command Injection and Exploitation Tool', 'webapps'),
    ('dirb', 'DIRB', 'URL Bruteforcer', 'webapps'),
    ('dirbuster', 'DirBuster', 'Web directory brute-forcer', 'webapps'),
    ('gobuster', 'Gobuster', 'Directory/File, DNS and VHost busting tool written in Go', 'webapps'),
    ('sqlmap', 'sqlmap', 'Automatic SQL injection and database takeover tool', 'webapps'),
    ('zaproxy', 'ZAP', 'OWASP Zed Attack Proxy', 'webapps'),
    ('davtest', 'DAVTest', 'Tests WebDAV enabled servers', 'webapps'),
    
    # Wireless
    ('aircrack-ng', 'Aircrack-ng', 'WiFi security auditing tools suite', 'wireless'),
    ('kismet', 'Kismet', 'Wireless network and device detector', 'wireless'),
    ('mdk4', 'MDK4', 'Wi-Fi penetration testing tool', 'wireless'),
    ('bully', 'Bully', 'Retrieve WPA/WPA2 passphrase from a WPS enabled access point', 'wireless'),
    ('pixiewps', 'Pixiewps', 'Offline Wi-Fi Protected Setup brute force utility', 'wireless'),
    ('reaver', 'Reaver', 'Brute force attack against Wifi Protected Setup', 'wireless'),
    ('fern-wifi-cracker', 'Fern WiFi Cracker', 'Wireless security auditing and attack software', 'wireless'),
    ('cowpatty', 'coWPAtty', 'Brute-force dictionary attack against WPA-PSK', 'wireless'),
    
    # Exploitation
    ('metasploit-framework', 'Metasploit', 'Penetration testing framework', 'exploitation'),
    ('armitage', 'Armitage', 'Graphical cyber attack management tool for Metasploit', 'exploitation'),
    ('routersploit', 'RouterSploit', 'Exploitation Framework for Embedded Devices', 'exploitation'),
    ('searchsploit', 'SearchSploit', 'Command line search tool for Exploit-DB', 'exploitation'),
    ('beef-xss', 'BeEF', 'Browser Exploitation Framework', 'exploitation'),
    ('the-backdoor-factory', 'Backdoor Factory', 'Patch PE, ELF, Mach-O binaries with shellcode', 'exploitation'),
    ('veil', 'Veil', 'Tool designed to generate metasploit payloads', 'exploitation'),
    
    # Password
    ('john', 'John the Ripper', 'Password cracker', 'password'),
    ('hashcat', 'Hashcat', 'World\'s fastest and most advanced password recovery utility', 'password'),
    ('hydra', 'Hydra', 'Network logon cracker', 'password'),
    ('cewl', 'CeWL', 'Custom Word List generator', 'password'),
    ('crunch', 'Crunch', 'Wordlist generator', 'password'),
    ('fcrackzip', 'fcrackzip', 'Free/Fast ZIP password cracker', 'password'),
    ('ophcrack', 'Ophcrack', 'Windows password cracker based on rainbow tables', 'password'),
    ('pdfcrack', 'PDFCrack', 'Password recovery tool for PDF-files', 'password'),
    ('rcrack', 'rcrack', 'Rainbow table crack', 'password'),
    ('wordlists', 'Wordlists', 'Collection of wordlists', 'password'),
    ('steghide', 'Steghide', 'Steganography program', 'password'),
    ('outguess', 'OutGuess', 'Universal steganographic tool', 'password'),
    
    # Forensics
    ('autopsy', 'Autopsy', 'Digital forensics platform', 'forensics'),
    ('binwalk', 'Binwalk', 'Firmware analysis tool', 'forensics'),
    ('bulk_extractor', 'bulk_extractor', 'Extracts information without parsing the file system', 'forensics'),
    ('chntpw', 'chntpw', 'Offline NT Password & Registry Editor', 'forensics'),
    ('forensics-samples', 'Forensics Samples', 'Forensics samples', 'forensics'),
    ('galleta', 'Galleta', 'Internet Explorer Cookie Forensic Analysis Tool', 'forensics'),
    ('guymager', 'Guymager', 'Forensic imager for media acquisition', 'forensics'),
    ('pff-tools', 'pff-tools', 'Tools to access the Personal Folder File format', 'forensics'),
    ('sleuthkit', 'The Sleuth Kit', 'Library and collection of command line digital forensics tools', 'forensics'),
    ('bluez', 'BlueZ', 'Official Linux Bluetooth protocol stack', 'forensics'),
    ('rfidiot', 'RFIDiot', 'RFID exploration tools', 'forensics'),
    
    # Sniffing
    ('wireshark', 'Wireshark', 'Network protocol analyzer', 'sniffing'),
    ('tshark', 'TShark', 'Network protocol analyzer (Terminal)', 'sniffing'),
    ('bettercap', 'bettercap', 'Swiss army knife for WiFi, Bluetooth Low Energy, wireless remote controllers', 'sniffing'),
    ('ettercap', 'Ettercap', 'Comprehensive suite for man in the middle attacks', 'sniffing'),
    ('netsniff-ng', 'netsniff-ng', 'Swiss army knife for your daily Linux network plumbing', 'sniffing'),
    ('scapy', 'Scapy', 'Interactive packet manipulation program', 'sniffing'),
    ('mitmproxy', 'mitmproxy', 'Interactive TLS-capable intercepting HTTP proxy', 'sniffing'),
    ('sslsplit', 'SSLsplit', 'Transparent SSL/TLS interception', 'sniffing'),
    ('yersinia', 'Yersinia', 'Network vulnerabilities check', 'sniffing'),
    
    # Reverse Engineering
    ('apktool', 'Apktool', 'Tool for reverse engineering 3rd party, closed, binary Android apps', 'reverseengineering'),
    ('dex2jar', 'dex2jar', 'Tools to work with android .dex and java .class files', 'reverseengineering'),
    ('edb-debugger', 'EDB', 'Cross platform AArch32/x86/x86-64 debugger', 'reverseengineering'),
    ('jadx', 'JADX', 'Dex to Java decompiler', 'reverseengineering'),
    ('mona-py', 'mona.py', 'Corelan Team corelan.be PyCommand for Immunity Debugger', 'reverseengineering'),
    ('ollydbg', 'OllyDbg', '32-bit assembler level analysing debugger', 'reverseengineering'),
    ('radare2', 'radare2', 'UNIX-like reverse engineering framework', 'reverseengineering'),
    ('x64dbg', 'x64dbg', 'An open-source x64/x32 debugger for windows', 'reverseengineering'),
    
    # Maintaining Access
    ('weevely', 'Weevely', 'Weaponized web shell', 'maintainingaccess'),
    ('powershell-empire', 'Empire', 'PowerShell and Python post-exploitation agent', 'maintainingaccess'),
    ('pty-shell', 'pty-shell', 'PTY shell', 'maintainingaccess'),
    ('webshells', 'Webshells', 'Collection of webshells', 'maintainingaccess'),
    
    # Social Engineering
    ('setoolkit', 'SET', 'Social-Engineer Toolkit', 'socialengineering'),
    ('gophish', 'Gophish', 'Open-source phishing framework', 'socialengineering'),
    ('king-phisher', 'King Phisher', 'Phishing campaign toolkit', 'socialengineering')
]

# Read tools.js
with open('src/data/tools.js', 'r') as f:
    content = f.read()

# Generate tool strings
tool_strings = []
for t_id, name, desc, cat in new_tools:
    # Set apt and yay to ID usually.
    # We will assume pacman=null, dnf=null, brew=null, winget=null, flatpak=null unless we hardcode them, but let's just default yay and apt to id.
    # For some like wireshark, nmap, netcat we can assume common ones.
    
    apt = f"'{t_id}'"
    yay = f"'{t_id}'"
    pacman = f"'{t_id}'" if cat in ['infogathering', 'sniffing', 'reverseengineering', 'password'] else 'null'
    brew = 'null'
    winget = 'null'
    flatpak = 'null'
    dnf = f"'{t_id}'" if cat in ['infogathering', 'sniffing', 'reverseengineering', 'password'] else 'null'
    
    if t_id == 'burpsuite':
        brew = "'burp-suite'"
        yay = "'burpsuite'"
    if t_id == 'wireshark':
        brew = "'wireshark'"
        winget = "'WiresharkFoundation.Wireshark'"
    if t_id == 'nmap':
        brew = "'nmap'"
        winget = "'Insecure.Nmap'"
    
    tool_str = f"  {{ id: '{t_id}', name: '{name}', description: '{desc.replace(chr(39), chr(92)+chr(39))}', category: '{cat}', packages: {{ apt: {apt}, dnf: {dnf}, pacman: {pacman}, yay: {yay}, brew: {brew}, winget: {winget}, flatpak: {flatpak} }} }},"
    tool_strings.append(tool_str)

# Insert before the last closing bracket
last_bracket_idx = content.rfind(']')
if last_bracket_idx != -1:
    new_content = content[:last_bracket_idx] + '\n' + '\n'.join(tool_strings) + '\n' + content[last_bracket_idx:]
    with open('src/data/tools.js', 'w') as f:
        f.write(new_content)
    print("Added tools to src/data/tools.js")
else:
    print("Could not find closing bracket in tools.js")
