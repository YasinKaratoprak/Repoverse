<script setup>
import { ref, computed } from 'vue'

// ============================================================
// OS / Package Manager Definitions
// ============================================================
const osOptions = [
  { id: 'apt', label: 'Ubuntu / Debian', img: '/images/ubuntu.png', pm: 'apt', prefix: 'sudo apt install -y' },
  { id: 'dnf', label: 'Fedora', img: '/images/Fedora.png', pm: 'dnf', prefix: 'sudo dnf install -y' },
  { id: 'pacman', label: 'Arch (pacman)', img: '/images/pacman.png', pm: 'pacman', prefix: 'sudo pacman -S --noconfirm' },
  { id: 'yay', label: 'Arch (AUR / yay)', img: '/images/pacman.png', pm: 'yay', prefix: 'yay -S --noconfirm' },
  { id: 'brew', label: 'macOS (Brew)', img: '/images/homebrew.png', pm: 'brew', prefix: 'brew install' },
  { id: 'winget', label: 'Windows (Winget)', img: '/images/windows.png', pm: 'winget', prefix: 'winget install -e --id' },
  { id: 'flatpak', label: 'Universal (Flatpak)', img: '/images/flatpak.png', pm: 'flatpak', prefix: 'flatpak install -y flathub' },
]

const selectedOS = ref('apt')

