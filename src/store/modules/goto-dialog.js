import { SHOW_GOTO_DIALOG, HIDE_GOTO_DIALOG } from './mutation-types'

export default {
  state: {
    show: false,
  },

  mutations: {
    [SHOW_GOTO_DIALOG] (state) {
      state.show = true
    },

    [HIDE_GOTO_DIALOG] (state) {
      state.show = false
    }
  },
  actions: {
    [SHOW_GOTO_DIALOG] ({ commit, state }, data) {
      commit(SHOW_GOTO_DIALOG, data)
    },

    [HIDE_GOTO_DIALOG] ({ commit, state }) {
      commit(HIDE_GOTO_DIALOG)
    }

  }
}
