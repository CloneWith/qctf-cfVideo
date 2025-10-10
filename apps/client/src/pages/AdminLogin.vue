<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password = ref('')
const error = ref('')

async function login() {
  error.value = ''
  try {
    const res = await fetch('/api/admin/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: username.value, password: password.value })
    })
    if (!res.ok) throw new Error(await res.text())
    router.push('/admin')
  } catch (e: any) {
    error.value = e.message || String(e)
  }
}
</script>

<template>
  <main>
    <h1>管理员后台登录</h1>
    <form @submit.prevent="login">
      <label>用户名 <input v-model="username" required /></label><br />
      <label>密码 <input v-model="password" type="password" required /></label><br />
      <button type="submit">登录</button>
      <div v-if="error" style="color:red">{{ error }}</div>
    </form>
    <button @click="router.push('/')">返回</button>
  </main>
</template>