// ============================================================
// Tool Data — 7 categories, extensible for Step 2
// ============================================================
const tools = ref([
  { id: 'chrome', name: 'Google Chrome', description: 'Fast Browser by Google', category: 'browser', packages: { apt: 'google-chrome-stable', dnf: 'google-chrome-stable', yay: 'google-chrome', brew: 'google-chrome', winget: 'Google.Chrome', flatpak: 'com.google.Chrome', pacman: null } },
  { id: 'opera', name: 'Opera', description: 'Alternative Browser', category: 'browser', packages: { apt: 'opera-stable', dnf: 'opera-stable', yay: 'opera', brew: 'opera', winget: 'Opera.Opera', flatpak: 'com.opera.Opera', pacman: null } },
  { id: 'firefox', name: 'Mozilla Firefox', description: 'Extensible Browser', category: 'browser', packages: { apt: 'firefox', dnf: 'firefox', pacman: 'firefox', yay: 'firefox', brew: 'firefox', winget: 'Mozilla.Firefox', flatpak: 'org.mozilla.firefox' } },
  { id: 'edge', name: 'Microsoft Edge', description: 'Microsoft Edge Browser', category: 'browser', packages: { apt: 'microsoft-edge-stable', dnf: 'microsoft-edge-stable', yay: 'microsoft-edge-stable-bin', brew: 'microsoft-edge', winget: 'Microsoft.Edge', flatpak: 'com.microsoft.Edge', pacman: null } },
  { id: 'brave', name: 'Brave Browser', description: 'Privacy Browser', category: 'browser', packages: { apt: 'brave-browser', dnf: 'brave-browser', yay: 'brave-bin', brew: 'brave-browser', winget: 'Brave.Brave', flatpak: 'com.brave.Browser', pacman: null } },
  { id: 'vivaldi', name: 'Vivaldi', description: 'Vivaldi Browser', category: 'browser', packages: { apt: 'vivaldi-stable', dnf: 'vivaldi-stable', yay: 'vivaldi', brew: 'vivaldi', winget: 'VivaldiTechnologies.Vivaldi', flatpak: 'com.vivaldi.Vivaldi', pacman: null } },
  { id: 'zoom', name: 'Zoom', description: 'Video Conference', category: 'messaging', packages: { yay: 'zoom', brew: 'zoom', winget: 'Zoom.Zoom', flatpak: 'us.zoom.Zoom', apt: null, dnf: null, pacman: null } },
  { id: 'discord', name: 'Discord', description: 'Voice and Text Chat', category: 'messaging', packages: { apt: 'discord', pacman: 'discord', yay: 'discord', brew: 'discord', winget: 'Discord.Discord', flatpak: 'com.discordapp.Discord', dnf: null } },
  { id: 'teams', name: 'Microsoft Teams', description: 'Video Conferencing, Meetings', category: 'messaging', packages: { yay: 'teams', brew: 'microsoft-teams', winget: 'Microsoft.Teams', flatpak: 'com.microsoft.Teams', apt: null, dnf: null, pacman: null } },
  { id: 'pidgin', name: 'Pidgin', description: 'Multi-IM Client', category: 'messaging', packages: { apt: 'pidgin', dnf: 'pidgin', pacman: 'pidgin', yay: 'pidgin', brew: 'pidgin', winget: 'Pidgin.Pidgin', flatpak: 'im.pidgin.Pidgin' } },
  { id: 'thunderbird', name: 'Thunderbird', description: 'Email Reader by Mozilla', category: 'messaging', packages: { apt: 'thunderbird', dnf: 'thunderbird', pacman: 'thunderbird', yay: 'thunderbird', brew: 'thunderbird', winget: 'Mozilla.Thunderbird', flatpak: 'org.mozilla.Thunderbird' } },
  { id: 'trillian', name: 'Trillian', description: 'Trillian IM', category: 'messaging', packages: { winget: 'CeruleanStudios.Trillian', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'itunes', name: 'iTunes', description: 'Music/Media Manager', category: 'media', packages: { winget: 'Apple.iTunes', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'vlc', name: 'VLC', description: 'Great Video Player', category: 'media', packages: { apt: 'vlc', dnf: 'vlc', pacman: 'vlc', yay: 'vlc', brew: 'vlc', winget: 'VideoLAN.VLC', flatpak: 'org.videolan.VLC' } },
  { id: 'aimp', name: 'AIMP', description: 'Music Player', category: 'media', packages: { winget: 'AIMP.AIMP', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'foobar2000', name: 'foobar2000', description: 'Music Player', category: 'media', packages: { winget: 'PeterPawlowski.foobar2000', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'winamp', name: 'Winamp', description: 'Music Player', category: 'media', packages: { winget: 'Radionomy.Winamp', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'musicbee', name: 'MusicBee', description: 'Music Manager & Player', category: 'media', packages: { winget: 'StevenMayall.MusicBee', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'audacity', name: 'Audacity', description: 'Audio Editor', category: 'media', packages: { apt: 'audacity', dnf: 'audacity', pacman: 'audacity', yay: 'audacity', brew: 'audacity', winget: 'Audacity.Audacity', flatpak: 'org.audacityteam.Audacity' } },
  { id: 'klite', name: 'K-Lite Codecs', description: 'Video decoders plus MPC', category: 'media', packages: { winget: 'CodecGuide.K-LiteCodecPack.Basic', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'gom', name: 'GOM Player', description: 'Video Player', category: 'media', packages: { winget: 'GOMLab.GOMPlayer', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'spotify', name: 'Spotify', description: 'Online Music Service', category: 'media', packages: { apt: 'spotify-client', yay: 'spotify', brew: 'spotify', winget: 'Spotify.Spotify', flatpak: 'com.spotify.Client', dnf: null, pacman: null } },
  { id: 'cccp', name: 'CCCP', description: 'Video decoders', category: 'media', packages: { apt: null, dnf: null, pacman: null, yay: null, brew: null, winget: null, flatpak: null } },
  { id: 'mediamonkey', name: 'MediaMonkey', description: 'Music Organizer', category: 'media', packages: { winget: 'VentisMedia.MediaMonkey.5', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'handbrake', name: 'HandBrake', description: 'Convert Videos', category: 'media', packages: { apt: 'handbrake', dnf: 'handbrake', pacman: 'handbrake', yay: 'handbrake', brew: 'handbrake', winget: 'HandBrake.HandBrake', flatpak: 'fr.handbrake.ghb' } },
  { id: 'dotnet8', name: '.NET 8 Desktop Runtime', description: 'Microsoft .NET 8', category: 'dotnet', packages: { winget: 'Microsoft.dotnet.desktop.8', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'dotnet9', name: '.NET 9 Desktop Runtime', description: 'Microsoft .NET 9', category: 'dotnet', packages: { winget: 'Microsoft.dotnet.desktop.9', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'java17', name: 'Java 17 JRE', description: 'OpenJDK 17 JRE', category: 'java', packages: { apt: 'openjdk-17-jre', dnf: 'java-17-openjdk', pacman: 'jre17-openjdk', yay: 'jre17-openjdk', brew: 'openjdk@17', winget: 'EclipseAdoptium.Temurin.17.JRE', flatpak: null } },
  { id: 'java21', name: 'Java 21 JRE', description: 'OpenJDK 21 JRE', category: 'java', packages: { apt: 'openjdk-21-jre', dnf: 'java-21-openjdk', pacman: 'jre21-openjdk', yay: 'jre21-openjdk', brew: 'openjdk@21', winget: 'EclipseAdoptium.Temurin.21.JRE', flatpak: null } },
  { id: 'krita', name: 'Krita', description: 'Painting Program', category: 'imaging', packages: { apt: 'krita', dnf: 'krita', pacman: 'krita', yay: 'krita', brew: 'krita', winget: 'KDE.Krita', flatpak: 'org.kde.krita' } },
  { id: 'blender', name: 'Blender', description: '3D Creation Suite', category: 'imaging', packages: { apt: 'blender', dnf: 'blender', pacman: 'blender', yay: 'blender', brew: 'blender', winget: 'BlenderFoundation.Blender', flatpak: 'org.blender.Blender' } },
  { id: 'paintnet', name: 'Paint.NET', description: 'Image Editor', category: 'imaging', packages: { winget: 'dotPDN.PaintDotNet', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'gimp', name: 'GIMP', description: 'Open Source Image Editor', category: 'imaging', packages: { apt: 'gimp', dnf: 'gimp', pacman: 'gimp', yay: 'gimp', brew: 'gimp', winget: 'GIMP.GIMP', flatpak: 'org.gimp.GIMP' } },
  { id: 'irfanview', name: 'IrfanView', description: 'Image Viewer', category: 'imaging', packages: { winget: 'IrfanSkiljan.IrfanView', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'xnview', name: 'XnView', description: 'Image Viewer', category: 'imaging', packages: { winget: 'XnSoft.XnView.Classic', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'inkscape', name: 'Inkscape', description: 'Vector Graphics Editor', category: 'imaging', packages: { apt: 'inkscape', dnf: 'inkscape', pacman: 'inkscape', yay: 'inkscape', brew: 'inkscape', winget: 'Inkscape.Inkscape', flatpak: 'org.inkscape.Inkscape' } },
  { id: 'faststone', name: 'FastStone', description: 'FastStone Image Viewer', category: 'imaging', packages: { winget: 'FastStone.ImageViewer', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'greenshot', name: 'Greenshot', description: 'Screenshot Tool', category: 'imaging', packages: { winget: 'Greenshot.Greenshot', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'sharex', name: 'ShareX', description: 'Screenshot Uploader', category: 'imaging', packages: { winget: 'ShareX.ShareX', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'foxit', name: 'Foxit Reader', description: 'Alternative PDF Reader', category: 'docs', packages: { winget: 'Foxit.FoxitReader', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'libreoffice', name: 'LibreOffice', description: 'Free Office Suite', category: 'docs', packages: { apt: 'libreoffice', dnf: 'libreoffice', pacman: 'libreoffice', yay: 'libreoffice', brew: 'libreoffice', winget: 'TheDocumentFoundation.LibreOffice', flatpak: 'org.libreoffice.LibreOffice' } },
  { id: 'sumatrapdf', name: 'SumatraPDF', description: 'Lightweight PDF Reader', category: 'docs', packages: { winget: 'SumatraPDF.SumatraPDF', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'cutepdf', name: 'CutePDF', description: 'Print Documents as PDF Files', category: 'docs', packages: { winget: 'AcroSoftware.CutePDFWriter', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'malwarebytes', name: 'Malwarebytes', description: 'Malware Remover', category: 'security', packages: { brew: 'malwarebytes', winget: 'Malwarebytes.Malwarebytes', apt: null, dnf: null, pacman: null, yay: null, flatpak: null } },
  { id: 'avast', name: 'Avast', description: 'Avast Free Antivirus', category: 'security', packages: { winget: 'Avast.Antivirus.Free', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'avg', name: 'AVG', description: 'AVG Free Antivirus', category: 'security', packages: { winget: 'AVG.AntivirusFree', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'qbittorrent', name: 'qBittorrent', description: 'Free Bittorrent Client', category: 'filesharing', packages: { apt: 'qbittorrent', dnf: 'qbittorrent', pacman: 'qbittorrent', yay: 'qbittorrent', brew: 'qbittorrent', winget: 'qBittorrent.qBittorrent', flatpak: 'org.qbittorrent.qBittorrent' } },
  { id: 'dropbox', name: 'Dropbox', description: 'Online Backup/File Sync', category: 'storage', packages: { yay: 'dropbox', brew: 'dropbox', winget: 'Dropbox.Dropbox', apt: null, dnf: null, pacman: null, flatpak: null } },
  { id: 'googledrive', name: 'Google Drive', description: 'Online File Sync', category: 'storage', packages: { brew: 'google-drive', winget: 'Google.Drive', apt: null, dnf: null, pacman: null, yay: null, flatpak: null } },
  { id: 'onedrive', name: 'OneDrive', description: 'Online File Sync by Microsoft', category: 'storage', packages: { brew: 'onedrive', winget: 'Microsoft.OneDrive', apt: null, dnf: null, pacman: null, yay: null, flatpak: null } },
  { id: 'evernote', name: 'Evernote', description: 'Online Notes', category: 'other', packages: { brew: 'evernote', winget: 'Evernote.Evernote', apt: null, dnf: null, pacman: null, yay: null, flatpak: null } },
  { id: 'googleearth', name: 'Google Earth', description: 'Online Atlas by Google', category: 'other', packages: { yay: 'google-earth-pro', brew: 'google-earth-pro', winget: 'Google.EarthPro', apt: null, dnf: null, pacman: null, flatpak: null } },
  { id: 'steam', name: 'Steam', description: 'App Store for Games', category: 'other', packages: { apt: 'steam', dnf: 'steam', pacman: 'steam', yay: 'steam', brew: 'steam', winget: 'Valve.Steam', flatpak: 'com.valvesoftware.Steam' } },
  { id: 'epicgames', name: 'Epic Games Launcher', description: 'Epic Games Store', category: 'other', packages: { brew: 'epic-games', winget: 'EpicGames.EpicGamesLauncher', apt: null, dnf: null, pacman: null, yay: null, flatpak: null } },
  { id: 'keepass2', name: 'KeePass 2', description: 'Password Manager', category: 'other', packages: { apt: 'keepass2', dnf: 'keepass', pacman: 'keepass', yay: 'keepass', brew: 'keepassxc', winget: 'DominikReichl.KeePass', flatpak: 'org.keepassxc.KeePassXC' } },
  { id: 'everything', name: 'Everything', description: 'Local File Search Engine', category: 'other', packages: { winget: 'voidtools.Everything', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'anydesk', name: 'AnyDesk', description: 'Remote Desktop', category: 'utilities', packages: { yay: 'anydesk-bin', brew: 'anydesk', winget: 'AnyDeskSoftwareGmbH.AnyDesk', flatpak: 'com.anydesk.Anydesk', apt: null, dnf: null, pacman: null } },
  { id: 'teamviewer', name: 'TeamViewer', description: 'Remote Access Tool', category: 'utilities', packages: { yay: 'teamviewer', brew: 'teamviewer', winget: 'TeamViewer.TeamViewer', apt: null, dnf: null, pacman: null, flatpak: null } },
  { id: 'imgburn', name: 'ImgBurn', description: 'Disc Burner', category: 'utilities', packages: { winget: 'LIGHTNINGUK.ImgBurn', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'teracopy', name: 'TeraCopy', description: 'Better File Copy', category: 'utilities', packages: { winget: 'CodeSector.TeraCopy', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'revo', name: 'Revo', description: 'App Uninstaller', category: 'utilities', packages: { winget: 'RevoUninstaller.RevoUninstaller', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'launchy', name: 'Launchy', description: 'Hotkey Launcher', category: 'utilities', packages: { winget: 'Launchy.Launchy', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'windirstat', name: 'WinDirStat', description: 'Directory Statistics', category: 'utilities', packages: { winget: 'WinDirStat.WinDirStat', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'wiztree', name: 'WizTree', description: 'Directory Statistics', category: 'utilities', packages: { winget: 'AntibodySoftware.WizTree', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'ccleaner', name: 'CCleaner', description: 'PC Cleaner', category: 'utilities', packages: { winget: 'Piriform.CCleaner', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: '7zip', name: '7-Zip', description: 'Great Compression App', category: 'compression', packages: { apt: 'p7zip-full', dnf: 'p7zip', pacman: 'p7zip', yay: 'p7zip', brew: 'sevenzip', winget: '7zip.7zip', flatpak: null } },
  { id: 'peazip', name: 'PeaZip', description: 'File Compression Tool', category: 'compression', packages: { yay: 'peazip-qt-bin', brew: 'peazip', winget: 'GiorgioTani.PeaZip', flatpak: 'io.github.peazip.PeaZip', apt: null, dnf: null, pacman: null } },
  { id: 'winrar', name: 'WinRAR', description: 'Compression Tool', category: 'compression', packages: { winget: 'RARLab.WinRAR', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'vcredist2015', name: 'VC Redist 2015+', description: 'MSVC runtime libraries', category: 'vcredist', packages: { winget: 'Microsoft.VCRedist.2015+.x64', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'python', name: 'Python 3', description: 'Programming Language', category: 'dev', packages: { apt: 'python3', dnf: 'python3', pacman: 'python', yay: 'python', brew: 'python', winget: 'Python.Python.3.12', flatpak: null } },
  { id: 'git', name: 'Git', description: 'Version Control System', category: 'dev', packages: { apt: 'git', dnf: 'git', pacman: 'git', yay: 'git', brew: 'git', winget: 'Git.Git', flatpak: null } },
  { id: 'filezilla', name: 'FileZilla', description: 'FTP Client', category: 'dev', packages: { apt: 'filezilla', dnf: 'filezilla', pacman: 'filezilla', yay: 'filezilla', brew: 'filezilla', winget: 'TimKosse.FileZillaClient', flatpak: 'org.filezillaproject.Filezilla' } },
  { id: 'notepadpp', name: 'Notepad++', description: 'Code Editor', category: 'dev', packages: { yay: 'notepadqq', brew: 'notepadqq', winget: 'Notepad++.Notepad++', flatpak: 'com.notepadqq.Notepadqq', apt: null, dnf: null, pacman: null } },
  { id: 'winscp', name: 'WinSCP', description: 'SCP Client', category: 'dev', packages: { winget: 'WinSCP.WinSCP', apt: null, dnf: null, pacman: null, yay: null, brew: null, flatpak: null } },
  { id: 'putty', name: 'PuTTY', description: 'SSH client', category: 'dev', packages: { apt: 'putty', dnf: 'putty', pacman: 'putty', yay: 'putty', brew: 'putty', winget: 'PuTTY.PuTTY', flatpak: null } },
  { id: 'eclipse', name: 'Eclipse', description: 'IDE for Java', category: 'dev', packages: { apt: 'eclipse', dnf: 'eclipse', pacman: 'eclipse-java', yay: 'eclipse-java', brew: 'eclipse-java', winget: 'EclipseFoundation.EclipseIDEforJavaDevelopers', flatpak: 'org.eclipse.Java' } },
  { id: 'vscode', name: 'Visual Studio Code', description: 'Code Editor', category: 'dev', packages: { apt: 'code', dnf: 'code', yay: 'visual-studio-code-bin', brew: 'visual-studio-code', winget: 'Microsoft.VisualStudioCode', flatpak: 'com.visualstudio.code', pacman: null } },
  { id: 'cursor', name: 'Cursor', description: 'AI Code Editor', category: 'dev', packages: { yay: 'cursor-bin', brew: 'cursor', winget: 'Anysphere.Cursor', apt: null, dnf: null, pacman: null, flatpak: null } },
  { id: 'chromium', name: 'Chromium', description: 'Open-source browser', category: 'browser', packages: { apt: 'chromium-browser', dnf: 'chromium', pacman: 'chromium', yay: 'chromium', brew: 'chromium', winget: null, flatpak: 'org.chromium.Chromium' } },
  { id: 'tor', name: 'Tor Browser', description: 'Anonymous browsing', category: 'browser', packages: { apt: 'torbrowser-launcher', dnf: null, pacman: null, yay: 'tor-browser', brew: null, winget: null, flatpak: 'com.github.micahflee.torbrowser-launcher' } },
  { id: 'mullvad', name: 'Mullvad Browser', description: 'Privacy browser by Mullvad', category: 'browser', packages: { apt: null, dnf: null, pacman: null, yay: 'mullvad-browser-bin', brew: null, winget: null, flatpak: 'net.mullvad.MullvadBrowser' } },
  { id: 'telegram', name: 'Telegram Desktop', description: 'Fast and secure messaging', category: 'messaging', packages: { apt: 'telegram-desktop', dnf: 'telegram-desktop', pacman: 'telegram-desktop', yay: 'telegram-desktop', brew: 'telegram', winget: 'Telegram.TelegramDesktop', flatpak: 'org.telegram.desktop' } },
  { id: 'slack', name: 'Slack', description: 'Team communication', category: 'messaging', packages: { apt: null, dnf: null, pacman: null, yay: 'slack-desktop', brew: 'slack', winget: 'SlackTechnologies.Slack', flatpak: 'com.slack.Slack' } },
  { id: 'signal', name: 'Signal Desktop', description: 'Private messaging', category: 'messaging', packages: { apt: 'signal-desktop', dnf: null, pacman: null, yay: 'signal-desktop', brew: 'signal', winget: 'OpenWhisperSystems.Signal', flatpak: 'org.signal.Signal' } },
  { id: 'skype', name: 'Skype', description: 'Video calls', category: 'messaging', packages: { apt: null, dnf: null, pacman: null, yay: 'skypeforlinux-bin', brew: 'skype', winget: 'Microsoft.Skype', flatpak: 'com.skype.Client' } },
  { id: 'element', name: 'Element', description: 'Matrix client', category: 'messaging', packages: { apt: 'element-desktop', dnf: null, pacman: null, yay: 'element-desktop', brew: 'element', winget: 'Element.Element', flatpak: 'im.riot.Riot' } },
  { id: 'viber', name: 'Viber', description: 'Messaging and calls', category: 'messaging', packages: { apt: null, dnf: null, pacman: null, yay: 'viber', brew: null, winget: 'Viber.Viber', flatpak: 'com.viber.Viber' } },
  { id: 'session', name: 'Session', description: 'Decentralized messenger', category: 'messaging', packages: { apt: null, dnf: null, pacman: null, yay: 'session-desktop-bin', brew: null, winget: null, flatpak: 'network.loki.Session' } },
  { id: 'jami', name: 'Jami', description: 'P2P communication', category: 'messaging', packages: { apt: 'jami', dnf: 'jami', pacman: 'jami', yay: 'jami', brew: null, winget: null, flatpak: 'net.jami.Jami' } },
  { id: 'vscodium', name: 'VSCodium', description: 'Free VS Code build', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'vscodium-bin', brew: 'vscodium', winget: 'VSCodium.VSCodium', flatpak: 'com.vscodium.codium' } },
  { id: 'pycharm', name: 'PyCharm CE', description: 'Python IDE', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'pycharm-community-edition', brew: 'pycharm-ce', winget: 'JetBrains.PyCharm.Community', flatpak: 'com.jetbrains.PyCharm-Community' } },
  { id: 'intellij', name: 'IntelliJ IDEA CE', description: 'Java and Kotlin IDE', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'intellij-idea-community-edition', brew: 'intellij-idea-ce', winget: 'JetBrains.IntelliJIDEA.Community', flatpak: 'com.jetbrains.IntelliJ-IDEA-Community' } },
  { id: 'androidstudio', name: 'Android Studio', description: 'Android development IDE', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'android-studio', brew: 'android-studio', winget: 'Google.AndroidStudio', flatpak: 'com.google.AndroidStudio' } },
  { id: 'insomnia', name: 'Insomnia', description: 'REST/GraphQL API client', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'insomnia-bin', brew: 'insomnia', winget: 'Kong.Insomnia', flatpak: 'rest.insomnia.Insomnia' } },
  { id: 'dbeaver', name: 'DBeaver', description: 'Universal database tool', category: 'dev', packages: { apt: null, dnf: null, pacman: 'dbeaver', yay: 'dbeaver', brew: 'dbeaver-community', winget: 'dbeaver.dbeaver', flatpak: 'io.dbeaver.DBeaverCommunity' } },
  { id: 'sublimetext', name: 'Sublime Text', description: 'Fast code editor', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'sublime-text-4', brew: 'sublime-text', winget: 'SublimeHQ.SublimeText.4', flatpak: 'com.sublimetext.three' } },
  { id: 'godot', name: 'Godot Engine', description: 'Game engine', category: 'dev', packages: { apt: 'godot3', dnf: null, pacman: null, yay: 'godot', brew: 'godot', winget: 'GodotEngine.GodotEngine', flatpak: 'org.godotengine.Godot' } },
  { id: 'docker', name: 'Docker Desktop', description: 'Container platform', category: 'dev', packages: { apt: 'docker.io', dnf: 'docker', pacman: 'docker', yay: 'docker', brew: 'docker', winget: 'Docker.DockerDesktop', flatpak: 'com.docker.Docker' } },
  { id: 'gitkraken', name: 'GitKraken', description: 'Git GUI client', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'gitkraken', brew: 'gitkraken', winget: 'Axosoft.GitKraken', flatpak: 'com.axosoft.GitKraken' } },
  { id: 'beekeeper', name: 'Beekeeper Studio', description: 'SQL editor and manager', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'beekeeper-studio-bin', brew: 'beekeeper-studio', winget: null, flatpak: 'io.beekeeperstudio.Studio' } },
  { id: 'emacs', name: 'GNU Emacs', description: 'Extensible text editor', category: 'dev', packages: { apt: 'emacs', dnf: 'emacs', pacman: 'emacs', yay: 'emacs', brew: 'emacs', winget: null, flatpak: 'org.gnu.emacs' } },
  { id: 'zed', name: 'Zed', description: 'High-performance code editor', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'zed-editor', brew: 'zed', winget: null, flatpak: 'dev.zed.Zed' } },
  { id: 'mongocompass', name: 'MongoDB Compass', description: 'MongoDB GUI', category: 'dev', packages: { apt: null, dnf: null, pacman: null, yay: 'mongodb-compass', brew: 'mongodb-compass', winget: null, flatpak: 'com.mongodb.Compass' } },
  { id: 'obs', name: 'OBS Studio', description: 'Live streaming and recording', category: 'media', packages: { apt: 'obs-studio', dnf: 'obs-studio', pacman: 'obs-studio', yay: 'obs-studio', brew: 'obs', winget: 'OBSProject.OBSStudio', flatpak: 'com.obsproject.Studio' } },
  { id: 'kdenlive', name: 'Kdenlive', description: 'Video editor', category: 'media', packages: { apt: 'kdenlive', dnf: 'kdenlive', pacman: 'kdenlive', yay: 'kdenlive', brew: 'kdenlive', winget: null, flatpak: 'org.kde.kdenlive' } },
  { id: 'mpv', name: 'mpv', description: 'Minimalist video player', category: 'media', packages: { apt: 'mpv', dnf: 'mpv', pacman: 'mpv', yay: 'mpv', brew: 'mpv', winget: null, flatpak: 'io.mpv.Mpv' } },
  { id: 'kodi', name: 'Kodi', description: 'Media center', category: 'media', packages: { apt: 'kodi', dnf: 'kodi', pacman: 'kodi', yay: 'kodi', brew: 'kodi', winget: null, flatpak: 'tv.kodi.Kodi' } },
  { id: 'shotcut', name: 'Shotcut', description: 'Video editor', category: 'media', packages: { apt: 'shotcut', dnf: null, pacman: null, yay: 'shotcut', brew: 'shotcut', winget: 'Meltytech.Shotcut', flatpak: 'org.shotcut.Shotcut' } },
  { id: 'lmms', name: 'LMMS', description: 'Music production', category: 'media', packages: { apt: 'lmms', dnf: 'lmms', pacman: 'lmms', yay: 'lmms', brew: 'lmms', winget: null, flatpak: 'io.lmms.LMMS' } },
  { id: 'darktable', name: 'Darktable', description: 'Photography workflow', category: 'imaging', packages: { apt: 'darktable', dnf: 'darktable', pacman: 'darktable', yay: 'darktable', brew: 'darktable', winget: null, flatpak: 'org.darktable.Darktable' } },
  { id: 'rawtherapee', name: 'RawTherapee', description: 'RAW photo processor', category: 'imaging', packages: { apt: 'rawtherapee', dnf: 'rawtherapee', pacman: 'rawtherapee', yay: 'rawtherapee', brew: 'rawtherapee', winget: null, flatpak: 'com.rawtherapee.RawTherapee' } },
  { id: 'digikam', name: 'digiKam', description: 'Photo management', category: 'imaging', packages: { apt: 'digikam', dnf: 'digikam', pacman: 'digikam', yay: 'digikam', brew: 'digikam', winget: null, flatpak: 'org.kde.digikam' } },
  { id: 'freecad', name: 'FreeCAD', description: '3D parametric modeler', category: 'imaging', packages: { apt: 'freecad', dnf: 'freecad', pacman: 'freecad', yay: 'freecad', brew: 'freecad', winget: 'FreeCAD.FreeCAD', flatpak: 'org.freecadweb.FreeCAD' } },
  { id: 'mypaint', name: 'MyPaint', description: 'Painting app', category: 'imaging', packages: { apt: 'mypaint', dnf: 'mypaint', pacman: 'mypaint', yay: 'mypaint', brew: null, winget: null, flatpak: 'org.mypaint.MyPaint' } },
  { id: 'heroic', name: 'Heroic Games Launcher', description: 'Epic/GOG launcher', category: 'gaming', packages: { apt: null, dnf: null, pacman: null, yay: 'heroic-games-launcher-bin', brew: 'heroic', winget: null, flatpak: 'com.heroicgameslauncher.hgl' } },
  { id: 'lutris', name: 'Lutris', description: 'Open gaming platform', category: 'gaming', packages: { apt: 'lutris', dnf: 'lutris', pacman: 'lutris', yay: 'lutris', brew: null, winget: null, flatpak: 'net.lutris.Lutris' } },
  { id: 'retroarch', name: 'RetroArch', description: 'Multi-system emulator', category: 'gaming', packages: { apt: 'retroarch', dnf: null, pacman: 'retroarch', yay: 'retroarch', brew: 'retroarch', winget: null, flatpak: 'org.libretro.RetroArch' } },
  { id: 'prismlauncher', name: 'Prism Launcher', description: 'Minecraft launcher', category: 'gaming', packages: { apt: null, dnf: null, pacman: null, yay: 'prismlauncher', brew: 'prismlauncher', winget: 'PrismLauncher.PrismLauncher', flatpak: 'org.prismlauncher.PrismLauncher' } },
  { id: 'dolphinemu', name: 'Dolphin Emulator', description: 'GameCube/Wii emulator', category: 'gaming', packages: { apt: 'dolphin-emu', dnf: null, pacman: 'dolphin-emu', yay: 'dolphin-emu', brew: 'dolphin', winget: null, flatpak: 'org.DolphinEmu.dolphin-emu' } },
  { id: 'onlyoffice', name: 'ONLYOFFICE', description: 'Office suite', category: 'docs', packages: { apt: null, dnf: null, pacman: null, yay: 'onlyoffice-bin', brew: 'onlyoffice', winget: 'ONLYOFFICE.DesktopEditors', flatpak: 'org.onlyoffice.desktopeditors' } },
  { id: 'joplin', name: 'Joplin', description: 'Note-taking app', category: 'docs', packages: { apt: null, dnf: null, pacman: null, yay: 'joplin-appimage', brew: 'joplin', winget: 'Joplin.Joplin', flatpak: 'net.cozic.joplin_desktop' } },
  { id: 'logseq', name: 'Logseq', description: 'Knowledge management', category: 'docs', packages: { apt: null, dnf: null, pacman: null, yay: 'logseq-desktop-bin', brew: 'logseq', winget: 'Logseq.Logseq', flatpak: 'com.logseq.Logseq' } },
  { id: 'xournalpp', name: 'Xournal++', description: 'Handwriting notepad', category: 'docs', packages: { apt: 'xournalpp', dnf: 'xournalpp', pacman: 'xournalpp', yay: 'xournalpp', brew: 'xournalpp', winget: null, flatpak: 'com.github.xournalpp.xournalpp' } },
  { id: 'standardnotes', name: 'Standard Notes', description: 'Encrypted notes', category: 'docs', packages: { apt: null, dnf: null, pacman: null, yay: 'standardnotes-bin', brew: 'standard-notes', winget: 'StandardNotes.StandardNotes', flatpak: 'org.standardnotes.standardnotes' } },
  { id: 'flatseal', name: 'Flatseal', description: 'Flatpak permissions manager', category: 'utilities', packages: { apt: null, dnf: null, pacman: null, yay: null, brew: null, winget: null, flatpak: 'com.github.tchx84.Flatseal' } },
  { id: 'bitwarden', name: 'Bitwarden', description: 'Password manager', category: 'utilities', packages: { apt: 'bitwarden', dnf: null, pacman: null, yay: 'bitwarden', brew: 'bitwarden', winget: 'Bitwarden.Bitwarden', flatpak: 'com.bitwarden.desktop' } },
  { id: 'keepassxc', name: 'KeePassXC', description: 'Password manager', category: 'utilities', packages: { apt: 'keepassxc', dnf: 'keepassxc', pacman: 'keepassxc', yay: 'keepassxc', brew: 'keepassxc', winget: 'KeePassXCTeam.KeePassXC', flatpak: 'org.keepassxc.KeePassXC' } },
  { id: 'transmission', name: 'Transmission', description: 'BitTorrent client', category: 'utilities', packages: { apt: 'transmission', dnf: 'transmission', pacman: 'transmission-gtk', yay: 'transmission-gtk', brew: 'transmission', winget: null, flatpak: 'com.transmissionbt.Transmission' } },
  { id: 'bottles', name: 'Bottles', description: 'Run Windows apps via Wine', category: 'utilities', packages: { apt: null, dnf: null, pacman: null, yay: 'bottles', brew: null, winget: null, flatpak: 'com.usebottles.bottles' } },
  { id: 'bleachbit', name: 'BleachBit', description: 'System cleaner', category: 'utilities', packages: { apt: 'bleachbit', dnf: 'bleachbit', pacman: 'bleachbit', yay: 'bleachbit', brew: null, winget: 'BleachBit.BleachBit', flatpak: 'org.bleachbit.BleachBit' } },
  { id: 'impression', name: 'Impression', description: 'Bootable USB creator', category: 'utilities', packages: { apt: null, dnf: null, pacman: null, yay: null, brew: null, winget: null, flatpak: 'io.gitlab.adhami3310.Impression' } },
  { id: 'extmanager', name: 'Extension Manager', description: 'GNOME extension manager', category: 'utilities', packages: { apt: null, dnf: null, pacman: null, yay: null, brew: null, winget: null, flatpak: 'com.mattjakeman.ExtensionManager' } },
])

const selectedTools = ref(new Set())

// ============================================================
// Computed helpers
// ============================================================
const currentOS = computed(() => osOptions.find(o => o.id === selectedOS.value))

const isSupported = (tool) => tool.packages[selectedOS.value] !== null && tool.packages[selectedOS.value] !== undefined

const toggleTool = (tool) => {
  if (!isSupported(tool)) return
  if (selectedTools.value.has(tool.id)) {
    selectedTools.value.delete(tool.id)
  } else {
    selectedTools.value.add(tool.id)
  }
  // Force reactivity on Set
  selectedTools.value = new Set(selectedTools.value)
}

const selectAll = () => {
  tools.value.forEach(t => { if (isSupported(t)) selectedTools.value.add(t.id) })
  selectedTools.value = new Set(selectedTools.value)
}
const clearAll = () => { selectedTools.value = new Set() }

// Generate script lines
const scriptOutput = computed(() => {
  const os = currentOS.value
  if (!os) return ''
  const chosen = tools.value.filter(t => selectedTools.value.has(t.id) && isSupported(t))
  if (chosen.length === 0) return `# No tools selected — pick some from the grid above.\n# OS: ${os.label} (${os.pm})`

  const isWinget = os.id === 'winget'
  if (isWinget) {
    // Winget: one command per tool
    return [
      `# Terminal Installation Script`,
      `# OS: ${os.label}`,
      `# Generated: ${new Date().toLocaleDateString()}\n`,
      ...chosen.map(t => `${os.prefix} ${t.packages[os.id]}`)
    ].join('\n')
  }

  // Unix-style: single command with all packages
  const pkgs = chosen.map(t => t.packages[os.id])
  return [
    `# Terminal Installation Script`,
    `# OS: ${os.label}`,
    `# Generated: ${new Date().toLocaleDateString()}\n`,
    `${os.prefix} ${pkgs.join(' ')}`
  ].join('\n')
})

// Clipboard
const copied = ref(false)
const copyScript = async () => {
  try {
    await navigator.clipboard.writeText(scriptOutput.value)
    copied.value = true
    setTimeout(() => { copied.value = false }, 2000)
  } catch { alert('Copy failed — please copy manually.') }
}

// Category badge colors
const catColor = (cat) => ({
  browser: 'text-orange-400',
  messaging: 'text-indigo-400',
  media: 'text-pink-400',
  dotnet: 'text-purple-500',
  java: 'text-red-500',
  imaging: 'text-yellow-400',
  docs: 'text-blue-400',
  security: 'text-red-400',
  filesharing: 'text-green-500',
  storage: 'text-sky-400',
  other: 'text-gray-400',
  utilities: 'text-cyan-400',
  compression: 'text-yellow-500',
  vcredist: 'text-slate-400',
  dev: 'text-cyber-green',
  gaming: 'text-emerald-400',
}[cat] || 'text-cyber-text-dim')
</script>

<template>
  <div class="min-h-screen bg-cyber-bg text-cyber-text">

    <!-- ================ HEADER ================ -->
    <header class="sticky top-0 z-50 border-b border-cyber-border bg-cyber-bg/80 backdrop-blur-xl">
      <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        <div class="flex items-center gap-3">
          <span class="text-3xl">⚡</span>
          <div>
            <h1 class="text-xl font-extrabold tracking-tight text-cyber-green" style="font-family:'JetBrains Mono',monospace">
              REPOVERSE
            </h1>
            <p class="text-xs text-cyber-text-dim">Terminal Script Generator</p>
          </div>
        </div>
        <span class="hidden text-xs text-cyber-text-dim sm:block">v1.0 — Step 1</span>
      </div>
    </header>

    <main class="mx-auto max-w-7xl px-6 py-8">

      <!-- ================ OS SELECTOR ================ -->
      <section class="mb-10">
        <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-cyber-text-dim">
          Select OS / Package Manager
        </h2>
        <div class="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-7">
          <button
            v-for="os in osOptions"
            :key="os.id"
            @click="selectedOS = os.id; selectedTools = new Set()"
            :class="[
              'group relative flex flex-col items-center gap-2 rounded-xl border px-4 py-4 text-sm font-medium transition-all duration-300 cursor-pointer',
              selectedOS === os.id
                ? 'border-cyber-green bg-cyber-green/10 text-cyber-green shadow-[0_0_20px_rgba(0,255,153,0.15)]'
                : 'border-cyber-border bg-cyber-surface text-cyber-text-dim hover:border-cyber-green/40 hover:bg-cyber-card'
            ]"
          >
            <img :src="os.img" :alt="os.label" class="h-8 w-8 object-contain transition-transform duration-300 group-hover:scale-110" />
            <span class="text-center leading-tight">{{ os.label }}</span>
            <span
              v-if="selectedOS === os.id"
              class="absolute -top-1 -right-1 h-3 w-3 rounded-full bg-cyber-green shadow-[0_0_8px_var(--color-cyber-green)]"
            />
          </button>
        </div>
      </section>

      <!-- ================ MAIN GRID: TOOLS + TERMINAL ================ -->
      <div class="grid gap-8 lg:grid-cols-5">

        <!-- LEFT: TOOL CARDS (3 cols) -->
        <section class="lg:col-span-3">
          <div class="mb-4 flex items-center justify-between">
            <h2 class="text-sm font-semibold uppercase tracking-widest text-cyber-text-dim">
              Available Tools
            </h2>
            <div class="flex gap-2">
              <button @click="selectAll" class="rounded-lg border border-cyber-border bg-cyber-surface px-3 py-1 text-xs text-cyber-green transition hover:bg-cyber-card cursor-pointer">
                Select All
              </button>
              <button @click="clearAll" class="rounded-lg border border-cyber-border bg-cyber-surface px-3 py-1 text-xs text-cyber-red transition hover:bg-cyber-card cursor-pointer">
                Clear
              </button>
            </div>
          </div>

          <div class="grid grid-cols-1 gap-3 sm:grid-cols-2 xl:grid-cols-3">
            <div
              v-for="tool in tools"
              v-show="isSupported(tool)"
              :key="tool.id"
              @click="toggleTool(tool)"
              :class="[
                'relative rounded-xl border p-4 transition-all duration-300 cursor-pointer',
                selectedTools.has(tool.id)
                  ? 'border-cyber-green/60 bg-cyber-green/8 shadow-[0_0_15px_rgba(0,255,153,0.08)]'
                  : 'border-cyber-border bg-cyber-card hover:border-cyber-green/30 hover:bg-cyber-card-hover'
              ]"
            >
              <!-- Checkbox indicator -->
              <div class="absolute top-3 right-3">
                <div
                  :class="[
                    'flex h-5 w-5 items-center justify-center rounded border transition-all',
                    selectedTools.has(tool.id)
                      ? 'border-cyber-green bg-cyber-green text-cyber-bg'
                      : 'border-cyber-border bg-cyber-surface'
                  ]"
                >
                  <svg v-if="selectedTools.has(tool.id) && isSupported(tool)" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
              </div>

              <h3 class="mb-1 text-sm font-bold text-cyber-text">
                {{ tool.name }}
              </h3>
              <p class="mb-2 text-xs leading-relaxed text-cyber-text-dim">
                {{ tool.description }}
              </p>

              <!-- Category badge -->
              <span :class="['text-[10px] font-bold uppercase tracking-wider', catColor(tool.category)]">
                {{ tool.category }}
              </span>

              
            </div>
          </div>
        </section>

        <!-- RIGHT: TERMINAL OUTPUT (2 cols) -->
        <section class="lg:col-span-2">
          <div class="sticky top-24">
            <!-- Terminal chrome -->
            <div class="overflow-hidden rounded-xl border border-cyber-border shadow-2xl shadow-black/40">
              <!-- Title bar -->
              <div class="flex items-center justify-between border-b border-cyber-border bg-cyber-surface px-4 py-2.5">
                <div class="flex items-center gap-2">
                  <span class="h-3 w-3 rounded-full bg-cyber-red/80" />
                  <span class="h-3 w-3 rounded-full bg-yellow-500/80" />
                  <span class="h-3 w-3 rounded-full bg-cyber-green/80" />
                </div>
                <span class="text-xs text-cyber-text-dim" style="font-family:'JetBrains Mono',monospace">
                  {{ currentOS?.pm || 'shell' }} — bash
                </span>
                <button
                  @click="copyScript"
                  :class="[
                    'flex items-center gap-1.5 rounded-lg border px-3 py-1 text-xs font-medium transition-all duration-300 cursor-pointer',
                    copied
                      ? 'border-cyber-green/60 bg-cyber-green/20 text-cyber-green'
                      : 'border-cyber-border bg-cyber-card text-cyber-text-dim hover:border-cyber-green/40 hover:text-cyber-green'
                  ]"
                >
                  <svg v-if="!copied" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>
                  </svg>
                  <svg v-else class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/>
                  </svg>
                  {{ copied ? 'Copied!' : 'Copy' }}
                </button>
              </div>
              <!-- Terminal body -->
              <div class="min-h-[300px] bg-cyber-terminal p-4 lg:min-h-[450px]">
                <pre class="whitespace-pre-wrap break-all text-sm leading-relaxed text-cyber-green" style="font-family:'JetBrains Mono',monospace">{{ scriptOutput }}</pre>
                <span class="mt-2 inline-block h-4 w-2 animate-pulse bg-cyber-green/70" />
              </div>
            </div>

            <!-- Stats bar -->
            <div class="mt-3 flex items-center justify-between rounded-lg border border-cyber-border bg-cyber-surface px-4 py-2 text-xs text-cyber-text-dim">
              <span>{{ selectedTools.size }} tool{{ selectedTools.size !== 1 ? 's' : '' }} selected</span>
              <span>{{ currentOS?.label }}</span>
            </div>
          </div>
        </section>
      </div>
    </main>

    <!-- ================ FOOTER ================ -->
    <footer class="mt-16 border-t border-cyber-border bg-cyber-surface/50 py-6 text-center text-xs text-cyber-text-dim">
      REPOVERSE © {{ new Date().getFullYear() }} — Built for developers & cybersecurity professionals
    </footer>
  </div>
</template>
