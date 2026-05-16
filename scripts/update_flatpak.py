import re

file_path = 'src/App.vue'
with open(file_path, 'r') as f:
    content = f.read()

# Add flatpak to osOptions
if "{ id: 'flatpak'" not in content:
    content = content.replace(
        "{ id: 'winget', label: 'Windows (Winget)', icon: '🪟', pm: 'winget', prefix: 'winget install -e --id' },",
        "{ id: 'winget', label: 'Windows (Winget)', icon: '🪟', pm: 'winget', prefix: 'winget install -e --id' },\n  { id: 'flatpak', label: 'Universal (Flatpak)', icon: '📦', pm: 'flatpak', prefix: 'flatpak install -y flathub' },"
    )
    # Update grid cols for better layout
    content = content.replace("lg:grid-cols-6", "lg:grid-cols-7")

# Define Flatpak IDs
flatpak_ids = {
    'wireshark': "'org.wireshark.Wireshark'",
    'vscode': "'com.visualstudio.code'",
    'chrome': "'com.google.Chrome'",
    'firefox': "'org.mozilla.firefox'",
    'brave': "'com.brave.Browser'",
    'spotify': "'com.spotify.Client'",
    'vlc': "'org.videolan.VLC'",
    'discord': "'com.discordapp.Discord'",
    'telegram': "'org.telegram.desktop'",
    'obsidian': "'md.obsidian.Obsidian'",
    'steam': "'com.valvesoftware.Steam'",
    'neovim': "'io.neovim.nvim'",
    'postman': "'com.getpostman.Postman'",
    'insomnia': "'rest.insomnia.Insomnia'",
    'dbeaver': "'io.dbeaver.DBeaverCommunity'",
    'intellij': "'com.jetbrains.IntelliJ-IDEA-Community'",
    'androidstudio': "'com.google.AndroidStudio'",
    'alacritty': "'org.alacritty.Alacritty'",
}

# Find all packages objects
def update_packages(match):
    full_block = match.group(0)
    
    # Extract tool ID
    id_match = re.search(r"id:\s*'([^']+)'", full_block)
    if not id_match:
        return full_block
        
    tool_id = id_match.group(1)
    flatpak_val = flatpak_ids.get(tool_id, "null")
    
    if "flatpak:" in full_block:
        return full_block
        
    # Replace packages: { apt: 'xxx', ... }
    # using simple regex
    new_block = re.sub(r"(packages:\s*\{[^\}]+)(\})", r"\1, flatpak: " + flatpak_val + r" \2", full_block)
    return new_block

# Apply update to all tool objects
tools_block_match = re.search(r'const tools = ref\(\[([\s\S]*?)\]\)', content)
if tools_block_match:
    tools_block = tools_block_match.group(1)
    
    # Split tools by '},' or similar? We can just find all packages objects
    new_content = re.sub(r'\{[\s\S]*?packages:\s*\{[^\}]+\}[\s\S]*?\}', update_packages, content)
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    print("Done applying flatpak")
else:
    print("Could not find tools ref block")
