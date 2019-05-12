import {
  SHOW_BOTTOM_CONTAINER,
  HIDE_BOTTOM_CONTAINER,
  TRIGGER_BOTTOM_CONTAINER,
} from './mutation-types'

export default {
  state: {
    show: false,
  },

  mutations: {
    [SHOW_BOTTOM_CONTAINER] (state) {
      state.show = true
    },

    [HIDE_BOTTOM_CONTAINER] (state) {
      state.show = false
    },

    [TRIGGER_BOTTOM_CONTAINER] (state) {
      state.show = !state.show
    }
  },
  actions: {
    [SHOW_BOTTOM_CONTAINER] ({ commit, state }) {
      commit(SHOW_BOTTOM_CONTAINER)
    },

    [HIDE_BOTTOM_CONTAINER] ({ commit, state }) {
      commit(HIDE_BOTTOM_CONTAINER)
    },

    [TRIGGER_BOTTOM_CONTAINER] ({ commit, state }) {
      commit(TRIGGER_BOTTOM_CONTAINER)
    }
  }
}
