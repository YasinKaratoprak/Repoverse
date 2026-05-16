<script setup>
import AppHeader from './components/layout/AppHeader.vue'
import AppFooter from './components/layout/AppFooter.vue'
import OsSelector from './components/os/OsSelector.vue'
import ToolsSection from './components/tools/ToolsSection.vue'
import TerminalSection from './components/terminal/TerminalSection.vue'
</script>

<template>
  <div class="min-h-screen bg-ui-bg text-ui-text">
    <AppHeader />

    <main class="mx-auto max-w-7xl px-6 py-8">
      <OsSelector />

      <div class="grid gap-8 lg:grid-cols-3">
        <ToolsSection />
        <TerminalSection />
      </div>
    </main>

    <AppFooter />
  </div>
</template>
