import { createRouter, createWebHistory } from 'vue-router'
import Reservas from './components/Reservas.vue'
import Admin from './components/Admin.vue'

const routes = [
  { path: '/', component: Reservas },
  { path: '/administradores', component: Admin }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router