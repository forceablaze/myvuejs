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
    <v-content>
			<uploadfile-dialog ref="upload_dialog"
        @uploading="onUploading"
        @success="onUploadSuccess"
        @failed="onUploadFailed"></uploadfile-dialog>
      <process-progress ref="processProgress" :status=progressStatus></process-progress>
      <popup-messagebox ref="popupMessageBox" :message=popupMessage></popup-messagebox>
      <router-view></router-view>
    </v-content>
    <v-footer color="indigo" app>
      <span class="white--text">インテグ</span>
    </v-footer>
  </v-app>
</template>

<script>

import PopupMessageBox from '@/components/PopupMessageBox'
import UploadFileDialog from '@/components/UploadFileDialog'
import ProcessProgress from '@/components/ProcessProgress'
import DynamicToolBarComponent from '@/components/DynamicToolBarComponent'

import { delay } from '@/utils'

import { mapState } from 'vuex'

export default {

  data: () => ({
    drawer: null,
    progressStatus: '',
    popupMessage: '',
    count: { objs: [ { title: '123' }] }
  }),
  components: {
    'uploadfile-dialog': UploadFileDialog,
    'process-progress': ProcessProgress,
    'toolbar-component': DynamicToolBarComponent,
    'popup-messagebox': PopupMessageBox
  },
  props: {
    source: String,
  },

  computed: mapState({
    toolBarTitle: state => state.toolbar.title,

    toolBarMenu: state => state.toolbar.menuComponents
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
    upload_log() {
      this.$refs.upload_dialog.open()
    },

    retrieveTaskStatus(task_id) {
      delay(5000)('retry').then((result) => {
        console.log('retrieve task:' + task_id)

        this.axios.get('/pecker/' +  task_id)
        .then(response => {
          // Automatic transforms for JSON data
          console.log(response.data.status)
          if(response.data.status == 'running') {
            this.retrieveTaskStatus(task_id)
          }
          else if(response.data.status == 'success') {
            this.$refs.processProgress.hide()
            this.showPopupMessageBox('Success')
          }
          else if(response.data.status == 'failed') {
            this.$refs.processProgress.hide()
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

      this.$refs.processProgress.hide()

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
      this.popupMessage = message
      this.$refs.popupMessageBox.show()
    },

    showProgressBar(status) {
      this.progressStatus = status
      this.$refs.processProgress.show()
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
