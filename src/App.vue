<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer" fixed app
      width="200"
    >
      <v-list dense>
        <v-list-tile @click="navigatePage('home')">
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile @click="upload_log()">
          <v-list-tile-action>
            <v-icon>cloud_upload</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Upload Log</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile @click="toShowLogPage()">
          <v-list-tile-action>
            <v-icon>list</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Show Log</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="indigo" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>{{ toolBarTitle }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <toolbar-component
        v-for="(menu, index) in toolBarMenu"
        :key="index"
        :index="index"
        :handler="menu.handler">
      </toolbar-component>
    </v-toolbar>
    <v-content style="height:100%;">
			<uploadfile-dialog ref="upload_dialog"
        @uploading="onUploading"
        @success="onUploadSuccess"
        @failed="onUploadFailed"></uploadfile-dialog>
      <process-progress ref="processProgress"></process-progress>
      <popup-messagebox ref="popupMessageBox"
        :message=popupMessage
        :handler="onOkClick"
      ></popup-messagebox>
      <router-view></router-view>

      <transition name="fadeHeight">
        <searchresult-container v-if="showBottomContainer" :defaultHeight="300"/>
      </transition>

    </v-content>
    <v-footer color="indigo" app>
      <span class="white--text">インテグ</span>
      <v-spacer/>
      <v-btn flat icon @click.stop="filterButtonClick">
        <v-icon color="white">filter_list</v-icon>
      </v-btn>
    </v-footer>
  </v-app>
</template>

<style>

.container {
  max-width: 100%;
  padding: 0px;
}

.bottom-container {
  background-color: white;
}

.fadeHeight-enter-active,
.fadeHeight-leave-active {
  transition: all 0.2s;
}
.fadeHeight-enter,
.fadeHeight-leave-to
{
  opacity: 0;
  height: 0px
}
</style>

<script>

import PopupMessageBox from '@/components/PopupMessageBox'
import UploadFileDialog from '@/components/UploadFileDialog'
import ProcessProgress from '@/components/ProcessProgress'
import DynamicToolBarComponent from '@/components/DynamicToolBarComponent'

import SearchResultContainer from '@/containers/SearchResultContainer'

import { delay } from '@/utils'

import { mapState } from 'vuex'

export default {

  data: () => ({
    drawer: null,
    popupMessage: '',
    taskData: {},
  }),
  components: {
    'uploadfile-dialog': UploadFileDialog,
    'process-progress': ProcessProgress,
    'toolbar-component': DynamicToolBarComponent,
    'popup-messagebox': PopupMessageBox,
    'searchresult-container': SearchResultContainer,
  },
  props: {
    source: String,
  },

  computed: mapState({
    toolBarTitle: state => state.toolbar.title,

    toolBarMenu: state => state.toolbar.menuComponents,

    showBottomContainer: state => state.bottomcontainer.show,
  }),

  watch: {
    '$route.name' (to, from) {
      console.log(to)
      console.log(from)
    },
  },

  mounted() {

  },
 
  methods: {
    filterButtonClick() {
      this.$store.dispatch('TRIGGER_BOTTOM_CONTAINER')
    },

    upload_log() {
      this.$refs.upload_dialog.open()
    },

    updatePageButton() {
      let items = [...Array(this.searchResultTotalPage).keys()].map((idx) => {
        return {'title': String(idx + 1) }
      })
    },

    onOkClick() {
      console.log('click')
      if(this.taskData.status == 'success')
        this.$router.push({ name: 'log_view',
          params: {
            task_id: this.taskData.task_id,
            page: 1
          }})
    },

    retrieveTaskStatus(task_id) {
      delay(5000)('retry').then((result) => {
        console.log('retrieve task:' + task_id)

        this.axios.get('/pecker/' +  task_id)
        .then(response => {
          // Automatic transforms for JSON data
          console.log(response.data.status)
          this.taskData = response.data

          if(response.data.status == 'running') {
            this.retrieveTaskStatus(task_id)
          }
          else if(response.data.status == 'success') {
            this.hideProgressBar()

            this.showPopupMessageBox('Success')
          }
          else if(response.data.status == 'failed') {
            this.hideProgressBar()
            this.showPopupMessageBox('Failed')
          }
          else {
            console.log('retry')
            this.retrieveTaskStatus(task_id)
          }
        })
        .catch(error => {
          console.log(error)
        });
      });
    },

    onUploadSuccess(data) {
      console.log('upload success log_id:' + data.id)

      //this.$refs.processProgress.hide()

      this.hideProgressBar()

      /* trigger pecker task */
      this.axios.post('/pecker/', {
        log_id: data.id
      })
      .then(response => {
        console.log(response.data)
        this.retrieveTaskStatus(response.data.task_id)
      })
      .catch(error => {
        console.log(error)
      });

      this.showProgressBar('Analyzing')
    },

    onUploadFailed(e) {
      this.$refs.processProgress.hide()
    },

    onUploading(e) {
      this.showProgressBar('Uploading')
    },

    showPopupMessageBox(message) {
      this.$store.dispatch('SHOW_POPUP_MESSAGE', {
        'title': message
      })
    },

    showProgressBar(status) {
      this.$store.dispatch('SHOW_PROCESS_PROGRESS', {
        'title': status
      })
    },

    hideProgressBar() {
      this.$store.dispatch('HIDE_PROCESS_PROGRESS')
    },

    toShowLogPage() {
      this.navigatePage('log_list')
    },

    navigatePage(pageName) {
      this.$router.push({ name: pageName })
    }
  },
}
</script>
