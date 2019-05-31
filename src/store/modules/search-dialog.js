import { SHOW_SEARCH_DIALOG, HIDE_SEARCH_DIALOG } from './mutation-types'

export default {
  state: {
    show: false,
  },

  mutations: {
    [SHOW_SEARCH_DIALOG] (state) {
      state.show = true
    },

    [HIDE_SEARCH_DIALOG] (state) {
      state.show = false
    }
  },
  actions: {
    [SHOW_SEARCH_DIALOG] ({ commit, state }, data) {
      commit(SHOW_SEARCH_DIALOG, data)
    },

    [HIDE_SEARCH_DIALOG] ({ commit, state }) {
      commit(HIDE_SEARCH_DIALOG)
    }

  }
}
