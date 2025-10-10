<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const tab = ref('users')
const data = ref<any[]>([])
const sql = ref('SELECT * FROM requests')
const sqlResult = ref<any[]>([])
const sqlError = ref('')

async function fetchData() {
  let url = ''
  if (tab.value === 'users') url = '/api/users'
  if (tab.value === 'requests') url = '/api/requests'
  if (tab.value === 'budget') url = '/api/budget'
  if (tab.value === 'sponsorship') url = '/api/sponsorship'
  if (!url) return
  const res = await fetch(url)
  data.value = await res.json()
}

onMounted(fetchData)

function switchTab(t: string) {
  tab.value = t
  fetchData()
}

async function runSQL() {
  sqlError.value = ''
  try {
    const res = await fetch('/api/admin/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sql: sql.value })
    })
    if (!res.ok) throw new Error(await res.text())
    sqlResult.value = await res.json()
  } catch (e: any) {
    sqlError.value = e.message || String(e)
  }
}
</script>

<template>
  <main>
    <h1>管理员后台</h1>
    <nav>
      <button @click="switchTab('users')">用户</button>
      <button @click="switchTab('requests')">订单</button>
      <button @click="switchTab('budget')">收支</button>
      <button @click="switchTab('sponsorship')">赞助</button>
    </nav>
    <div v-if="tab === 'users'">
      <h2>用户</h2>
      <pre>{{ data }}</pre>
    </div>
    <div v-if="tab === 'requests'">
      <h2>订单</h2>
      <pre>{{ data }}</pre>
    </div>
    <div v-if="tab === 'budget'">
      <h2>收支</h2>
      <pre>{{ data }}</pre>
    </div>
    <div v-if="tab === 'sponsorship'">
      <h2>赞助</h2>
      <pre>{{ data }}</pre>
    </div>
    <section>
      <h2>SQL 注入/命令执行入口</h2>
      <form @submit.prevent="runSQL">
        <textarea v-model="sql" rows="3" style="width:100%"></textarea><br />
        <button type="submit">执行 SQL</button>
      </form>
      <div v-if="sqlError" style="color:red">{{ sqlError }}</div>
      <pre v-if="sqlResult.length">{{ sqlResult }}</pre>
    </section>
    <button @click="router.push('/')">返回</button>
  </main>
</template>
