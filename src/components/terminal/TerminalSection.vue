<script setup>
import { ref } from 'vue'
import { selectedTools, selectedToolsList, toggleTool, scriptOutput, currentOS } from '../../store.js'

const showSelectedApps = ref(false)
const copied = ref(false)

const copyScript = async () => {
  try {
    await navigator.clipboard.writeText(scriptOutput.value)
    copied.value = true
    setTimeout(() => { copied.value = false }, 2000)
  } catch { alert('Copy failed — please copy manually.') }
}
</script>

<template>
  <section class="lg:col-span-1">
    <div class="sticky top-24">
      
      <!-- Selected Apps Dropdown -->
      <div class="mb-4 overflow-hidden rounded-xl border border-ui-border bg-ui-surface">
        <button 
          @click="showSelectedApps = !showSelectedApps" 
          class="flex w-full cursor-pointer items-center justify-between px-4 py-3 text-sm font-medium text-ui-text transition hover:bg-ui-card"
        >
          <div class="flex items-center gap-2">
            <span class="text-ui-primary">📦</span>
            <span>Selected Apps</span>
            <span class="rounded bg-ui-primary/20 px-2 py-0.5 text-xs text-ui-primary">{{ selectedTools.size }}</span>
          </div>
          <svg :class="['h-4 w-4 transition-transform duration-300', showSelectedApps ? 'rotate-180' : '']" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </button>
        
        <div v-show="showSelectedApps" class="max-h-60 overflow-y-auto border-t border-ui-border bg-ui-card p-2">
          <div v-if="selectedToolsList.length === 0" class="p-4 text-center text-xs text-ui-text-muted">
            No apps selected yet.
          </div>
          <ul v-else class="flex flex-col gap-1">
            <li v-for="tool in selectedToolsList" :key="tool.id" class="flex items-center justify-between rounded p-2 text-xs transition-colors hover:bg-ui-surface">
              <div class="flex flex-col">
                <span class="font-bold text-ui-text">{{ tool.name }}</span>
                <span class="text-[9px] text-ui-text-muted uppercase tracking-wider">{{ tool.category }}</span>
              </div>
              <button @click="toggleTool(tool)" class="cursor-pointer p-1 text-ui-danger transition hover:text-red-400">
                <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </li>
          </ul>
        </div>
      </div>

      <!-- Terminal chrome -->
      <div class="overflow-hidden rounded-xl border border-ui-border shadow-2xl shadow-black/40">
        <!-- Title bar -->
        <div class="flex items-center justify-between border-b border-ui-border bg-ui-surface px-4 py-2.5">
          <div class="flex items-center gap-2">
            <span class="h-3 w-3 rounded-full bg-ui-danger/80" />
            <span class="h-3 w-3 rounded-full bg-yellow-500/80" />
            <span class="h-3 w-3 rounded-full bg-ui-primary/80" />
          </div>
          <span class="text-xs text-ui-text-muted" style="font-family:'JetBrains Mono',monospace">
            {{ currentOS?.pm || 'shell' }} — bash
          </span>
          <button
            @click="copyScript"
            :class="[
              'flex cursor-pointer items-center gap-1.5 rounded-lg border px-3 py-1 text-xs font-medium transition-all duration-300',
              copied
                ? 'border-ui-primary/60 bg-ui-primary/20 text-ui-primary'
                : 'border-ui-border bg-ui-card text-ui-text-muted hover:border-ui-primary/40 hover:text-ui-primary'
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
        <div class="min-h-[300px] bg-ui-terminal p-4 lg:min-h-[450px]">
          <pre class="whitespace-pre-wrap break-all text-sm leading-relaxed text-ui-primary" style="font-family:'JetBrains Mono',monospace">{{ scriptOutput }}</pre>
          <span class="mt-2 inline-block h-4 w-2 animate-pulse bg-ui-primary/70" />
        </div>
      </div>

      <!-- Stats bar -->
      <div class="mt-3 flex items-center justify-between rounded-lg border border-ui-border bg-ui-surface px-4 py-2 text-xs text-ui-text-muted">
        <span>{{ selectedTools.size }} tool{{ selectedTools.size !== 1 ? 's' : '' }} selected</span>
        <span>{{ currentOS?.label }}</span>
      </div>
    </div>
  </section>
</template>
