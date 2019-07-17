// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import axios from 'axios'
import VueAxios from 'vue-axios'
import { axiosConfig } from '@/config'

import 'vue-virtual-scroller/dist/vue-virtual-scroller.css'
import VueVirtualScroller from 'vue-virtual-scroller'


import App from './App'
import { createStore } from '@/store/index'
import { createRouter } from './router'

Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(VueAxios, axios.create(axiosConfig))
Vue.use(VueVirtualScroller)


const router = createRouter()
const store = createStore()

Vue.prototype.$eventHub = new Vue();

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
