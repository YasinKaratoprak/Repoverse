import { ref, computed, watch } from 'vue'
import toolsData from './data/tools.js'
import repoSetup from './data/repos.js'

// ============================================================
// Persistence & shared links
// ============================================================
const STORAGE_KEY = 'repoverse-state'
const validIds = new Set(toolsData.map(t => t.id))

const loadState = () => {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}
  } catch {
    return {}
  }
}
const saved = loadState()

// A shared link (?os=apt&tools=a,b,c) overrides the locally saved state
const urlParams = new URLSearchParams(window.location.search)
const urlOS = urlParams.get('os')
const urlTools = (urlParams.get('tools') || '').split(',').filter(id => validIds.has(id))
if (urlParams.has('os') || urlParams.has('tools')) {
  // Strip the query so a later refresh keeps the user's own edits
  history.replaceState(null, '', window.location.pathname)
}

// ============================================================
// State
// ============================================================
export const tools = ref(toolsData)
export const selectedOS = ref(urlOS || saved.os || 'apt')
export const selectedTools = ref(new Set(
  urlTools.length ? urlTools : (Array.isArray(saved.tools) ? saved.tools.filter(id => validIds.has(id)) : [])
))
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

// Fall back to apt if the persisted OS id is no longer valid
if (!osOptions.some(o => o.id === selectedOS.value)) selectedOS.value = 'apt'

// Persist OS + tool selections across sessions
watch([selectedOS, selectedTools], () => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ os: selectedOS.value, tools: [...selectedTools.value] }))
  } catch { /* storage unavailable (private mode etc.) */ }
})

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

  const header = [
    `# Repoverse — Terminal Installation Script`,
    `# OS: ${os.label}`,
    `# Generated: ${new Date().toLocaleDateString()}\n`,
  ]

  // Winget runs in PowerShell/cmd — no shebang, one command per package
  if (os.id === 'winget') {
    return [...header, ...chosen.map(t => `${os.prefix} ${t.packages[os.id]}`)].join('\n')
  }

  const lines = ['#!/usr/bin/env bash', 'set -e\n', ...header]

  // Register third-party repos (Chrome, VS Code, Spotify, ...) before installing
  const repoTools = chosen.filter(t => repoSetup[t.id]?.[os.id])
  if (repoTools.length > 0) {
    lines.push('# --- Third-party repositories ---')
    if (os.id === 'apt') lines.push('sudo install -d -m 0755 /etc/apt/keyrings')
    for (const t of repoTools) {
      lines.push(`# ${t.name}`)
      lines.push(...repoSetup[t.id][os.id])
    }
    lines.push('')
  }

  if (os.id === 'apt') lines.push('sudo apt update')
  const pkgs = chosen.map(t => t.packages[os.id])
  lines.push(`${os.prefix} ${pkgs.join(' ')}`)
  return lines.join('\n')
})

// ============================================================
// Share link — encodes current OS + selections into a URL
// ============================================================
export const shareUrl = computed(() => {
  const base = `${window.location.origin}${window.location.pathname}`
  const ids = [...selectedTools.value].join(',')
  return ids ? `${base}?os=${selectedOS.value}&tools=${ids}` : `${base}?os=${selectedOS.value}`
})
