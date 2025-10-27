<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const videos = ref<{ id: number; theme: string; content: string; username: string }[]>([]);
const router = useRouter();

onMounted(async () => {
  // 获取最近订单（祝福视频）
  const res = await fetch("/api/requests");
  const data = await res.json();
  videos.value = data.slice(-5).reverse();
});
</script>

<template>
  <main>
    <h1>欢迎来到</h1>
    <div>全网唯一指定·澄峰祝福视频制作平台</div>
    <h2>所有订单</h2>
    <ul>
      <li v-for="v in videos" :key="v.id">
        <strong>{{ v.theme }}</strong> - {{ v.content }}<br/>
        <span>by {{ v.username }}</span>
      </li>
    </ul>
    <button @click="router.push('/order')">新视频制作下单</button>
    <button @click="router.push('/budget')">赞助我！</button>
  </main>
</template>
