import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Hello from '@/components/Hello'

let createRouter = () => {
  const routes = [
    { path: '/hello', components: Hello },
  ]

  const router = new Router({
    routes
  })

  return router
}


export { createRouter };
