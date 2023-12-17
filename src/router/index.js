import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
      children:[
        {
          path: "/about/user",
          name: "user",
          component: () => import('../views/user.vue')
        },
        {
          path: "/about/subscribe",
          name: "subscribe",
          component: () => import('../views/subscribe.vue')
        },
        {
          path: "/about/publish",
          name: "publish",
          component: () => import('../views/publish.vue')
        },
        {
          path: "/about/help",
          name: "help",
          component: () => import('../views/help.vue')
        },
        {
          path: "/about/details",
          name: "details",
          component: () => import('../views/details.vue')
        },
      ]
    }
  ]
})

export default router
