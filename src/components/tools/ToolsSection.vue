<script setup>
import { 
  searchQuery, selectedCategory, categories, categoryLabels, 
  filteredTools, toggleTool, selectedTools, isSupported, catColor,
  selectAll, clearAll
} from '../../store.js'
</script>

<template>
  <section class="lg:col-span-2">
    <div class="mb-4 flex items-center justify-between">
      <h2 class="text-sm font-semibold uppercase tracking-widest text-cyber-text-dim">
        Available Tools
      </h2>
      <div class="flex gap-2">
        <button @click="selectAll" class="cursor-pointer rounded-lg border border-cyber-border bg-cyber-surface px-3 py-1 text-xs text-cyber-green transition hover:bg-cyber-card">
          Select All
        </button>
        <button @click="clearAll" class="cursor-pointer rounded-lg border border-cyber-border bg-cyber-surface px-3 py-1 text-xs text-cyber-red transition hover:bg-cyber-card">
          Clear
        </button>
      </div>
    </div>

    <!-- Search Input -->
    <div class="relative mb-4">
      <svg class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-cyber-text-dim" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search tools..."
        class="w-full rounded-xl border border-cyber-border bg-cyber-surface py-2.5 pl-10 pr-4 text-sm text-cyber-text placeholder-cyber-text-dim outline-none transition-all duration-300 focus:border-cyber-green/60 focus:shadow-[0_0_15px_rgba(0,255,153,0.1)]"
        style="font-family:'Inter',sans-serif"
      />
    </div>

    <!-- Category Pills -->
    <div class="mb-5 flex flex-wrap gap-2">
      <button
        @click="selectedCategory = 'all'"
        :class="[
          'cursor-pointer rounded-full border px-3 py-1.5 text-xs font-medium transition-all duration-300',
          selectedCategory === 'all'
            ? 'border-cyber-green bg-cyber-green/15 text-cyber-green shadow-[0_0_10px_rgba(0,255,153,0.1)]'
            : 'border-cyber-border bg-cyber-surface text-cyber-text-dim hover:border-cyber-green/40 hover:text-cyber-text'
        ]"
      >
        🏷️ All
      </button>
      <button
        v-for="cat in categories"
        :key="cat"
        @click="selectedCategory = cat"
        :class="[
          'cursor-pointer rounded-full border px-3 py-1.5 text-xs font-medium transition-all duration-300',
          selectedCategory === cat
            ? 'border-cyber-green bg-cyber-green/15 text-cyber-green shadow-[0_0_10px_rgba(0,255,153,0.1)]'
            : 'border-cyber-border bg-cyber-surface text-cyber-text-dim hover:border-cyber-green/40 hover:text-cyber-text'
        ]"
      >
        {{ categoryLabels[cat] || cat }}
      </button>
    </div>

    <!-- Tool Cards Grid -->
    <div class="grid grid-cols-1 gap-3 sm:grid-cols-2 xl:grid-cols-3">
      <div
        v-for="tool in filteredTools"
        :key="tool.id"
        @click="toggleTool(tool)"
        :class="[
          'cursor-pointer relative rounded-xl border p-4 transition-all duration-300',
          selectedTools.has(tool.id)
            ? 'border-cyber-green/60 bg-cyber-green/8 shadow-[0_0_15px_rgba(0,255,153,0.08)]'
            : 'border-cyber-border bg-cyber-card hover:border-cyber-green/30 hover:bg-cyber-card-hover'
        ]"
      >
        <!-- Checkbox indicator -->
        <div class="absolute right-3 top-3">
          <div
            :class="[
              'flex h-5 w-5 items-center justify-center rounded border transition-all',
              selectedTools.has(tool.id)
                ? 'border-cyber-green bg-cyber-green text-cyber-bg'
                : 'border-cyber-border bg-cyber-surface'
            ]"
          >
            <svg v-if="selectedTools.has(tool.id)" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
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

    <!-- Empty state for search/filter -->
    <div v-if="filteredTools.length === 0" class="mt-8 flex flex-col items-center justify-center rounded-xl border border-dashed border-cyber-border py-12 text-center">
      <span class="mb-2 text-3xl">🔍</span>
      <p class="text-sm text-cyber-text-dim">No tools match your search or filter.</p>
      <button
        @click="searchQuery = ''; selectedCategory = 'all'"
        class="cursor-pointer mt-3 rounded-lg border border-cyber-green/40 bg-cyber-green/10 px-4 py-1.5 text-xs font-medium text-cyber-green transition hover:bg-cyber-green/20"
      >
        Clear Filters
      </button>
    </div>
  </section>
</template>
