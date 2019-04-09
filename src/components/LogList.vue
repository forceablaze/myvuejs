<template>
  <v-list two-line subheader>
    <log-profile v-for="(profile, index) in profiles"
      :profile="profile"
      :key="index"
      :iconColor="profile.iconColor"
      @click="onProfileClick"></log-profile>
  </v-list>
</template>

<script>

import LogProfile from '@/components/LogProfile'

export default {
  data() {
    return {
      profiles: [],
      count: 0,
      loading: true,

      logProfileObjs: {},
      peckerTaskObjs: {},
    }
  },

  methods: {
    onProfileClick(task_id) {
      console.log(task_id)
      this.$router.push({ name: 'log_view',
        params: {
          task_id: task_id,
          page: 1
        }})
    },

    refreshToolBar() {
      this.$store.dispatch('UPDATE_TOOLBAR_MENU', {
        'title': 'Uploaded Log',
        'menuComponents': [
          { 'type': 'icon', 'iconType': 'refresh', 'handler': this.refresh },
        ]})
    },

    refresh() {
      this.fetchTaskList()
    },

    checkTaskIconType(taskStatus) {
      if(taskStatus == 'running')
        return { 'type': 'loop', 'color': 'grey' }
      else if(taskStatus == 'success')
        return { 'type': 'done', 'color': 'green' }
      else if(taskStatus == 'failed')
        return { 'type': 'error', 'color': 'red' }
      return { 'type': 'error', 'color': 'red' }
    },

    findLogProfile(log_id) {
      return this.logProfileObjs.find((element) => {
        return element.id == log_id
      })
    },

    async fetchTaskList() {

      this.profiles = []

      try {
        const response = await this.axios.get('/file/')

        this.logProfileObjs = null
        delete this.logProfileObjs

      // Automatic transforms for JSON data
        this.logProfileObjs = response.data

      } catch(error) {
        console.log(error)
      }

      try {
        const response = await this.axios.get('/pecker/')

        this.peckerTaskObjs = null
        delete this.peckerTaskObjs

        this.peckerTaskObjs = response.data

        this.peckerTaskObjs.sort((x, y) => {
          let xDate = new Date(x.timestamp)
          let yDate = new Date(y.timestamp)
        
        // the first the newest
          return yDate - xDate
        })

        this.peckerTaskObjs.forEach((task) => {
          let logProfile = this.findLogProfile(task.log_id)
          let { type, color } = this.checkTaskIconType(task.status)

          this.profiles.push({
            id: task.task_id,
            title: logProfile.file,
            file_size: logProfile.file_size,
            timestamp: logProfile.timestamp,
            iconType: type,
            iconColor: color
          })
        })
      } catch(error) {
        console.log(error)
      }

    }
  },

  computed: {
  },

  watch: {
    '$route' (to, from) {
      console.log(to)
      console.log(from)
    }
  },

  mounted() {
    this.refreshToolBar()
    this.fetchTaskList()
  },

  components: {
    LogProfile
  }
}

</script>
