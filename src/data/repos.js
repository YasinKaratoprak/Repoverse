// ============================================================
// Third-party repository setup for packages that are NOT in the
// default apt/dnf repositories. Keyed by tool id — each entry maps
// a package manager id to the shell lines that register the repo.
// The generated script runs these before `apt update` / `dnf install`.
// ============================================================

export default {
  chrome: {
    apt: [
      'wget -qO- https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --yes --dearmor -o /etc/apt/keyrings/google-chrome.gpg',
      'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] https://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list > /dev/null',
    ],
    dnf: [
      "printf '[google-chrome]\\nname=Google Chrome\\nbaseurl=https://dl.google.com/linux/chrome/rpm/stable/x86_64\\nenabled=1\\ngpgcheck=1\\ngpgkey=https://dl.google.com/linux/linux_signing_key.pub\\n' | sudo tee /etc/yum.repos.d/google-chrome.repo > /dev/null",
    ],
  },
  opera: {
    apt: [
      'wget -qO- https://deb.opera.com/archive.key | sudo gpg --yes --dearmor -o /etc/apt/keyrings/opera.gpg',
      'echo "deb [signed-by=/etc/apt/keyrings/opera.gpg] https://deb.opera.com/opera-stable/ stable non-free" | sudo tee /etc/apt/sources.list.d/opera-stable.list > /dev/null',
    ],
    dnf: [
      'sudo rpm --import https://rpm.opera.com/rpmrepo.key',
      "printf '[opera]\\nname=Opera packages\\ntype=rpm-md\\nbaseurl=https://rpm.opera.com/rpm\\nenabled=1\\ngpgcheck=1\\ngpgkey=https://rpm.opera.com/rpmrepo.key\\n' | sudo tee /etc/yum.repos.d/opera.repo > /dev/null",
    ],
  },
  edge: {
    apt: [
      'wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --yes --dearmor -o /etc/apt/keyrings/microsoft-edge.gpg',
      'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft-edge.gpg] https://packages.microsoft.com/repos/edge stable main" | sudo tee /etc/apt/sources.list.d/microsoft-edge.list > /dev/null',
    ],
    dnf: [
      'sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc',
      "printf '[microsoft-edge]\\nname=Microsoft Edge\\nbaseurl=https://packages.microsoft.com/yumrepos/edge\\nenabled=1\\ngpgcheck=1\\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc\\n' | sudo tee /etc/yum.repos.d/microsoft-edge.repo > /dev/null",
    ],
  },
  brave: {
    apt: [
      'sudo wget -qO /etc/apt/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg',
      'echo "deb [signed-by=/etc/apt/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list > /dev/null',
    ],
    dnf: [
      'sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc',
      'curl -fsS https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo | sudo tee /etc/yum.repos.d/brave-browser.repo > /dev/null',
    ],
  },
  vivaldi: {
    apt: [
      'wget -qO- https://repo.vivaldi.com/archive/linux_signing_key.pub | sudo gpg --yes --dearmor -o /etc/apt/keyrings/vivaldi.gpg',
      'echo "deb [signed-by=/etc/apt/keyrings/vivaldi.gpg] https://repo.vivaldi.com/archive/deb/ stable main" | sudo tee /etc/apt/sources.list.d/vivaldi.list > /dev/null',
    ],
    dnf: [
      'sudo rpm --import https://repo.vivaldi.com/archive/linux_signing_key.pub',
      "printf '[vivaldi]\\nname=Vivaldi\\nbaseurl=https://repo.vivaldi.com/archive/rpm/x86_64\\nenabled=1\\ngpgcheck=1\\ngpgkey=https://repo.vivaldi.com/archive/linux_signing_key.pub\\n' | sudo tee /etc/yum.repos.d/vivaldi.repo > /dev/null",
    ],
  },
  spotify: {
    apt: [
      'wget -qO- https://download.spotify.com/debian/pubkey_C85668DF69375001.gpg | sudo gpg --yes --dearmor -o /etc/apt/keyrings/spotify.gpg',
      'echo "deb [signed-by=/etc/apt/keyrings/spotify.gpg] http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list > /dev/null',
    ],
  },
  vscode: {
    apt: [
      'wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --yes --dearmor -o /etc/apt/keyrings/microsoft.gpg',
      'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null',
    ],
    dnf: [
      'sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc',
      "printf '[code]\\nname=Visual Studio Code\\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\\nenabled=1\\ngpgcheck=1\\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc\\n' | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null",
    ],
  },
  signal: {
    apt: [
      'wget -qO- https://updates.signal.org/desktop/apt/keys.asc | sudo gpg --yes --dearmor -o /etc/apt/keyrings/signal-desktop.gpg',
      'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/signal-desktop.gpg] https://updates.signal.org/desktop/apt xenial main" | sudo tee /etc/apt/sources.list.d/signal-xenial.list > /dev/null',
    ],
  },
  element: {
    apt: [
      'sudo wget -qO /etc/apt/keyrings/element-io-archive-keyring.gpg https://packages.element.io/debian/element-io-archive-keyring.gpg',
      'echo "deb [signed-by=/etc/apt/keyrings/element-io-archive-keyring.gpg] https://packages.element.io/debian/ default main" | sudo tee /etc/apt/sources.list.d/element-io.list > /dev/null',
    ],
  },
}
