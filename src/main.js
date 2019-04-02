// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import App from './App'
import { createStore } from '@/store/index'
import { createRouter } from './router'

Vue.config.productionTip = false

Vue.use(Vuetify)

const router = createRouter()
const store = createStore()

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store: store,
  router: router,
  components: { App },
  template: '<App/>',

  created: () => {
    console.log('created')
  }
})
