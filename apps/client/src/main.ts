import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import VideoList from './pages/VideoList.vue'
import OrderForm from './pages/OrderForm.vue'
import BudgetSponsor from './pages/BudgetSponsor.vue'
import AdminLogin from './pages/AdminLogin.vue'
import AdminPanel from './pages/AdminPanel.vue'

const routes = [
	{ path: '/', component: VideoList },
	{ path: '/order', component: OrderForm },
	{ path: '/budget', component: BudgetSponsor },
	{ path: '/admin-login', component: AdminLogin },
	{ path: '/admin', component: AdminPanel }
]
const router = createRouter({ history: createWebHistory(), routes })

const app = createApp(App)
app.use(router)
app.mount('#app')
