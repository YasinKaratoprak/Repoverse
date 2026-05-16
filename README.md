# Repoverse

A fast, client-side web app that generates bash/terminal installation scripts for your favorite operating systems and package managers. 

Pick your OS (Ubuntu, Fedora, Arch, Mac, Windows, etc.), select the tools you want from the grid, and copy the generated one-liner straight into your terminal. No more hunting down package names manually.

## Features

- **Multi-OS Support**: Handles `apt`, `dnf`, `pacman`, `yay`, `brew`, `winget`, and `flatpak`.
- **Massive Tool DB**: Comes with 200+ built-in packages, including a heavy focus on cybersecurity and pentesting tools.
- **Smart Filtering**: Automatically hides apps that don't exist for the package manager you selected. 
- **Persisted State**: Switching from `apt` to `flatpak` keeps your selections intact.
- **Built with Vue 3**: Uses the Composition API, Tailwind CSS, and Vite for a very fast dev experience.

## Getting Started

Make sure you have Node.js installed, then clone the repo and spin it up:

```bash
npm install
npm run dev
```

The site will run on `localhost:5173`. 

## Adding new tools

The database lives in `src/data/tools.js`. If you want to add a new package, just follow the existing object structure. You'll need to define the package names for whatever package managers support it. If a tool doesn't support a specific package manager, just set that field to `null`.

If you're doing bulk imports, check the `scripts/` folder for some Python helpers used to generate entries.

## Contact
Yasin Karatoprak - [contact@yasinkaratoprak.com](mailto:contact@yasinkaratoprak.com)
