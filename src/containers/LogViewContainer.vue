<template>
  <v-container>
    <v-layout column>
      <v-flex>
        <v-layout row>
          <v-flex d-flex xs1>
            <span>Index</span>
          </v-flex>
          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 100px;"> 
            <span>time</span>
          </v-flex>
          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 200px"> 
            <span>apitype</span>
          </v-flex>


          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 100px"> 
            <span>flag</span>
          </v-flex>

          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 100px"> 
            <span>direction</span>
          </v-flex>

          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 100px"> 
            <span>logid</span>
          </v-flex>

          <v-divider vertical></v-divider>

          <v-flex d-flex xs12> 
            <span>data</span>
          </v-flex>
        </v-layout>
      </v-flex>

        <v-expansion-panel v-model="panel" expand>
          <log-component
            v-for="(log, index) in logs"
            :key="index"
            :log="log">
          </log-component>
        </v-expansion-panel>
    </v-layout>
  </v-container>
</template>

<style>
.container {
  max-width: 100%;
  padding:0px;
}
</style>

<script>

import LogComponent from '@/components/LogComponent'

export default {
  data() {
    return {
      logs: [],
      panel: [],
      count: 0,
      log_obj: {},
      log: {},
      showAll: false,
      currentPageIndex: 0
    }
  },

  props: ['task_id'],

  watch: {
    '$route' (to, from) {
      console.log(to)
      console.log(from)
    }
  },
  methods: {
    showAllLog() {
      this.panel = [...this.logs.keys()].map(_ => true)
    },
    // Reset the panel
    hideAllLog() {
      this.panel = []
    },

    fetchForwardLog() {
      console.log('fetch forward')
      this.currentPageIndex += 1
      this.fetchLog()
    },

    fetchBackLog() {
      console.log('back forward')
      this.currentPageIndex -= 1
      this.fetchLog()
    },

    fetchLog() {
      let from = this.currentPageIndex * 50

      console.log('fetch log ' + from)

      this.axios.post('/pecker/cvlog', {
        task_id: this.task_id,
        from: from,
      })
      .then(response => {
        // Automatic transforms for JSON data
        this.log_obj = response.data
        this.logs = this.log_obj.logs
        this.updateToolBar()
      })
      .catch(error => {
        console.log(error)
      });
    },
  
    updateToolBar() {
      let text = ''
      if(!this.showAll) {
        text = 'show all'
      }
      else {
        text = 'hide'
      }

      this.$store.dispatch('UPDATE_TOOLBAR_MENU', {
        'title': this.log_obj.product + '/' + this.log_obj.serial_number,
        'menuComponents': [
          { 'type': 'flat', 'text': text, 'handler': this.showHideLog },
          { 'type': 'icon', 'iconType': 'arrow_back_ios', 'handler': this.fetchBackLog },
          { 'type': 'icon', 'iconType': 'arrow_forward_ios', 'handler': this.fetchForwardLog },
        ]})
    },

    showHideLog(e) {
      this.showAll = !this.showAll

      if(this.showAll) {
        this.showAllLog()
      }
      else {
        this.hideAllLog()
      }
      this.updateToolBar()
    }
  },

  mounted() {
    console.log('fetch cvlog')
    this.fetchLog()
  },

  components: {
    LogComponent
  }
}

</script>
