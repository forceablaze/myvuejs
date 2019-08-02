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
import { delay } from '@/utils'

export default {
  data() {
    return {
      profiles: [],
      count: 0,
      loading: true,

      logProfileObjs: null,
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
        })
    },

    async refreshLogProfile() {
      try {
        const response = await this.axios.get('/file/')

        this.logProfileObjs = null
        delete this.logProfileObjs

        // Automatic transforms to JSON data
        this.logProfileObjs = response.data

      } catch(error) {
        this.$store.dispatch('SHOW_POPUP_MESSAGE', {
         'title': error
        })
        console.log(error)
      }
    },

    refresh() {
      delay(3000)('retry').then( async () => {


        await this.refreshLogProfile()

        let taskInfos = undefined
        try {
          const response = await this.axios.get('/pecker/')
          taskInfos = response.data

        } catch(error) {
          this.$store.dispatch('SHOW_POPUP_MESSAGE', {
           'title': error
          })
          console.log(error)
        }

        let obj = {}
        taskInfos.forEach( (task) => {
          obj[task.task_id] = task
        })

        for(let key in obj) {

          let found = false

          if(obj[key].search)
            continue

          /* check current profile is include all of the task */
          this.profiles.forEach((profile) => {
            if(profile.id == key) {
              found = true
              return
            }
          })

          const task = obj[key]

          if(!found) {
            console.log('push new task')

            let logProfile = this.findLogProfile(task.log_id)
            let { type, color } = this.checkTaskIconType(task.status)

            this.profiles.unshift({
              id: task.task_id,
              logId: task.log_id,
              title: logProfile.file,
              file_size: logProfile.file_size,
              timestamp: logProfile.timestamp,
              iconType: type,
              iconColor: color
            })
          }
        }

        this.profiles.forEach( (profile) => {
          profile.iconType = this.checkTaskIconType(
            obj[profile.id].status).type
        });

        this.refresh()
      })
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

          // ignore searching task
          if(task.search)
            return

          let logProfile = this.findLogProfile(task.log_id)
          let { type, color } = this.checkTaskIconType(task.status)

          this.profiles.push({
            id: task.task_id,
            logId: task.log_id,
            title: logProfile.file,
            file_size: logProfile.file_size,
            timestamp: logProfile.timestamp,
            iconType: type,
            iconColor: color
          })
        })
      } catch(error) {
        this.$store.dispatch('SHOW_POPUP_MESSAGE', {
         'title': error
        })
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

    this.$nextTick( async () => {
      await this.refreshLogProfile()
      await this.fetchTaskList()
      this.refresh()
    })
  },

  beforeDestroy: function () {
    this.profiles = null
    this.logProfileObjs = null
    this.peckerTaskObjs = null
  },

  components: {
    LogProfile
  }
}

</script>
