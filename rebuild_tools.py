import re

with open('src/App.vue', 'r') as f:
    content = f.read()

NEW_TOOLS = """const tools = ref([
  // ── 1. Web Exploitation & Bug Bounty ──
  { id: 'burpsuite', name: 'Burp Suite', description: 'Web vulnerability scanner & proxy', category: 'web',
    packages: { apt: 'burpsuite', dnf: null, pacman: 'burpsuite', yay: 'burpsuite', brew: 'burp-suite', winget: 'PortSwigger.BurpSuite.Community', flatpak: null } },
  { id: 'owaspzap', name: 'OWASP ZAP', description: 'Open-source web app security scanner', category: 'web',
    packages: { apt: 'zaproxy', dnf: 'zaproxy', pacman: 'zaproxy', yay: 'zaproxy', brew: 'owasp-zap', winget: 'OWASP.ZAP', flatpak: null } },
  { id: 'sqlmap', name: 'SQLMap', description: 'Automatic SQL injection & takeover', category: 'web',
    packages: { apt: 'sqlmap', dnf: 'sqlmap', pacman: 'sqlmap', yay: 'sqlmap-git', brew: 'sqlmap', winget: 'sqlmapproject.sqlmap', flatpak: null } },
  { id: 'ffuf', name: 'ffuf', description: 'Fast web fuzzer written in Go', category: 'web',
    packages: { apt: 'ffuf', dnf: 'ffuf', pacman: 'ffuf', yay: 'ffuf', brew: 'ffuf', winget: 'ffuf', flatpak: null } },
  { id: 'gobuster', name: 'Gobuster', description: 'Directory/DNS/VHost busting tool', category: 'web',
    packages: { apt: 'gobuster', dnf: null, pacman: 'gobuster', yay: 'gobuster', brew: 'gobuster', winget: 'OJReeves.Gobuster', flatpak: null } },
  { id: 'dirsearch', name: 'Dirsearch', description: 'Web path brute-forcer', category: 'web',
    packages: { apt: 'dirsearch', dnf: null, pacman: null, yay: 'dirsearch', brew: 'dirsearch', winget: null, flatpak: null } },
  { id: 'nuclei', name: 'Nuclei', description: 'Fast and customizable vulnerability scanner', category: 'web',
    packages: { apt: 'nuclei', dnf: null, pacman: 'nuclei', yay: 'nuclei', brew: 'nuclei', winget: 'ProjectDiscovery.Nuclei', flatpak: null } },

  // ── 2. Network Analysis & Red Teaming ──
  { id: 'nmap', name: 'Nmap', description: 'Network discovery & security auditing', category: 'network',
    packages: { apt: 'nmap', dnf: 'nmap', pacman: 'nmap', yay: 'nmap', brew: 'nmap', winget: 'Insecure.Nmap', flatpak: null } },
  { id: 'wireshark', name: 'Wireshark', description: 'Network protocol analyzer', category: 'network',
    packages: { apt: 'wireshark', dnf: 'wireshark', pacman: 'wireshark-qt', yay: 'wireshark-qt', brew: 'wireshark', winget: 'WiresharkFoundation.Wireshark', flatpak: 'org.wireshark.Wireshark' } },
  { id: 'metasploit', name: 'Metasploit', description: 'Penetration testing framework', category: 'network',
    packages: { apt: 'metasploit-framework', dnf: null, pacman: null, yay: 'metasploit', brew: 'metasploit', winget: 'Rapid7.Metasploit', flatpak: null } },
  { id: 'masscan', name: 'Masscan', description: 'TCP port scanner at scale', category: 'network',
    packages: { apt: 'masscan', dnf: 'masscan', pacman: 'masscan', yay: 'masscan', brew: 'masscan', winget: 'robertdavidgraham.masscan', flatpak: null } },
  { id: 'responder', name: 'Responder', description: 'LLMNR/NBT-NS/MDNS poisoner', category: 'network',
    packages: { apt: 'responder', dnf: null, pacman: null, yay: 'responder', brew: null, winget: null, flatpak: null } },
  { id: 'aircrackng', name: 'Aircrack-ng', description: 'WiFi security auditing tools suite', category: 'network',
    packages: { apt: 'aircrack-ng', dnf: 'aircrack-ng', pacman: 'aircrack-ng', yay: 'aircrack-ng', brew: 'aircrack-ng', winget: null, flatpak: null } },

  // ── 3. Password Cracking & Cryptography ──
  { id: 'hashcat', name: 'Hashcat', description: 'Advanced password recovery utility', category: 'password',
    packages: { apt: 'hashcat', dnf: 'hashcat', pacman: 'hashcat', yay: 'hashcat', brew: 'hashcat', winget: 'hashcat.hashcat', flatpak: null } },
  { id: 'john', name: 'John the Ripper', description: 'Password security auditing tool', category: 'password',
    packages: { apt: 'john', dnf: 'john', pacman: 'john', yay: 'john', brew: 'john-jumbo', winget: 'openwall.johntheripper', flatpak: null } },
  { id: 'hydra', name: 'Hydra', description: 'Parallelized network login cracker', category: 'password',
    packages: { apt: 'hydra', dnf: 'hydra', pacman: 'hydra', yay: 'hydra', brew: 'hydra', winget: null, flatpak: null } },
  { id: 'veracrypt', name: 'VeraCrypt', description: 'Disk encryption software', category: 'password',
    packages: { apt: 'veracrypt', dnf: null, pacman: null, yay: 'veracrypt', brew: 'veracrypt', winget: 'IDRIX.VeraCrypt', flatpak: null } },

  // ── 4. Reconnaissance & OSINT ──
  { id: 'maltego', name: 'Maltego', description: 'Interactive data mining and link analysis', category: 'osint',
    packages: { apt: 'maltego', dnf: null, pacman: null, yay: 'maltego', brew: 'maltego', winget: 'Paterva.Maltego', flatpak: null } },
  { id: 'amass', name: 'Amass', description: 'In-depth attack surface mapping', category: 'osint',
    packages: { apt: 'amass', dnf: null, pacman: 'amass', yay: 'amass', brew: 'amass', winget: 'OWASP.Amass', flatpak: null } },
  { id: 'theharvester', name: 'theHarvester', description: 'E-mails, subdomains and names harvester', category: 'osint',
    packages: { apt: 'theharvester', dnf: null, pacman: null, yay: 'theharvester', brew: 'theharvester', winget: null, flatpak: null } },
  { id: 'sherlock', name: 'Sherlock', description: 'Hunt usernames across social networks', category: 'osint',
    packages: { apt: 'sherlock', dnf: null, pacman: null, yay: 'sherlock', brew: 'sherlock', winget: null, flatpak: null } },

  // ── 5. Terminal, Shell & System Utilities ──
  { id: 'tmux', name: 'Tmux', description: 'Terminal multiplexer', category: 'terminal',
    packages: { apt: 'tmux', dnf: 'tmux', pacman: 'tmux', yay: 'tmux', brew: 'tmux', winget: null, flatpak: null } },
  { id: 'zsh', name: 'Zsh', description: 'Powerful shell with scripting support', category: 'terminal',
    packages: { apt: 'zsh', dnf: 'zsh', pacman: 'zsh', yay: 'zsh', brew: 'zsh', winget: null, flatpak: null } },
  { id: 'fish', name: 'Fish Shell', description: 'User-friendly command line shell', category: 'terminal',
    packages: { apt: 'fish', dnf: 'fish', pacman: 'fish', yay: 'fish', brew: 'fish', winget: null, flatpak: null } },
  { id: 'alacritty', name: 'Alacritty', description: 'GPU-accelerated terminal emulator', category: 'terminal',
    packages: { apt: 'alacritty', dnf: 'alacritty', pacman: 'alacritty', yay: 'alacritty', brew: 'alacritty', winget: 'Alacritty.Alacritty', flatpak: 'org.alacritty.Alacritty' } },
  { id: 'kitty', name: 'Kitty', description: 'Fast, feature-rich GPU terminal', category: 'terminal',
    packages: { apt: 'kitty', dnf: 'kitty', pacman: 'kitty', yay: 'kitty', brew: 'kitty', winget: null, flatpak: null } },
  { id: 'neovim', name: 'Neovim', description: 'Vim-fork focused on extensibility', category: 'terminal',
    packages: { apt: 'neovim', dnf: 'neovim', pacman: 'neovim', yay: 'neovim', brew: 'neovim', winget: 'Neovim.Neovim', flatpak: 'io.neovim.nvim' } },
  { id: 'btop', name: 'BTOP', description: 'Resource monitor (modern htop alternative)', category: 'terminal',
    packages: { apt: 'btop', dnf: 'btop', pacman: 'btop', yay: 'btop', brew: 'btop', winget: 'aristocratos.btop', flatpak: null } },

  // ── 6. Development & Coding ──
  { id: 'vscode', name: 'VS Code', description: 'Lightweight but powerful code editor', category: 'dev',
    packages: { apt: 'code', dnf: 'code', pacman: null, yay: 'visual-studio-code-bin', brew: 'visual-studio-code', winget: 'Microsoft.VisualStudioCode', flatpak: 'com.visualstudio.code' } },
  { id: 'git', name: 'Git', description: 'Distributed version control system', category: 'dev',
    packages: { apt: 'git', dnf: 'git', pacman: 'git', yay: 'git', brew: 'git', winget: 'Git.Git', flatpak: null } },
  { id: 'docker', name: 'Docker', description: 'Container platform for devs & ops', category: 'dev',
    packages: { apt: 'docker.io', dnf: 'docker', pacman: 'docker', yay: 'docker', brew: 'docker', winget: 'Docker.DockerDesktop', flatpak: null } },
  { id: 'python3', name: 'Python 3', description: 'General-purpose programming language', category: 'dev',
    packages: { apt: 'python3', dnf: 'python3', pacman: 'python', yay: 'python', brew: 'python', winget: 'Python.Python.3.12', flatpak: null } },
  { id: 'go', name: 'Go (Golang)', description: 'Open source language by Google', category: 'dev',
    packages: { apt: 'golang', dnf: 'golang', pacman: 'go', yay: 'go', brew: 'go', winget: 'GoLang.Go', flatpak: null } },
  { id: 'nodejs', name: 'Node.js', description: 'JavaScript runtime built on V8', category: 'dev',
    packages: { apt: 'nodejs', dnf: 'nodejs', pacman: 'nodejs', yay: 'nodejs', brew: 'node', winget: 'OpenJS.NodeJS', flatpak: null } },
  { id: 'postman', name: 'Postman', description: 'API platform for building and testing', category: 'dev',
    packages: { apt: null, dnf: null, pacman: null, yay: 'postman-bin', brew: 'postman', winget: 'Postman.Postman', flatpak: 'com.getpostman.Postman' } },

  // ── 7. Everyday Essentials (Daily Use) ──
  { id: 'chrome', name: 'Google Chrome', description: 'Fast, secure web browser', category: 'daily',
    packages: { apt: 'google-chrome-stable', dnf: 'google-chrome-stable', pacman: null, yay: 'google-chrome', brew: 'google-chrome', winget: 'Google.Chrome', flatpak: 'com.google.Chrome' } },
  { id: 'brave', name: 'Brave Browser', description: 'Ad-blocking, privacy-first browser', category: 'daily',
    packages: { apt: 'brave-browser', dnf: 'brave-browser', pacman: null, yay: 'brave-bin', brew: 'brave-browser', winget: 'Brave.Brave', flatpak: 'com.brave.Browser' } },
  { id: 'spotify', name: 'Spotify', description: 'Digital music service', category: 'daily',
    packages: { apt: 'spotify-client', dnf: null, pacman: null, yay: 'spotify', brew: 'spotify', winget: 'Spotify.Spotify', flatpak: 'com.spotify.Client' } },
  { id: 'discord', name: 'Discord', description: 'Voice, video & text communication', category: 'daily',
    packages: { apt: 'discord', dnf: null, pacman: 'discord', yay: 'discord', brew: 'discord', winget: 'Discord.Discord', flatpak: 'com.discordapp.Discord' } },
  { id: 'obsidian', name: 'Obsidian', description: 'Knowledge base & note-taking app', category: 'daily',
    packages: { apt: null, dnf: null, pacman: null, yay: 'obsidian', brew: 'obsidian', winget: 'Obsidian.Obsidian', flatpak: 'md.obsidian.Obsidian' } },
  { id: 'notion', name: 'Notion', description: 'All-in-one workspace for notes & docs', category: 'daily',
    packages: { apt: null, dnf: null, pacman: null, yay: 'notion-app-electron', brew: 'notion', winget: 'Notion.Notion', flatpak: null } },
  { id: 'vlc', name: 'VLC Media Player', description: 'Open source multimedia player', category: 'daily',
    packages: { apt: 'vlc', dnf: 'vlc', pacman: 'vlc', yay: 'vlc', brew: 'vlc', winget: 'VideoLAN.VLC', flatpak: 'org.videolan.VLC' } },
])"""

NEW_CATCOLOR = """// Category badge colors
const catColor = (cat) => ({
  web: 'text-cyber-purple',
  network: 'text-cyber-blue',
  password: 'text-cyber-red',
  osint: 'text-orange-400',
  terminal: 'text-cyan-400',
  dev: 'text-cyber-green',
  daily: 'text-pink-400',
}[cat] || 'text-cyber-text-dim')
</script>"""

# Replace tools array (lines 19-332)
content = re.sub(
    r'// =+\n// Tool Data.*?\n// =+\nconst tools = ref\(\[.*?\]\)',
    '// ============================================================\n'
    '// Tool Data — 7 categories, extensible for Step 2\n'
    '// ============================================================\n'
    + NEW_TOOLS,
    content,
    flags=re.DOTALL
)

# Replace catColor
content = re.sub(
    r'// Category badge colors\nconst catColor.*?\</script>',
    NEW_CATCOLOR,
    content,
    flags=re.DOTALL
)

with open('src/App.vue', 'w') as f:
    f.write(content)

print("Done! Rebuilt tools with 7 categories.")
