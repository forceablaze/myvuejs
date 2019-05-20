import {
  SHOW_SEARCH_CONTAINER,
  HIDE_SEARCH_CONTAINER,
  TRIGGER_SEARCH_CONTAINER,
} from './mutation-types'

export default {
  state: {
    show: false,
  },

  mutations: {
    [SHOW_SEARCH_CONTAINER] (state) {
      state.show = true
    },

    [HIDE_SEARCH_CONTAINER] (state) {
      state.show = false
    },

    [TRIGGER_SEARCH_CONTAINER] (state) {
      state.show = !state.show
    }
  },
  actions: {
    [SHOW_SEARCH_CONTAINER] ({ commit, state }) {
      commit(SHOW_SEARCH_CONTAINER)
    },

    [HIDE_SEARCH_CONTAINER] ({ commit, state }) {
      commit(HIDE_SEARCH_CONTAINER)
    },

    [TRIGGER_SEARCH_CONTAINER] ({ commit, state }) {
      commit(TRIGGER_SEARCH_CONTAINER)
    }
  }
}
