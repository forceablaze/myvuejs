import { UPDATE_TOOLBAR_MENU, UPDATE_TOOLBAR_COMPONENT,UPDATE_EXPORT_PROGRESS } from './mutation-types'


export default {
  state: {
    title: '',
    menuComponents: [],
    count: 0,
    processing: false,
    ratio: 0
  },

  mutations: {
    [UPDATE_TOOLBAR_MENU] (state, { title, menuComponents }) {
      state.title = title
      state.menuComponents = menuComponents
    },

    [UPDATE_TOOLBAR_COMPONENT] (state, { index, component }) {
      state.menuComponents[index] = component
      console.log(component)
    },

    [UPDATE_EXPORT_PROGRESS] (state, { processing ,ratio }) {
      state.processing = processing
      state.ratio = ratio
      
      if(state.ratio == 100){
        setTimeout(() => {
          state.processing = false;
        }, 1000);
      }
      console.log('exporting status:' + processing)
    }
  },
  actions: {
    [UPDATE_TOOLBAR_MENU] ({ commit, state }, toolBarData) {
      commit(UPDATE_TOOLBAR_MENU, toolBarData)
    },

    [UPDATE_TOOLBAR_COMPONENT] ({ commit, state }, componentData) {
      commit(UPDATE_TOOLBAR_COMPONENT, componentData)
    },
    
    [UPDATE_EXPORT_PROGRESS] ({ commit, state }, processingData) {
      commit(UPDATE_EXPORT_PROGRESS, processingData)
    }
  }
}
