<script setup>
import { osOptions, selectedOS } from '../../store.js'
</script>

<template>
  <section class="mb-10">
    <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-cyber-text-dim">
      Select OS / Package Manager
    </h2>
    <div class="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-7">
      <button
        v-for="os in osOptions"
        :key="os.id"
        @click="selectedOS = os.id"
        :class="[
          'group relative flex cursor-pointer flex-col items-center gap-2 rounded-xl border px-4 py-4 text-sm font-medium transition-all duration-300',
          selectedOS === os.id
            ? 'border-cyber-green bg-cyber-green/10 text-cyber-green shadow-[0_0_20px_rgba(0,255,153,0.15)]'
            : 'border-cyber-border bg-cyber-surface text-cyber-text-dim hover:border-cyber-green/40 hover:bg-cyber-card'
        ]"
      >
        <img :src="os.img" :alt="os.label" class="h-8 w-8 object-contain transition-transform duration-300 group-hover:scale-110" />
        <span class="text-center leading-tight">{{ os.label }}</span>
        <span
          v-if="selectedOS === os.id"
          class="absolute -right-1 -top-1 h-3 w-3 rounded-full bg-cyber-green shadow-[0_0_8px_var(--color-cyber-green)]"
        />
      </button>
    </div>
  </section>
</template>
