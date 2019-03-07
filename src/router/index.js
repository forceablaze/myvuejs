import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Hello from '@/components/Hello'
import Home from '@/components/Home'
import LogViewContainer from '@/containers/LogViewContainer'
import LogComponent from '@/components/LogComponent'

let About = {
  template: '<h2>About</h2>'
}

let createRouter = () => {
  const routes = [
    { path: '/', name: 'hello', component: Hello },
    { path: '/home', name: 'home', component: Home },
    { path: '/log', name: 'log', component: LogViewContainer },
    { path: '/test', name: 'test', component: LogComponent },
    { path: '/about', name: 'about', component: About },
  ]

  const router = new Router({
    routes
  })

  return router
}


export { createRouter };
