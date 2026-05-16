import { ref, computed } from 'vue'
import toolsData from './data/tools.js'

// ============================================================
// State
// ============================================================
export const tools = ref(toolsData)
export const selectedOS = ref('apt')
export const selectedTools = ref(new Set())
export const searchQuery = ref('')
export const selectedCategory = ref('all')

export const osOptions = [
  { id: 'apt', label: 'Ubuntu / Debian', img: '/images/ubuntu.png', pm: 'apt', prefix: 'sudo apt install -y' },
  { id: 'dnf', label: 'Fedora', img: '/images/Fedora.png', pm: 'dnf', prefix: 'sudo dnf install -y' },
  { id: 'pacman', label: 'Arch (pacman)', img: '/images/pacman.png', pm: 'pacman', prefix: 'sudo pacman -S --noconfirm' },
  { id: 'yay', label: 'Arch (AUR / yay)', img: '/images/pacman.png', pm: 'yay', prefix: 'yay -S --noconfirm' },
  { id: 'brew', label: 'macOS (Brew)', img: '/images/homebrew.png', pm: 'brew', prefix: 'brew install' },
  { id: 'winget', label: 'Windows (Winget)', img: '/images/windows.png', pm: 'winget', prefix: 'winget install -e --id' },
  { id: 'flatpak', label: 'Universal (Flatpak)', img: '/images/flatpak.png', pm: 'flatpak', prefix: 'flatpak install -y flathub' },
]

export const categoryLabels = {
  browser: '🌐 Browsers',
  messaging: '💬 Messaging',
  media: '🎵 Media',
  dotnet: '🔷 .NET',
  java: '☕ Java',
  imaging: '🎨 Imaging',
  docs: '📄 Documents',
  security: '🔒 Security',
  filesharing: '📤 File Sharing',
  storage: '☁️ Storage',
  other: '📦 Other',
  utilities: '🔧 Utilities',
  compression: '🗜️ Compression',
  vcredist: '⚙️ VC Redist',
  dev: '💻 Development',
  gaming: '🎮 Gaming',
  infogathering: '🔍 Info Gathering',
  vulnanalysis: '🛡️ Vuln Analysis',
  webapps: '🌐 Web Apps',
  wireless: '📡 Wireless Attacks',
  exploitation: '💥 Exploitation',
  password: '🔑 Password Attacks',
  forensics: '🔬 Forensics',
  sniffing: '🕵️ Sniffing & Spoofing',
  reverseengineering: '🔄 Reverse Eng',
  maintainingaccess: '🚪 Maintaining Access',
  socialengineering: '🎣 Social Engineering',
}

export const catColor = (cat) => ({
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
  dev: 'text-ui-primary',
  gaming: 'text-emerald-400',
  infogathering: 'text-cyan-400',
  vulnanalysis: 'text-orange-500',
  webapps: 'text-blue-500',
  wireless: 'text-indigo-400',
  exploitation: 'text-red-500',
  password: 'text-yellow-500',
  forensics: 'text-purple-400',
  sniffing: 'text-teal-400',
  reverseengineering: 'text-pink-500',
  maintainingaccess: 'text-green-600',
  socialengineering: 'text-rose-400',
}[cat] || 'text-ui-text-muted')

export const categories = computed(() => {
  const cats = [...new Set(tools.value.map(t => t.category))]
  cats.sort()
  return cats
})

export const currentOS = computed(() => osOptions.find(o => o.id === selectedOS.value))

export const isSupported = (tool) => tool.packages[selectedOS.value] !== null && tool.packages[selectedOS.value] !== undefined

export const filteredTools = computed(() => {
  let result = tools.value.filter(t => t.packages[selectedOS.value] !== null && t.packages[selectedOS.value] !== undefined)
  if (selectedCategory.value !== 'all') {
    result = result.filter(t => t.category === selectedCategory.value)
  }
  const query = searchQuery.value.trim().toLowerCase()
  if (query) {
    result = result.filter(t =>
      t.name.toLowerCase().includes(query) ||
      t.description.toLowerCase().includes(query) ||
      t.category.toLowerCase().includes(query)
    )
  }
  return result
})

export const selectedToolsList = computed(() => tools.value.filter(t => selectedTools.value.has(t.id)))

export const toggleTool = (tool) => {
  if (!isSupported(tool)) return
  if (selectedTools.value.has(tool.id)) {
    selectedTools.value.delete(tool.id)
  } else {
    selectedTools.value.add(tool.id)
  }
  selectedTools.value = new Set(selectedTools.value)
}

export const selectAll = () => {
  filteredTools.value.forEach(t => { if (isSupported(t)) selectedTools.value.add(t.id) })
  selectedTools.value = new Set(selectedTools.value)
}

export const clearAll = () => { selectedTools.value = new Set() }

export const scriptOutput = computed(() => {
  const os = currentOS.value
  if (!os) return ''
  const chosen = tools.value.filter(t => selectedTools.value.has(t.id) && isSupported(t))
  if (chosen.length === 0) return `# No tools selected — pick some from the grid above.\n# OS: ${os.label} (${os.pm})`

  const isWinget = os.id === 'winget'
  if (isWinget) {
    return [
      `# Terminal Installation Script`,
      `# OS: ${os.label}`,
      `# Generated: ${new Date().toLocaleDateString()}\n`,
      ...chosen.map(t => `${os.prefix} ${t.packages[os.id]}`)
    ].join('\n')
  }

  const pkgs = chosen.map(t => t.packages[os.id])
  return [
    `# Terminal Installation Script`,
    `# OS: ${os.label}`,
    `# Generated: ${new Date().toLocaleDateString()}\n`,
    `${os.prefix} ${pkgs.join(' ')}`
  ].join('\n')
})
