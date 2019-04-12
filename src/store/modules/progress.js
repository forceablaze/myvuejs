import { SHOW_PROCESS_PROGRESS, HIDE_PROCESS_PROGRESS } from './mutation-types'

export default {
  state: {
    title: '',
    show: false,
  },

  mutations: {
    [SHOW_PROCESS_PROGRESS] (state, { title }) {
      state.title = title
      state.show = true
    },

    [HIDE_PROCESS_PROGRESS] (state) {
      state.title = ''
      state.show = false
    }
  },
  actions: {
    [SHOW_PROCESS_PROGRESS] ({ commit, state }, data) {
      commit(SHOW_PROCESS_PROGRESS, data)
    },

    [HIDE_PROCESS_PROGRESS] ({ commit, state }) {
      commit(HIDE_PROCESS_PROGRESS)
    }

  }
}
