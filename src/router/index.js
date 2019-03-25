import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'

let axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api',
	timeout: 60000,
})

Vue.use(Router)
Vue.use(VueAxios, axiosInstance)

import Hello from '@/components/Hello'
import Home from '@/components/Home'
import LogViewContainer from '@/containers/LogViewContainer'
import LogListContainer from '@/containers/LogListContainer'
import LogComponent from '@/components/LogComponent'

let About = {
  template: '<h2>About</h2>'
}

let createRouter = () => {
  const routes = [
    { path: '/', name: 'hello', component: Home },
    { path: '/home', name: 'home', component: Home },
    { path: '/log', name: 'log', component: LogListContainer },
    { path: '/test', name: 'test', component: LogViewContainer },
    { path: '/about', name: 'about', component: About },
  ]

  const router = new Router({
    routes
  })

  return router
}


export { createRouter };
