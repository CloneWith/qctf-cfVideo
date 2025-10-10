<script setup lang="ts">
import { ref, onMounted } from 'vue'

const message = ref<string>('Hello from Vue + Vite + TS')
const apiMessage = ref<string>('(loading...)')

onMounted(async () => {
  try {
    const res = await fetch('/api/health')
    const data = await res.json()
    apiMessage.value = data.status ?? JSON.stringify(data)
  } catch (e) {
    apiMessage.value = 'API not available'
  }
})
</script>

<template>
  <main style="font-family: ui-sans-serif, system-ui, -apple-system; padding: 2rem">
    <h1>{{ message }}</h1>
    <p>Backend health: {{ apiMessage }}</p>
  </main>
</template>

<style scoped>
h1 {
  color: #42b883;
}
</style>
