<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const videos = ref<{ id: number; theme: string; content: string; username: string }[]>([])
const router = useRouter()

onMounted(async () => {
  // 获取最近订单（祝福视频）
  const res = await fetch('/api/requests')
  const data = await res.json()
  videos.value = data.slice(-5).reverse()
})
</script>

<template>
  <main>
    <h1>澄峰祝福视频列表</h1>
    <ul>
      <li v-for="v in videos" :key="v.id">
        <strong>{{ v.theme }}</strong> - {{ v.content }}<br />
        <span>by {{ v.username }}</span>
      </li>
    </ul>
    <button @click="router.push('/order')">请求制作新视频</button>
    <button @click="router.push('/budget')">查看本月开销与赞助</button>
  </main>
</template>
