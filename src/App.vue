<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      fixed
      app
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
        <v-list-tile @click="navigatePage('log')">
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
      <v-toolbar-title>Application</v-toolbar-title>
    </v-toolbar>
    <v-content>
			<uploadfile-dialog ref="upload_dialog"
        @uploading="onUploading"
        @success="onUploadSuccess"
        @failed="onUploadFailed"></uploadfile-dialog>
      <process-progress ref="processProgress" :status=progressStatus></process-progress>
      <router-view></router-view>
    </v-content>
    <v-footer color="indigo" app>
      <span class="white--text">&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>

import UploadFileDialog from '@/components/UploadFileDialog'
import ProcessProgress from '@/components/ProcessProgress'

export default {

  data: () => ({
    drawer: null,
    progressStatus: ''
  }),
  components: {
    'uploadfile-dialog': UploadFileDialog,
    'process-progress': ProcessProgress,
  },
  props: {
    source: String,
  },
  methods: {
    upload_log() {
      this.$refs.upload_dialog.open()
    },
    onUploadSuccess(e) {
      this.refs.processProgress.hide()
    },
    onUploadFailed(e) {
      console.log(e)
    },
    onUploading(e) {
      this.showProgressBar('Uploading')
    },
    showProgressBar(status) {
      this.progressStatus = status
      this.$refs.processProgress.show()
    },
    navigatePage(pageName) {
      this.$router.push({ name: pageName })
    }
  },
}
</script>
