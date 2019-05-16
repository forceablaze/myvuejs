import {
  UPDATE_CVLOG_OBJECT,
  UPDATE_CVLOG_SEARCH_OBJECT,
  UPDATE_CVLOG_SEARCH_TASK_ID,
} from './mutation-types'

export default {
  state: {
    log_obj: {},
    search_log_obj: {},
    search_task_id: undefined
  },

  mutations: {
    [UPDATE_CVLOG_OBJECT] (state, { log_obj }) {
      console.log('update log')
      state.log_obj = {}
      state.log_obj = log_obj
    },

    [UPDATE_CVLOG_SEARCH_OBJECT] (state, { search_log_obj }) {
      state.search_log_obj = {}
      state.search_log_obj = search_log_obj
    },

    [UPDATE_CVLOG_SEARCH_TASK_ID] (state, { search_task_id }) {
      state.search_task_id = search_task_id
    }
  },
  actions: {
    [UPDATE_CVLOG_OBJECT] ({ commit, state }, data) {
      commit(UPDATE_CVLOG_OBJECT, data)
    },

    [UPDATE_CVLOG_SEARCH_OBJECT] ({ commit, state }, data) {
      commit(UPDATE_CVLOG_SEARCH_OBJECT, data)
    },

    [UPDATE_CVLOG_SEARCH_TASK_ID] ({ commit, state }, data) {
      commit(UPDATE_CVLOG_SEARCH_TASK_ID, data)
    }
  }
}
