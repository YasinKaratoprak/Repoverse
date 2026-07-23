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
      <h2 class="text-sm font-semibold uppercase tracking-widest text-ui-text-muted">
        Available Tools
      </h2>
      <div class="flex gap-2">
        <button @click="selectAll" class="cursor-pointer rounded-lg border border-ui-border bg-ui-surface px-3 py-1 text-xs text-ui-primary transition hover:bg-ui-card">
          Select All
        </button>
        <button @click="clearAll" class="cursor-pointer rounded-lg border border-ui-border bg-ui-surface px-3 py-1 text-xs text-ui-danger transition hover:bg-ui-card">
          Clear
        </button>
      </div>
    </div>

    <!-- Search Input -->
    <div class="relative mb-4">
      <svg class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-ui-text-muted" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search tools..."
        class="w-full rounded-xl border border-ui-border bg-ui-surface py-2.5 pl-10 pr-4 text-sm text-ui-text placeholder-ui-text-muted outline-none transition-all duration-300 focus:border-ui-primary/60 focus:shadow-sm"
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
            ? 'border-ui-primary bg-ui-primary/15 text-ui-primary shadow-sm'
            : 'border-ui-border bg-ui-surface text-ui-text-muted hover:border-ui-primary/40 hover:text-ui-text'
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
            ? 'border-ui-primary bg-ui-primary/15 text-ui-primary shadow-sm'
            : 'border-ui-border bg-ui-surface text-ui-text-muted hover:border-ui-primary/40 hover:text-ui-text'
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
        role="button"
        tabindex="0"
        :aria-pressed="selectedTools.has(tool.id)"
        @click="toggleTool(tool)"
        @keydown.enter.prevent="toggleTool(tool)"
        @keydown.space.prevent="toggleTool(tool)"
        :class="[
          'cursor-pointer relative rounded-xl border p-4 outline-none transition-all duration-300 focus-visible:ring-2 focus-visible:ring-ui-primary/60',
          selectedTools.has(tool.id)
            ? 'border-ui-primary/60 bg-ui-primary/8 shadow-sm'
            : 'border-ui-border bg-ui-card hover:border-ui-primary/30 hover:bg-ui-hover'
        ]"
      >
        <!-- Checkbox indicator -->
        <div class="absolute right-3 top-3">
          <div
            :class="[
              'flex h-5 w-5 items-center justify-center rounded border transition-all',
              selectedTools.has(tool.id)
                ? 'border-ui-primary bg-ui-primary text-ui-bg'
                : 'border-ui-border bg-ui-surface'
            ]"
          >
            <svg v-if="selectedTools.has(tool.id)" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
              <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
            </svg>
          </div>
        </div>

        <h3 class="mb-1 text-sm font-bold text-ui-text">
          {{ tool.name }}
        </h3>
        <p class="mb-2 text-xs leading-relaxed text-ui-text-muted">
          {{ tool.description }}
        </p>

        <!-- Category badge -->
        <span :class="['text-[10px] font-bold uppercase tracking-wider', catColor(tool.category)]">
          {{ tool.category }}
        </span>
      </div>
    </div>

    <!-- Empty state for search/filter -->
    <div v-if="filteredTools.length === 0" class="mt-8 flex flex-col items-center justify-center rounded-xl border border-dashed border-ui-border py-12 text-center">
      <span class="mb-2 text-3xl">🔍</span>
      <p class="text-sm text-ui-text-muted">No tools match your search or filter.</p>
      <button
        @click="searchQuery = ''; selectedCategory = 'all'"
        class="cursor-pointer mt-3 rounded-lg border border-ui-primary/40 bg-ui-primary/10 px-4 py-1.5 text-xs font-medium text-ui-primary transition hover:bg-ui-primary/20"
      >
        Clear Filters
      </button>
    </div>
  </section>
</template>
