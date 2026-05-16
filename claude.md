# Repoverse - Project Documentation & Architecture

## Project Overview
Repoverse is a sleek, modern Vue 3 web application designed to generate terminal installation scripts for a wide variety of operating systems and package managers (Apt, Dnf, Pacman, Yay, Brew, Winget, Flatpak). Tailored for developers and cybersecurity professionals, the application features an extensive suite of over 200 software packages, spanning from standard utilities to highly specialized penetration testing frameworks.

## Technical Architecture

The application was built following modern enterprise standards, emphasizing a strictly decoupled, highly-cohesive Vue 3 Composition API architecture.

### 📁 Directory Structure
```text
.
├── scripts/               # Python utility scripts for database generation and maintenance
├── src/
│   ├── components/        # Highly-cohesive UI components
│   │   ├── layout/        # AppHeader.vue, AppFooter.vue
│   │   ├── os/            # OsSelector.vue (Handles platform switching)
│   │   ├── terminal/      # TerminalSection.vue (Script preview & Selected Apps dropdown)
│   │   └── tools/         # ToolsSection.vue (Grid, Search, and Category Filtering)
│   ├── data/              # Static data sources
│   │   └── tools.js       # The centralized Repoverse tool database (~200+ entries)
│   ├── App.vue            # Root layout orchestrator
│   ├── main.js            # Vue entry point
│   ├── store.js           # Centralized reactive state store (Composition API)
│   └── style.css          # Tailwind CSS & global styles
├── index.html             # HTML entry point
├── package.json           # Node.js dependencies
└── vite.config.js         # Vite bundler configuration
```

### 🧠 State Management (`src/store.js`)
Instead of prop-drilling or relying on a monolithic `App.vue`, the application utilizes a lightweight, native Vue Composition API store (`src/store.js`). This module exports reactive references (`ref`) and derived data (`computed`) that handle:
- **Platform Selection:** `selectedOS`, `osOptions`
- **Tool Data & Filtering:** `searchQuery`, `selectedCategory`, `filteredTools`
- **Selection State:** `selectedTools` (Set), logic to `toggleTool()`, `selectAll()`, `clearAll()`
- **Terminal Generation:** Dynamic `scriptOutput` computed property formatting bash payloads.

### 🛡️ Feature Highlights
1. **Dynamic OS Filtering:** Tools that are unsupported on the currently active operating system are instantly removed from the UI grid, ensuring users only build valid installation scripts.
2. **Advanced Search & Categorization:** Users can search across titles, descriptions, and categories in real-time, or use emoji-labeled pill filters to isolate specific domains (e.g., *Forensics*, *Web Apps*, *Messaging*).
3. **Cybersecurity Integration:** The database ships with ~90 specialized penetration testing and info-sec tools.
4. **Selected Apps Analysis:** An interactive accordion menu in the terminal panel allows users to quickly audit and remove selected packages prior to script generation.
5. **State Preservation:** Selections are cached in a persistent global state, preventing data loss when pivoting between package managers (e.g., building a hybrid Ubuntu/Flatpak script).

## Development
- **Framework:** Vue 3 (Composition API)
- **Styling:** Tailwind CSS + Custom Cyberpunk UI tokens
- **Build Tool:** Vite

### Running Locally
```bash
npm install
npm run dev
```
