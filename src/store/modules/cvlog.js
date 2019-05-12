import { UPDATE_CVLOG_OBJECT, UPDATE_CVLOG_SEARCH_OBJECT } from './mutation-types'

export default {
  state: {
    log_obj: {},
    search_logs: []
  },

  mutations: {
    [UPDATE_CVLOG_OBJECT] (state, { log_obj }) {
      console.log('update log')
      state.log_obj = {}
      state.log_obj = log_obj
    },

    [UPDATE_CVLOG_SEARCH_OBJECT] (state, { search_logs }) {
      state.search_logs = []
      state.search_logs = search_logs
    }
  },
  actions: {
    [UPDATE_CVLOG_OBJECT] ({ commit, state }, data) {
      commit(UPDATE_CVLOG_OBJECT, data)
    },

    [UPDATE_CVLOG_SEARCH_OBJECT] ({ commit, state }, data) {
      commit(UPDATE_CVLOG_SEARCH_OBJECT, data)
    }
  }
}
