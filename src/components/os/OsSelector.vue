<script setup>
import { osOptions, selectedOS } from '../../store.js'
</script>

<template>
  <section class="mb-10">
    <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-ui-text-muted">
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
            ? 'border-ui-primary bg-ui-primary/10 text-ui-primary shadow-sm'
            : 'border-ui-border bg-ui-surface text-ui-text-muted hover:border-ui-primary/40 hover:bg-ui-card'
        ]"
      >
        <img :src="os.img" :alt="os.label" class="h-8 w-8 object-contain transition-transform duration-300 group-hover:scale-110" />
        <span class="text-center leading-tight">{{ os.label }}</span>
        <span
          v-if="selectedOS === os.id"
          class="absolute -right-1 -top-1 h-3 w-3 rounded-full bg-ui-primary shadow-sm"
        />
      </button>
    </div>
  </section>
</template>
