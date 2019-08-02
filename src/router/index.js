import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Hello from '@/components/Hello'
import Home from '@/components/Home'

import LogListContainer from '@/containers/LogListContainer'
import LogList from '@/components/LogList'

import LogViewContainer from '@/containers/LogViewContainer'
import LogComponent from '@/components/LogComponent'

import VirtualScroller from '@/components/VirtualScroller'

let About = {
  template: '<h2>About</h2>'
}

let createRouter = () => {
  const routes = [
    { path: '/', name: 'hello', component: Home },
    { path: '/home', name: 'home', component: Home },
    { path: '/log', component: LogListContainer,
      children: [
        {
          path: '',
          name: 'log_list',
          component: LogList
        },
        {
          path: ':task_id/:page',
          name: 'log_view',
          props: true,
          component: LogViewContainer
        },
      ]
    },
  ]

  const router = new Router({
    routes
  })

  return router
}


export { createRouter };
