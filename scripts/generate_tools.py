import re

tools_data = [
    # Browsers
    {"id": "chrome", "name": "Google Chrome", "desc": "Fast Browser by Google", "cat": "browser", "pkgs": {"apt": "google-chrome-stable", "dnf": "google-chrome-stable", "yay": "google-chrome", "brew": "google-chrome", "winget": "Google.Chrome", "flatpak": "com.google.Chrome"}},
    {"id": "opera", "name": "Opera", "desc": "Alternative Browser", "cat": "browser", "pkgs": {"apt": "opera-stable", "dnf": "opera-stable", "yay": "opera", "brew": "opera", "winget": "Opera.Opera", "flatpak": "com.opera.Opera"}},
    {"id": "firefox", "name": "Mozilla Firefox", "desc": "Extensible Browser", "cat": "browser", "pkgs": {"apt": "firefox", "dnf": "firefox", "pacman": "firefox", "yay": "firefox", "brew": "firefox", "winget": "Mozilla.Firefox", "flatpak": "org.mozilla.firefox"}},
    {"id": "edge", "name": "Microsoft Edge", "desc": "Microsoft Edge Browser", "cat": "browser", "pkgs": {"apt": "microsoft-edge-stable", "dnf": "microsoft-edge-stable", "yay": "microsoft-edge-stable-bin", "brew": "microsoft-edge", "winget": "Microsoft.Edge", "flatpak": "com.microsoft.Edge"}},
    {"id": "brave", "name": "Brave Browser", "desc": "Privacy Browser", "cat": "browser", "pkgs": {"apt": "brave-browser", "dnf": "brave-browser", "yay": "brave-bin", "brew": "brave-browser", "winget": "Brave.Brave", "flatpak": "com.brave.Browser"}},
    {"id": "vivaldi", "name": "Vivaldi", "desc": "Vivaldi Browser", "cat": "browser", "pkgs": {"apt": "vivaldi-stable", "dnf": "vivaldi-stable", "yay": "vivaldi", "brew": "vivaldi", "winget": "VivaldiTechnologies.Vivaldi", "flatpak": "com.vivaldi.Vivaldi"}},

    # Messaging
    {"id": "zoom", "name": "Zoom", "desc": "Video Conference", "cat": "messaging", "pkgs": {"yay": "zoom", "brew": "zoom", "winget": "Zoom.Zoom", "flatpak": "us.zoom.Zoom"}},
    {"id": "discord", "name": "Discord", "desc": "Voice and Text Chat", "cat": "messaging", "pkgs": {"apt": "discord", "pacman": "discord", "yay": "discord", "brew": "discord", "winget": "Discord.Discord", "flatpak": "com.discordapp.Discord"}},
    {"id": "teams", "name": "Microsoft Teams", "desc": "Video Conferencing, Meetings", "cat": "messaging", "pkgs": {"yay": "teams", "brew": "microsoft-teams", "winget": "Microsoft.Teams", "flatpak": "com.microsoft.Teams"}},
    {"id": "pidgin", "name": "Pidgin", "desc": "Multi-IM Client", "cat": "messaging", "pkgs": {"apt": "pidgin", "dnf": "pidgin", "pacman": "pidgin", "yay": "pidgin", "brew": "pidgin", "winget": "Pidgin.Pidgin", "flatpak": "im.pidgin.Pidgin"}},
    {"id": "thunderbird", "name": "Thunderbird", "desc": "Email Reader by Mozilla", "cat": "messaging", "pkgs": {"apt": "thunderbird", "dnf": "thunderbird", "pacman": "thunderbird", "yay": "thunderbird", "brew": "thunderbird", "winget": "Mozilla.Thunderbird", "flatpak": "org.mozilla.Thunderbird"}},
    {"id": "trillian", "name": "Trillian", "desc": "Trillian IM", "cat": "messaging", "pkgs": {"winget": "CeruleanStudios.Trillian"}},

    # Media
    {"id": "itunes", "name": "iTunes", "desc": "Music/Media Manager", "cat": "media", "pkgs": {"winget": "Apple.iTunes"}},
    {"id": "vlc", "name": "VLC", "desc": "Great Video Player", "cat": "media", "pkgs": {"apt": "vlc", "dnf": "vlc", "pacman": "vlc", "yay": "vlc", "brew": "vlc", "winget": "VideoLAN.VLC", "flatpak": "org.videolan.VLC"}},
    {"id": "aimp", "name": "AIMP", "desc": "Music Player", "cat": "media", "pkgs": {"winget": "AIMP.AIMP"}},
    {"id": "foobar2000", "name": "foobar2000", "desc": "Music Player", "cat": "media", "pkgs": {"winget": "PeterPawlowski.foobar2000"}},
    {"id": "winamp", "name": "Winamp", "desc": "Music Player", "cat": "media", "pkgs": {"winget": "Radionomy.Winamp"}},
    {"id": "musicbee", "name": "MusicBee", "desc": "Music Manager & Player", "cat": "media", "pkgs": {"winget": "StevenMayall.MusicBee"}},
    {"id": "audacity", "name": "Audacity", "desc": "Audio Editor", "cat": "media", "pkgs": {"apt": "audacity", "dnf": "audacity", "pacman": "audacity", "yay": "audacity", "brew": "audacity", "winget": "Audacity.Audacity", "flatpak": "org.audacityteam.Audacity"}},
    {"id": "klite", "name": "K-Lite Codecs", "desc": "Video decoders plus MPC", "cat": "media", "pkgs": {"winget": "CodecGuide.K-LiteCodecPack.Basic"}},
    {"id": "gom", "name": "GOM Player", "desc": "Video Player", "cat": "media", "pkgs": {"winget": "GOMLab.GOMPlayer"}},
    {"id": "spotify", "name": "Spotify", "desc": "Online Music Service", "cat": "media", "pkgs": {"apt": "spotify-client", "yay": "spotify", "brew": "spotify", "winget": "Spotify.Spotify", "flatpak": "com.spotify.Client"}},
    {"id": "cccp", "name": "CCCP", "desc": "Video decoders", "cat": "media", "pkgs": {}},
    {"id": "mediamonkey", "name": "MediaMonkey", "desc": "Music Organizer", "cat": "media", "pkgs": {"winget": "VentisMedia.MediaMonkey.5"}},
    {"id": "handbrake", "name": "HandBrake", "desc": "Convert Videos", "cat": "media", "pkgs": {"apt": "handbrake", "dnf": "handbrake", "pacman": "handbrake", "yay": "handbrake", "brew": "handbrake", "winget": "HandBrake.HandBrake", "flatpak": "fr.handbrake.ghb"}},

    # .NET
    {"id": "dotnet8", "name": ".NET 8 Desktop Runtime", "desc": "Microsoft .NET 8", "cat": "dotnet", "pkgs": {"winget": "Microsoft.dotnet.desktop.8"}},
    {"id": "dotnet9", "name": ".NET 9 Desktop Runtime", "desc": "Microsoft .NET 9", "cat": "dotnet", "pkgs": {"winget": "Microsoft.dotnet.desktop.9"}},
    
    # Java
    {"id": "java17", "name": "Java 17 JRE", "desc": "OpenJDK 17 JRE", "cat": "java", "pkgs": {"apt": "openjdk-17-jre", "dnf": "java-17-openjdk", "pacman": "jre17-openjdk", "yay": "jre17-openjdk", "brew": "openjdk@17", "winget": "EclipseAdoptium.Temurin.17.JRE"}},
    {"id": "java21", "name": "Java 21 JRE", "desc": "OpenJDK 21 JRE", "cat": "java", "pkgs": {"apt": "openjdk-21-jre", "dnf": "java-21-openjdk", "pacman": "jre21-openjdk", "yay": "jre21-openjdk", "brew": "openjdk@21", "winget": "EclipseAdoptium.Temurin.21.JRE"}},

    # Imaging
    {"id": "krita", "name": "Krita", "desc": "Painting Program", "cat": "imaging", "pkgs": {"apt": "krita", "dnf": "krita", "pacman": "krita", "yay": "krita", "brew": "krita", "winget": "KDE.Krita", "flatpak": "org.kde.krita"}},
    {"id": "blender", "name": "Blender", "desc": "3D Creation Suite", "cat": "imaging", "pkgs": {"apt": "blender", "dnf": "blender", "pacman": "blender", "yay": "blender", "brew": "blender", "winget": "BlenderFoundation.Blender", "flatpak": "org.blender.Blender"}},
    {"id": "paintnet", "name": "Paint.NET", "desc": "Image Editor", "cat": "imaging", "pkgs": {"winget": "dotPDN.PaintDotNet"}},
    {"id": "gimp", "name": "GIMP", "desc": "Open Source Image Editor", "cat": "imaging", "pkgs": {"apt": "gimp", "dnf": "gimp", "pacman": "gimp", "yay": "gimp", "brew": "gimp", "winget": "GIMP.GIMP", "flatpak": "org.gimp.GIMP"}},
    {"id": "irfanview", "name": "IrfanView", "desc": "Image Viewer", "cat": "imaging", "pkgs": {"winget": "IrfanSkiljan.IrfanView"}},
    {"id": "xnview", "name": "XnView", "desc": "Image Viewer", "cat": "imaging", "pkgs": {"winget": "XnSoft.XnView.Classic"}},
    {"id": "inkscape", "name": "Inkscape", "desc": "Vector Graphics Editor", "cat": "imaging", "pkgs": {"apt": "inkscape", "dnf": "inkscape", "pacman": "inkscape", "yay": "inkscape", "brew": "inkscape", "winget": "Inkscape.Inkscape", "flatpak": "org.inkscape.Inkscape"}},
    {"id": "faststone", "name": "FastStone", "desc": "FastStone Image Viewer", "cat": "imaging", "pkgs": {"winget": "FastStone.ImageViewer"}},
    {"id": "greenshot", "name": "Greenshot", "desc": "Screenshot Tool", "cat": "imaging", "pkgs": {"winget": "Greenshot.Greenshot"}},
    {"id": "sharex", "name": "ShareX", "desc": "Screenshot Uploader", "cat": "imaging", "pkgs": {"winget": "ShareX.ShareX"}},

    # Documents
    {"id": "foxit", "name": "Foxit Reader", "desc": "Alternative PDF Reader", "cat": "docs", "pkgs": {"winget": "Foxit.FoxitReader"}},
    {"id": "libreoffice", "name": "LibreOffice", "desc": "Free Office Suite", "cat": "docs", "pkgs": {"apt": "libreoffice", "dnf": "libreoffice", "pacman": "libreoffice", "yay": "libreoffice", "brew": "libreoffice", "winget": "TheDocumentFoundation.LibreOffice", "flatpak": "org.libreoffice.LibreOffice"}},
    {"id": "sumatrapdf", "name": "SumatraPDF", "desc": "Lightweight PDF Reader", "cat": "docs", "pkgs": {"winget": "SumatraPDF.SumatraPDF"}},
    {"id": "cutepdf", "name": "CutePDF", "desc": "Print Documents as PDF Files", "cat": "docs", "pkgs": {"winget": "AcroSoftware.CutePDFWriter"}},

    # Security
    {"id": "malwarebytes", "name": "Malwarebytes", "desc": "Malware Remover", "cat": "security", "pkgs": {"brew": "malwarebytes", "winget": "Malwarebytes.Malwarebytes"}},
    {"id": "avast", "name": "Avast", "desc": "Avast Free Antivirus", "cat": "security", "pkgs": {"winget": "Avast.Antivirus.Free"}},
    {"id": "avg", "name": "AVG", "desc": "AVG Free Antivirus", "cat": "security", "pkgs": {"winget": "AVG.AntivirusFree"}},
    
    # File Sharing
    {"id": "qbittorrent", "name": "qBittorrent", "desc": "Free Bittorrent Client", "cat": "filesharing", "pkgs": {"apt": "qbittorrent", "dnf": "qbittorrent", "pacman": "qbittorrent", "yay": "qbittorrent", "brew": "qbittorrent", "winget": "qBittorrent.qBittorrent", "flatpak": "org.qbittorrent.qBittorrent"}},

    # Online Storage
    {"id": "dropbox", "name": "Dropbox", "desc": "Online Backup/File Sync", "cat": "storage", "pkgs": {"yay": "dropbox", "brew": "dropbox", "winget": "Dropbox.Dropbox"}},
    {"id": "googledrive", "name": "Google Drive", "desc": "Online File Sync", "cat": "storage", "pkgs": {"brew": "google-drive", "winget": "Google.Drive"}},
    {"id": "onedrive", "name": "OneDrive", "desc": "Online File Sync by Microsoft", "cat": "storage", "pkgs": {"brew": "onedrive", "winget": "Microsoft.OneDrive"}},

    # Other
    {"id": "evernote", "name": "Evernote", "desc": "Online Notes", "cat": "other", "pkgs": {"brew": "evernote", "winget": "Evernote.Evernote"}},
    {"id": "googleearth", "name": "Google Earth", "desc": "Online Atlas by Google", "cat": "other", "pkgs": {"yay": "google-earth-pro", "brew": "google-earth-pro", "winget": "Google.EarthPro"}},
    {"id": "steam", "name": "Steam", "desc": "App Store for Games", "cat": "other", "pkgs": {"apt": "steam", "dnf": "steam", "pacman": "steam", "yay": "steam", "brew": "steam", "winget": "Valve.Steam", "flatpak": "com.valvesoftware.Steam"}},
    {"id": "epicgames", "name": "Epic Games Launcher", "desc": "Epic Games Store", "cat": "other", "pkgs": {"brew": "epic-games", "winget": "EpicGames.EpicGamesLauncher"}},
    {"id": "keepass2", "name": "KeePass 2", "desc": "Password Manager", "cat": "other", "pkgs": {"apt": "keepass2", "dnf": "keepass", "pacman": "keepass", "yay": "keepass", "brew": "keepassxc", "winget": "DominikReichl.KeePass"}},
    {"id": "everything", "name": "Everything", "desc": "Local File Search Engine", "cat": "other", "pkgs": {"winget": "voidtools.Everything"}},

    # Utilities
    {"id": "anydesk", "name": "AnyDesk", "desc": "Remote Desktop", "cat": "utilities", "pkgs": {"yay": "anydesk-bin", "brew": "anydesk", "winget": "AnyDeskSoftwareGmbH.AnyDesk", "flatpak": "com.anydesk.Anydesk"}},
    {"id": "teamviewer", "name": "TeamViewer", "desc": "Remote Access Tool", "cat": "utilities", "pkgs": {"yay": "teamviewer", "brew": "teamviewer", "winget": "TeamViewer.TeamViewer"}},
    {"id": "imgburn", "name": "ImgBurn", "desc": "Disc Burner", "cat": "utilities", "pkgs": {"winget": "LIGHTNINGUK.ImgBurn"}},
    {"id": "teracopy", "name": "TeraCopy", "desc": "Better File Copy", "cat": "utilities", "pkgs": {"winget": "CodeSector.TeraCopy"}},
    {"id": "revo", "name": "Revo", "desc": "App Uninstaller", "cat": "utilities", "pkgs": {"winget": "RevoUninstaller.RevoUninstaller"}},
    {"id": "launchy", "name": "Launchy", "desc": "Hotkey Launcher", "cat": "utilities", "pkgs": {"winget": "Launchy.Launchy"}},
    {"id": "windirstat", "name": "WinDirStat", "desc": "Directory Statistics", "cat": "utilities", "pkgs": {"winget": "WinDirStat.WinDirStat"}},
    {"id": "wiztree", "name": "WizTree", "desc": "Directory Statistics", "cat": "utilities", "pkgs": {"winget": "AntibodySoftware.WizTree"}},
    {"id": "ccleaner", "name": "CCleaner", "desc": "PC Cleaner", "cat": "utilities", "pkgs": {"winget": "Piriform.CCleaner"}},

    # Compression
    {"id": "7zip", "name": "7-Zip", "desc": "Great Compression App", "cat": "compression", "pkgs": {"apt": "p7zip-full", "dnf": "p7zip", "pacman": "p7zip", "yay": "p7zip", "brew": "sevenzip", "winget": "7zip.7zip"}},
    {"id": "peazip", "name": "PeaZip", "desc": "File Compression Tool", "cat": "compression", "pkgs": {"yay": "peazip-qt-bin", "brew": "peazip", "winget": "GiorgioTani.PeaZip", "flatpak": "io.github.peazip.PeaZip"}},
    {"id": "winrar", "name": "WinRAR", "desc": "Compression Tool", "cat": "compression", "pkgs": {"winget": "RARLab.WinRAR"}},

    # VC++ Redist
    {"id": "vcredist2015", "name": "VC Redist 2015+", "desc": "MSVC runtime libraries", "cat": "vcredist", "pkgs": {"winget": "Microsoft.VCRedist.2015+.x64"}},

    # Developer Tools
    {"id": "python", "name": "Python 3", "desc": "Programming Language", "cat": "dev", "pkgs": {"apt": "python3", "dnf": "python3", "pacman": "python", "yay": "python", "brew": "python", "winget": "Python.Python.3.12"}},
    {"id": "git", "name": "Git", "desc": "Version Control System", "cat": "dev", "pkgs": {"apt": "git", "dnf": "git", "pacman": "git", "yay": "git", "brew": "git", "winget": "Git.Git"}},
    {"id": "filezilla", "name": "FileZilla", "desc": "FTP Client", "cat": "dev", "pkgs": {"apt": "filezilla", "dnf": "filezilla", "pacman": "filezilla", "yay": "filezilla", "brew": "filezilla", "winget": "TimKosse.FileZillaClient", "flatpak": "org.filezillaproject.Filezilla"}},
    {"id": "notepadpp", "name": "Notepad++", "desc": "Programmer's Editor", "cat": "dev", "pkgs": {"yay": "notepadqq", "brew": "notepadqq", "winget": "Notepad++.Notepad++", "flatpak": "com.notepadqq.Notepadqq"}},
    {"id": "winscp", "name": "WinSCP", "desc": "SCP Client", "cat": "dev", "pkgs": {"winget": "WinSCP.WinSCP"}},
    {"id": "putty", "name": "PuTTY", "desc": "SSH client", "cat": "dev", "pkgs": {"apt": "putty", "dnf": "putty", "pacman": "putty", "yay": "putty", "brew": "putty", "winget": "PuTTY.PuTTY"}},
    {"id": "eclipse", "name": "Eclipse", "desc": "IDE for Java", "cat": "dev", "pkgs": {"apt": "eclipse", "dnf": "eclipse", "pacman": "eclipse-java", "yay": "eclipse-java", "brew": "eclipse-java", "winget": "EclipseFoundation.EclipseIDEforJavaDevelopers", "flatpak": "org.eclipse.Java"}},
    {"id": "vscode", "name": "Visual Studio Code", "desc": "Programmer's Editor", "cat": "dev", "pkgs": {"apt": "code", "dnf": "code", "yay": "visual-studio-code-bin", "brew": "visual-studio-code", "winget": "Microsoft.VisualStudioCode", "flatpak": "com.visualstudio.code"}},
    {"id": "cursor", "name": "Cursor", "desc": "AI Code Editor", "cat": "dev", "pkgs": {"yay": "cursor-bin", "brew": "cursor", "winget": "Anysphere.Cursor"}},
]

