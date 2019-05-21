import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Hello from '@/components/Hello'
import Home from '@/components/Home'

import LogListContainer from '@/containers/LogListContainer'
import LogList from '@/components/LogList'

import LogViewContainer from '@/containers/LogViewContainer'
import LogComponent from '@/components/LogComponent'

import Http404 from '@/components/errors/Http404'
import Http406 from '@/components/errors/Http406'

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
    { path: '/about', name: 'about', component: About },
    { path: '/404', component: Http404 },
    { path: '/406', component: Http406 },
    { path: '*', redirect: '/404' },
  ]

  const router = new Router({
    routes
  })

  return router
}


export { createRouter };
