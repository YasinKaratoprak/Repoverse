import re
with open('src/App.vue','r') as f: c=f.read()

# Update existing tools' flatpak IDs
updates = {
    'chrome': 'com.google.Chrome', 'firefox': 'org.mozilla.firefox', 'brave': 'com.brave.Browser',
    'edge': 'com.microsoft.Edge', 'vivaldi': 'com.vivaldi.Vivaldi', 'opera': 'com.opera.Opera',
    'discord': 'com.discordapp.Discord', 'thunderbird': 'org.mozilla.Thunderbird',
    'zoom': 'us.zoom.Zoom', 'vscode': 'com.visualstudio.code', 'postman': 'com.getpostman.Postman',
    'vlc': 'org.videolan.VLC', 'spotify': 'com.spotify.Client', 'handbrake': 'fr.handbrake.ghb',
    'audacity': 'org.audacityteam.Audacity', 'krita': 'org.kde.krita', 'blender': 'org.blender.Blender',
    'gimp': 'org.gimp.GIMP', 'inkscape': 'org.inkscape.Inkscape', 'steam': 'com.valvesoftware.Steam',
    'libreoffice': 'org.libreoffice.LibreOffice', 'obsidian': 'md.obsidian.Obsidian',
    'qbittorrent': 'org.qbittorrent.qBittorrent', 'filezilla': 'org.filezillaproject.Filezilla',
    'anydesk': 'com.anydesk.Anydesk', 'alacritty': 'org.alacritty.Alacritty',
    'neovim': 'io.neovim.nvim', 'keepass2': 'org.keepassxc.KeePassXC',
}
for tid, fid in updates.items():
    c = re.sub(r"(id:\s*'" + tid + r"'.*?flatpak:\s*)'[^']*'", r"\1'" + fid + "'", c)
    c = re.sub(r"(id:\s*'" + tid + r"'.*?flatpak:\s*)null", r"\1'" + fid + "'", c)