js_tools = "const tools = ref([\n"
for t in tools_data:
    pkgs_str = ", ".join([f"{k}: '{v}'" if v else f"{k}: null" for k, v in t["pkgs"].items()])
    # Fill in missing pm with null
    for pm in ["apt", "dnf", "pacman", "yay", "brew", "winget", "flatpak"]:
        if pm not in t["pkgs"]:
            pkgs_str += f", {pm}: null"
            
    js_tools += f"  {{ id: '{t['id']}', name: '{t['name']}', description: '{t['desc']}', category: '{t['cat']}', packages: {{ {pkgs_str} }} }},\n"
js_tools += "])\n"

with open('src/App.vue', 'r') as f:
    content = f.read()

# Update tools array
content = re.sub(r'const tools = ref\(\[.*?\]\)\n', js_tools, content, flags=re.DOTALL)

# Update UI to use v-if
content = re.sub(
    r'<div\s+v-for="tool in tools"\s+:key="tool\.id"\s+@click="toggleTool\(tool\)"\s+:class="\[[^\]]+\]"\s*>',
    '''<div
              v-for="tool in tools"
              :key="tool.id"
              v-if="isSupported(tool)"
              @click="toggleTool(tool)"
              :class="[
                'relative rounded-xl border p-4 transition-all duration-300 cursor-pointer',
                selectedTools.has(tool.id)
                  ? 'border-cyber-green/60 bg-cyber-green/8 shadow-[0_0_15px_rgba(0,255,153,0.08)]'
                  : 'border-cyber-border bg-cyber-card hover:border-cyber-green/30 hover:bg-cyber-card-hover'
              ]"
            >''',
    content,
    flags=re.DOTALL
)

