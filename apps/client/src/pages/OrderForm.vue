<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref({
  username: '',
  email: '',
  theme: '',
  content: '',
  contact: '',
  fee: '',
  attachment: null as File | null
})
const submitting = ref(false)
const error = ref('')

async function submitOrder() {
  submitting.value = true
  error.value = ''
  const fd = new FormData()
  fd.append('username', form.value.username)
  fd.append('email', form.value.email)
  fd.append('theme', form.value.theme)
  fd.append('content', form.value.content)
  fd.append('contact', form.value.contact)
  fd.append('fee', form.value.fee)
  if (form.value.attachment) fd.append('attachment', form.value.attachment)
  try {
    const res = await fetch('/api/requests', {
      method: 'POST',
      body: fd
    })
    if (!res.ok) throw new Error(await res.text())
    router.push('/')
  } catch (e: any) {
    error.value = e.message || String(e)
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <main>
    <h1>请求制作祝福视频</h1>
    <form @submit.prevent="submitOrder">
      <label>用户名 <input v-model="form.username" required /></label><br />
      <label>邮箱 <input v-model="form.email" type="email" required /></label><br />
      <label>主题 <input v-model="form.theme" required /></label><br />
      <label>内容 <textarea v-model="form.content" required /></label><br />
      <label>联系方式 <input v-model="form.contact" required /></label><br />
      <label>费用 <input v-model="form.fee" type="number" required /></label><br />
      <label>附件 <input type="file" @change="e => form.attachment = e.target.files[0]" /></label><br />
      <button type="submit" :disabled="submitting">提交订单</button>
      <button type="button" @click="router.push('/')">返回</button>
      <div v-if="error" style="color:red">{{ error }}</div>
    </form>
  </main>
</template>
