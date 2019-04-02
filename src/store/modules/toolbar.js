import { UPDATE_TOOLBAR_MENU, UPDATE_TOOLBAR_COMPONENT } from './mutation-types'


export default {
  state: {
    title: '',
    menuComponents: [],
    count: 0
  },

  mutations: {
    [UPDATE_TOOLBAR_MENU] (state, { title, menuComponents }) {
      state.title = title
      state.menuComponents = menuComponents
    },

    [UPDATE_TOOLBAR_COMPONENT] (state, { index, component }) {
      state.menuComponents[index] = component
      console.log(component)
    }
  },
  actions: {
    [UPDATE_TOOLBAR_MENU] ({ commit, state }, toolBarData) {
      commit(UPDATE_TOOLBAR_MENU, toolBarData)
    },

    [UPDATE_TOOLBAR_COMPONENT] ({ commit, state }, componentData) {
      commit(UPDATE_TOOLBAR_COMPONENT, componentData)
    }

  }
}