# New tools to add (flatpak-only or with cross-platform support)
new_tools = [
    # Browsers
    ("chromium","Chromium","Open-source browser","browser",{"flatpak":"org.chromium.Chromium","apt":"chromium-browser","dnf":"chromium","pacman":"chromium","yay":"chromium","brew":"chromium"}),
    ("tor","Tor Browser","Anonymous browsing","browser",{"flatpak":"com.github.micahflee.torbrowser-launcher","apt":"torbrowser-launcher","yay":"tor-browser"}),
    ("mullvad","Mullvad Browser","Privacy browser by Mullvad","browser",{"flatpak":"net.mullvad.MullvadBrowser","yay":"mullvad-browser-bin"}),
    # Messaging
    ("telegram","Telegram Desktop","Fast and secure messaging","messaging",{"flatpak":"org.telegram.desktop","apt":"telegram-desktop","dnf":"telegram-desktop","pacman":"telegram-desktop","yay":"telegram-desktop","brew":"telegram","winget":"Telegram.TelegramDesktop"}),
    ("slack","Slack","Team communication","messaging",{"flatpak":"com.slack.Slack","yay":"slack-desktop","brew":"slack","winget":"SlackTechnologies.Slack"}),
    ("signal","Signal Desktop","Private messaging","messaging",{"flatpak":"org.signal.Signal","apt":"signal-desktop","yay":"signal-desktop","brew":"signal","winget":"OpenWhisperSystems.Signal"}),
    ("skype","Skype","Video calls","messaging",{"flatpak":"com.skype.Client","yay":"skypeforlinux-bin","brew":"skype","winget":"Microsoft.Skype"}),
    ("element","Element","Matrix client","messaging",{"flatpak":"im.riot.Riot","apt":"element-desktop","yay":"element-desktop","brew":"element","winget":"Element.Element"}),
    ("viber","Viber","Messaging and calls","messaging",{"flatpak":"com.viber.Viber","yay":"viber","winget":"Viber.Viber"}),
    ("session","Session","Decentralized messenger","messaging",{"flatpak":"network.loki.Session","yay":"session-desktop-bin"}),
    ("jami","Jami","P2P communication","messaging",{"flatpak":"net.jami.Jami","apt":"jami","dnf":"jami","pacman":"jami","yay":"jami"}),
    # Dev
    ("vscodium","VSCodium","Free VS Code build","dev",{"flatpak":"com.vscodium.codium","yay":"vscodium-bin","brew":"vscodium","winget":"VSCodium.VSCodium"}),
    ("pycharm","PyCharm CE","Python IDE","dev",{"flatpak":"com.jetbrains.PyCharm-Community","yay":"pycharm-community-edition","brew":"pycharm-ce","winget":"JetBrains.PyCharm.Community"}),
    ("intellij","IntelliJ IDEA CE","Java and Kotlin IDE","dev",{"flatpak":"com.jetbrains.IntelliJ-IDEA-Community","yay":"intellij-idea-community-edition","brew":"intellij-idea-ce","winget":"JetBrains.IntelliJIDEA.Community"}),
    ("androidstudio","Android Studio","Android development IDE","dev",{"flatpak":"com.google.AndroidStudio","yay":"android-studio","brew":"android-studio","winget":"Google.AndroidStudio"}),
    ("insomnia","Insomnia","REST/GraphQL API client","dev",{"flatpak":"rest.insomnia.Insomnia","yay":"insomnia-bin","brew":"insomnia","winget":"Kong.Insomnia"}),
    ("dbeaver","DBeaver","Universal database tool","dev",{"flatpak":"io.dbeaver.DBeaverCommunity","pacman":"dbeaver","yay":"dbeaver","brew":"dbeaver-community","winget":"dbeaver.dbeaver"}),
    ("sublimetext","Sublime Text","Fast code editor","dev",{"flatpak":"com.sublimetext.three","yay":"sublime-text-4","brew":"sublime-text","winget":"SublimeHQ.SublimeText.4"}),
    ("godot","Godot Engine","Game engine","dev",{"flatpak":"org.godotengine.Godot","apt":"godot3","yay":"godot","brew":"godot","winget":"GodotEngine.GodotEngine"}),
    ("docker","Docker Desktop","Container platform","dev",{"flatpak":"com.docker.Docker","apt":"docker.io","dnf":"docker","pacman":"docker","yay":"docker","brew":"docker","winget":"Docker.DockerDesktop"}),
    ("gitkraken","GitKraken","Git GUI client","dev",{"flatpak":"com.axosoft.GitKraken","yay":"gitkraken","brew":"gitkraken","winget":"Axosoft.GitKraken"}),
    ("beekeeper","Beekeeper Studio","SQL editor and manager","dev",{"flatpak":"io.beekeeperstudio.Studio","yay":"beekeeper-studio-bin","brew":"beekeeper-studio"}),
    ("emacs","GNU Emacs","Extensible text editor","dev",{"flatpak":"org.gnu.emacs","apt":"emacs","dnf":"emacs","pacman":"emacs","yay":"emacs","brew":"emacs"}),
    ("zed","Zed","High-performance code editor","dev",{"flatpak":"dev.zed.Zed","yay":"zed-editor","brew":"zed"}),
    ("mongocompass","MongoDB Compass","MongoDB GUI","dev",{"flatpak":"com.mongodb.Compass","yay":"mongodb-compass","brew":"mongodb-compass"}),
    # Media
    ("obs","OBS Studio","Live streaming and recording","media",{"flatpak":"com.obsproject.Studio","apt":"obs-studio","dnf":"obs-studio","pacman":"obs-studio","yay":"obs-studio","brew":"obs","winget":"OBSProject.OBSStudio"}),
    ("kdenlive","Kdenlive","Video editor","media",{"flatpak":"org.kde.kdenlive","apt":"kdenlive","dnf":"kdenlive","pacman":"kdenlive","yay":"kdenlive","brew":"kdenlive"}),
    ("mpv","mpv","Minimalist video player","media",{"flatpak":"io.mpv.Mpv","apt":"mpv","dnf":"mpv","pacman":"mpv","yay":"mpv","brew":"mpv"}),
    ("kodi","Kodi","Media center","media",{"flatpak":"tv.kodi.Kodi","apt":"kodi","dnf":"kodi","pacman":"kodi","yay":"kodi","brew":"kodi"}),
    ("shotcut","Shotcut","Video editor","media",{"flatpak":"org.shotcut.Shotcut","apt":"shotcut","yay":"shotcut","brew":"shotcut","winget":"Meltytech.Shotcut"}),
    ("lmms","LMMS","Music production","media",{"flatpak":"io.lmms.LMMS","apt":"lmms","dnf":"lmms","pacman":"lmms","yay":"lmms","brew":"lmms"}),
    # Graphics
    ("darktable","Darktable","Photography workflow","imaging",{"flatpak":"org.darktable.Darktable","apt":"darktable","dnf":"darktable","pacman":"darktable","yay":"darktable","brew":"darktable"}),
    ("rawtherapee","RawTherapee","RAW photo processor","imaging",{"flatpak":"com.rawtherapee.RawTherapee","apt":"rawtherapee","dnf":"rawtherapee","pacman":"rawtherapee","yay":"rawtherapee","brew":"rawtherapee"}),
    ("digikam","digiKam","Photo management","imaging",{"flatpak":"org.kde.digikam","apt":"digikam","dnf":"digikam","pacman":"digikam","yay":"digikam","brew":"digikam"}),
    ("freecad","FreeCAD","3D parametric modeler","imaging",{"flatpak":"org.freecadweb.FreeCAD","apt":"freecad","dnf":"freecad","pacman":"freecad","yay":"freecad","brew":"freecad","winget":"FreeCAD.FreeCAD"}),
    ("mypaint","MyPaint","Painting app","imaging",{"flatpak":"org.mypaint.MyPaint","apt":"mypaint","dnf":"mypaint","pacman":"mypaint","yay":"mypaint"}),
    # Gaming
    ("heroic","Heroic Games Launcher","Epic/GOG launcher","gaming",{"flatpak":"com.heroicgameslauncher.hgl","yay":"heroic-games-launcher-bin","brew":"heroic"}),
    ("lutris","Lutris","Open gaming platform","gaming",{"flatpak":"net.lutris.Lutris","apt":"lutris","dnf":"lutris","pacman":"lutris","yay":"lutris"}),
    ("retroarch","RetroArch","Multi-system emulator","gaming",{"flatpak":"org.libretro.RetroArch","apt":"retroarch","pacman":"retroarch","yay":"retroarch","brew":"retroarch"}),
    ("prismlauncher","Prism Launcher","Minecraft launcher","gaming",{"flatpak":"org.prismlauncher.PrismLauncher","yay":"prismlauncher","brew":"prismlauncher","winget":"PrismLauncher.PrismLauncher"}),
    ("dolphinemu","Dolphin Emulator","GameCube/Wii emulator","gaming",{"flatpak":"org.DolphinEmu.dolphin-emu","apt":"dolphin-emu","pacman":"dolphin-emu","yay":"dolphin-emu","brew":"dolphin"}),
    # Productivity
    ("onlyoffice","ONLYOFFICE","Office suite","docs",{"flatpak":"org.onlyoffice.desktopeditors","yay":"onlyoffice-bin","brew":"onlyoffice","winget":"ONLYOFFICE.DesktopEditors"}),
    ("joplin","Joplin","Note-taking app","docs",{"flatpak":"net.cozic.joplin_desktop","yay":"joplin-appimage","brew":"joplin","winget":"Joplin.Joplin"}),
    ("logseq","Logseq","Knowledge management","docs",{"flatpak":"com.logseq.Logseq","yay":"logseq-desktop-bin","brew":"logseq","winget":"Logseq.Logseq"}),
    ("xournalpp","Xournal++","Handwriting notepad","docs",{"flatpak":"com.github.xournalpp.xournalpp","apt":"xournalpp","dnf":"xournalpp","pacman":"xournalpp","yay":"xournalpp","brew":"xournalpp"}),
    ("standardnotes","Standard Notes","Encrypted notes","docs",{"flatpak":"org.standardnotes.standardnotes","yay":"standardnotes-bin","brew":"standard-notes","winget":"StandardNotes.StandardNotes"}),
    # Utilities
    ("flatseal","Flatseal","Flatpak permissions manager","utilities",{"flatpak":"com.github.tchx84.Flatseal"}),
    ("bitwarden","Bitwarden","Password manager","utilities",{"flatpak":"com.bitwarden.desktop","apt":"bitwarden","yay":"bitwarden","brew":"bitwarden","winget":"Bitwarden.Bitwarden"}),
    ("keepassxc","KeePassXC","Password manager","utilities",{"flatpak":"org.keepassxc.KeePassXC","apt":"keepassxc","dnf":"keepassxc","pacman":"keepassxc","yay":"keepassxc","brew":"keepassxc","winget":"KeePassXCTeam.KeePassXC"}),
    ("transmission","Transmission","BitTorrent client","utilities",{"flatpak":"com.transmissionbt.Transmission","apt":"transmission","dnf":"transmission","pacman":"transmission-gtk","yay":"transmission-gtk","brew":"transmission"}),
    ("bottles","Bottles","Run Windows apps via Wine","utilities",{"flatpak":"com.usebottles.bottles","yay":"bottles"}),
    ("bleachbit","BleachBit","System cleaner","utilities",{"flatpak":"org.bleachbit.BleachBit","apt":"bleachbit","dnf":"bleachbit","pacman":"bleachbit","yay":"bleachbit","winget":"BleachBit.BleachBit"}),
    ("impression","Impression","Bootable USB creator","utilities",{"flatpak":"io.gitlab.adhami3310.Impression"}),
    ("extmanager","Extension Manager","GNOME extension manager","utilities",{"flatpak":"com.mattjakeman.ExtensionManager"}),
]

