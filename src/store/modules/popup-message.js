import { SHOW_POPUP_MESSAGE, HIDE_POPUP_MESSAGE } from './mutation-types'

export default {
  state: {
    title: '',
    show: false,
  },

  mutations: {
    [SHOW_POPUP_MESSAGE] (state, { title }) {
      state.title = title
      state.show = true
    },

    [HIDE_POPUP_MESSAGE] (state) {
      state.title = ''
      state.show = false
    }
  },
  actions: {
    [SHOW_POPUP_MESSAGE] ({ commit, state }, data) {
      commit(SHOW_POPUP_MESSAGE, data)
    },

    [HIDE_POPUP_MESSAGE] ({ commit, state }) {
      commit(HIDE_POPUP_MESSAGE)
    }

  }
}
