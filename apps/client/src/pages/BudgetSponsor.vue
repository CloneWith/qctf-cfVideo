<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const info = ref<{ in: number; out: number }>({in: 0, out: 0});
const username = ref("");
const amount = ref("");
const msg = ref("");

onMounted(async () => {
  const res = await fetch("/api/budget/info");
  info.value = await res.json();
});

async function sponsor() {
  msg.value = "";
  try {
    const res = await fetch("/api/sponsorship", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({username: username.value, amount: amount.value}),
    });
    if (!res.ok) throw new Error(await res.text());
    msg.value = "赞助成功！";
    username.value = "";
    amount.value = "";
  } catch (e: any) {
    msg.value = e.message || String(e);
  }
}
</script>

<template>
  <main>
    <h1>本月开销</h1>
    <h3>收入：{{ info.in }} 元</h3>
    <h3>支出：{{ info.out }} 元</h3>
    <div>来赞助吧·获得<b>澄峰主理人</b>会员专属头衔！</div>
    <form @submit.prevent="sponsor">
      <label>赞助用户名 <input v-model="username" required/></label>
      <label>赞助金额 <input v-model="amount" type="number" required/></label>
      <button type="submit">赞助</button>
      <span v-if="msg">{{ msg }}</span>
    </form>
    <button @click="router.push('/')">返回</button>
  </main>
</template>