# Build JS lines for new tools, skip if ID already exists
existing_ids = set(re.findall(r"id:\s*'([^']+)'", c))
lines = []
for tid, name, desc, cat, pkgs in new_tools:
    if tid in existing_ids:
        # Just update the flatpak ID if exists
        if 'flatpak' in pkgs:
            fid = pkgs['flatpak']
            c = re.sub(r"(id:\s*'" + tid + r"'.*?flatpak:\s*)(null|'[^']*')", r"\1'" + fid + "'", c)
        continue
    parts = []
    for pm in ['apt','dnf','pacman','yay','brew','winget','flatpak']:
        v = pkgs.get(pm)
        parts.append(f"{pm}: '{v}'" if v else f"{pm}: null")
    lines.append(f"  {{ id: '{tid}', name: '{name}', description: '{desc}', category: '{cat}', packages: {{ {', '.join(parts)} }} }},")

# Insert before the closing ])
insert = '\n'.join(lines)
c = c.replace('\n])\n', '\n' + insert + '\n])\n', 1)

# Add new category colors
for cat, color in [('gaming','text-emerald-400')]:
    if f"  {cat}:" not in c:
        c = c.replace("}[cat] || 'text-cyber-text-dim')", f"  {cat}: '{color}',\n" + "}[cat] || 'text-cyber-text-dim')")

with open('src/App.vue','w') as f: f.write(c)
print("Done! Added Flatpak tools.")