# Remove the gray out logic for the checkbox indicator
content = re.sub(
    r':class="\[\s*\'flex h-5 w-5 items-center justify-center rounded border transition-all\',\s*!isSupported\(tool\)\s*\?\s*\'border-cyber-disabled bg-cyber-disabled/30\'\s*:\s*selectedTools\.has\(tool\.id\)\s*\?\s*\'border-cyber-green bg-cyber-green text-cyber-bg\'\s*:\s*\'border-cyber-border bg-cyber-surface\'\s*\]"',
    """:class="[
                    'flex h-5 w-5 items-center justify-center rounded border transition-all',
                    selectedTools.has(tool.id)
                      ? 'border-cyber-green bg-cyber-green text-cyber-bg'
                      : 'border-cyber-border bg-cyber-surface'
                  ]\"""",
    content,
    flags=re.DOTALL
)

# Remove the text gray out logic
content = re.sub(r":class=\"\['mb-1 text-sm font-bold', isSupported\(tool\) \? 'text-cyber-text' : 'text-cyber-disabled'\]\"", 'class="mb-1 text-sm font-bold text-cyber-text"', content)
content = re.sub(r":class=\"\['mb-2 text-xs leading-relaxed', isSupported\(tool\) \? 'text-cyber-text-dim' : 'text-cyber-disabled'\]\"", 'class="mb-2 text-xs leading-relaxed text-cyber-text-dim"', content)
content = re.sub(r":class=\"\['text-\[10px\] font-bold uppercase tracking-wider', isSupported\(tool\) \? catColor\(tool\.category\) : 'text-cyber-disabled'\]\"", ':class="[\'text-[10px] font-bold uppercase tracking-wider\', catColor(tool.category)]"', content)

# Remove the "Not supported" label entirely
content = re.sub(r'<!-- Not supported label -->\s*<div v-if="!isSupported\(tool\)".*?</div>', '', content, flags=re.DOTALL)

with open('src/App.vue', 'w') as f:
    f.write(content)

print("Updated tools and UI.")
