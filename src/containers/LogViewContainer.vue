<template>
  <v-container>
    <search-dialog ref="search_dialog"
      @search="searchLog"
    >
    </search-dialog>

    <goto-log-dialog ref="goto_log_dialog"
      @goto="gotoLog"
    >
    </goto-log-dialog>

    <v-container
      class="scroll-y"
    >
      <logdata-table
        :logs="logs"
        :rowsPerPage="perPageCount"
      />
    </v-container>
  </v-container>
</template>

<style>
.container {
  max-width: 100%;
  padding:0px;
}

table.v-table tbody td, table.v-table tbody th {
  height: auto;
}
</style>

<script>

import LogComponent from '@/components/LogComponent'
import SearchDialog from '@/components/SearchDialog'
import GotoLogDialog from '@/components/GotoLogDialog'

import LogDataTable from '@/components/LogDataTable'

import { delay } from '@/utils'

export default {
  data() {
    return {
      highlight: [],
      perPageCount: 2000,
      showAll: false,
      headers: [
        { text: 'index', value: 'index'},
        { text: 'time', value: 'time' },
        { text: 'apitype', value: 'apitype' },
        { text: 'flag', value: 'flag' },
        { text: 'direction', value: 'direction' },
        { text: 'logid', value: 'logid' },
        { text: 'data', value: 'data' },
      ],
    }
  },

  props: ['task_id', 'page'],

  computed: {
    'pageInfo' () {
      console.log(this.log_obj.total_pages)
      return 'page: ' + this.page + '/' + this.log_obj.total_pages
    },
    log_obj () {
      return this.$store.state.cvlog.log_obj
    },
    logs () {
      return this.$store.state.cvlog.log_obj.logs
    },
  },

  watch: {
    '$route' (to, from) {
      console.log(to.query)
      this.fetchLog((this.page - 1) * this.perPageCount)
    },
    'window.scrollY' (to) {
      console.log('scroll height changed:' + to)
    }
  },
  methods: {
    handleResize() {
      console.log('size changed')
      window.scrollTo(0, document.body.scrollHeight)
    },

    search() {
      console.log('open')
      this.$refs.search_dialog.open()
    },

    gotoLog(index) {
      this.fetchLog(Number(index), () => {

        this.highlight = [...this.logs.values()].map((log, idx) => {
          return log.index == Number(index)
        })
      })
    },

    showPopupMessageBox(message) {
      this.$store.dispatch('SHOW_POPUP_MESSAGE', {
        'title': message
      })
    },

    hideProgressBar() {
      this.$store.dispatch('HIDE_PROCESS_PROGRESS')
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

            this.retrieveFilteredLog(task_id)
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

    retrieveFilteredLog(task_id) {
      this.$store.dispatch('SHOW_PROCESS_PROGRESS', {
        'title': 'Loading...'
      })

      this.axios.post('/pecker/cvlog/' + task_id + '/search', { 'retrieve' : true })
      .then(response => {


        this.$store.dispatch('UPDATE_CVLOG_SEARCH_TASK_ID', {
          'search_task_id': task_id
        })

        this.$store.dispatch('UPDATE_CVLOG_SEARCH_OBJECT', {
          'search_log_obj': response.data
        })

        this.$store.dispatch('HIDE_PROCESS_PROGRESS')
        this.$store.dispatch('SHOW_BOTTOM_CONTAINER')

      })
      .catch(error => {
      })
    },

    searchLog(data) {
      console.log('search log')
      console.log(data)

      this.$store.dispatch('SHOW_PROCESS_PROGRESS', {
        'title': 'Searching...'
      })

      this.axios.post('/pecker/cvlog/' + this.task_id + '/search', data)
      .then(response => {
        this.retrieveTaskStatus(response.data.task_id)
      })
      .catch(error => {

        this.$store.dispatch('HIDE_PROCESS_PROGRESS')
        this.$store.dispatch('SHOW_POPUP_MESSAGE', {
         'title': error
        })

        console.log(error)
      });
    },

    onGotoClick() {
      this.$refs.goto_log_dialog.open()
    },

    fetchForwardLog() {
      console.log('fetch forward')

      let nextPage = parseInt(this.page) + 1
      if(nextPage > this.log_obj.total_pages)
        return

      this.$router.push({ name: 'log_view',
        params: {
          task_id: this.task_id,
          page: nextPage
        }})
    },

    fetchBackLog() {
      console.log('back forward')

      let prevPage = parseInt(this.page) - 1
      if(prevPage <= 0)
        return

      this.$router.push({ name: 'log_view',
        params: {
          task_id: this.task_id,
          page: parseInt(this.page) - 1
        }})
    },

    fetchLog(from, doneHandler = () => {} ) {
      console.log(typeof from)

      console.log('fetch log ' + from)
      this.$store.dispatch('SHOW_PROCESS_PROGRESS', {
        'title': 'Loading...'
      })

      this.axios.post('/pecker/cvlog', {
        task_id: this.task_id,
        from: from,
        count: this.perPageCount,
      })
      .then(response => {

        this.$store.dispatch('UPDATE_CVLOG_OBJECT', {
         'log_obj': response.data
        })

        doneHandler()
        this.updateToolBar(this.pageInfo, (idx) => {
          console.log(idx)

          this.$router.push({ name: 'log_view',
            params: {
              task_id: this.task_id,
              page: idx
          }})
        })

        this.$store.dispatch('HIDE_PROCESS_PROGRESS')
      })
      .catch(error => {

        this.$store.dispatch('HIDE_PROCESS_PROGRESS')
        this.$store.dispatch('SHOW_POPUP_MESSAGE', {
         'title': error
        })

        console.log(error)
      });
    },
  
    updateToolBar(info, handler) {
      let items = [...Array(this.log_obj.total_pages).keys()].map((idx) => {
        return {'title': String(idx + 1) }
      })

      this.$store.dispatch('UPDATE_TOOLBAR_MENU', {
        'title': this.log_obj.product + '/' + this.log_obj.serial_number,
        'menuComponents': [
          { 'compType': 'itemlistbutton', 'title': info,
            'items': items,
            'handler': handler
          },
          { 'type': 'flat', 'text': 'GOTO', 'handler': this.onGotoClick },
          { 'type': 'icon', 'iconType': 'search', 'handler': this.search },
          { 'type': 'icon', 'iconType': 'arrow_back_ios', 'handler': this.fetchBackLog },
          { 'type': 'icon', 'iconType': 'arrow_forward_ios', 'handler': this.fetchForwardLog },
        ]})
    },

  },

  ready: function () {
  },

  beforeDestroy: function () {
  },

  mounted() {
    console.log('fetch cvlog')
    this.fetchLog((this.page - 1) * this.perPageCount)
  },

  components: {
    LogComponent,
    SearchDialog,
    GotoLogDialog,
    'logdata-table': LogDataTable,
  }
}

</script>
