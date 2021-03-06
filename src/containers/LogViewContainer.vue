<template>
  <v-container>

    <goto-log-dialog @goto="gotoLog"/>

    <multitoolbar @search="searchLog"/>

    <searchresult-container
      v-if="showSearchContainer"
      :defaultWidth="300"
      />

    <logdata-table
      :style="tableStyleObject"
      :headers="tableHeaders"
      :logs="logs"
      :rowsPerPage="perPageCount"
      :highlight="highlight"
      :focus="focus"
      @click="logItemClick"
    />

    <bottomview
      :defaultHeight="200"
      :style="bottomViewStyle"
      ref="bottomView"
    >
      <log-component
        v-if="current_log"
        :log="current_log"
      />
    </bottomview>

  </v-container>
</template>

<style scoped>

.container {
  max-width: 100%;
  padding:0px;
}

</style>

<script>

import LogComponent from '@/components/LogComponent'
import SearchDialog from '@/components/SearchDialog'
import GotoLogDialog from '@/components/GotoLogDialog'
import LogDataTable from '@/components/LogDataTable'

import MultiFunctionToolBar from '@/components/MultiFunctionToolBar'
import SearchResultContainer from '@/containers/SearchResultContainer'
import BottomViewContainer from '@/containers/BottomViewContainer'

import { delay } from '@/utils'

/* override the computed priorities data table height and width */
import DataTable from '@/components/DataTable'
const MainDataTable = {
  extends: DataTable,

  computed: {
    dataTableHeight() {
      return this.$wood.logViewContainer.windowHeight -
        this.$wood.logViewContainer.bottomViewHeight -
        128
    },
    dataTableWidth() {
      return this.$wood.logViewContainer.windowWidth -
        this.$wood.logViewContainer.rightViewWidth
    }
  }
}

const MainLogDataTable = {
  extends:  LogDataTable,

  components: {
    'datatable': MainDataTable,
  }
}

export default {

  data() {
    return {
      highlight: [],
      highLightIndex:-1,
      focus: undefined,
      perPageCount: 500,
      tableHeaders: [
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
    log_obj () {
      return this.$store.state.cvlog.log_obj
    },
    logs () {
      return this.$store.state.cvlog.log_obj.logs
    },

    computedTablePaddingRight() {
      return this.$vuetify.application.left
    },

    bottomViewStyle() {
      return {
        transition: "padding .2s cubic-bezier(.4,0,.2,1)",
        position: "absolute"
      }
    },

    tableStyleObject() {
      return {
        top: "128px",
        position: "fixed",
        width: "100%",
        paddingRight: `${this.computedTablePaddingRight}px`,

        transition: "padding .2s cubic-bezier(.4,0,.2,1)"
      }
    },

    showLogInfo() {

      if(this.logs === undefined ||
        this.$store.state.cvlog.current_logid === undefined)
        return false
      return true
    },

    current_log() {
      if(!this.showLogInfo)
        return false

      return this.logs[this.$store.state.cvlog.current_logid]
    },

    showSearchContainer() {
      return this.$store.state.searchcontainer.show
    },
  },

  watch: {
    '$route' (to, from) {
      console.log(to.query)
      this.fetchLog((this.page - 1) * this.perPageCount)
    },

    'window.scrollY' (to) {
      console.log('scroll height changed:' + to)
    },

    showSearchContainer(show) {
      if(!show)
        this.$wood.logViewContainer.rightViewWidth = 0
    }
  },
  methods: {

    logItemClick(idx) {
      console.log(idx)
      this.$store.dispatch('UPDATE_CVLOG_CURRENT_LOGID',
        { 'logid': idx }
      )
    },

    updateExportProgress(ratio) {
      this.$store.dispatch('UPDATE_EXPORT_PROGRESS',
        {
          'processing': true,
          'ratio': ratio
        })
    },
  
    async onExportClick(){
      let log_id = undefined
      let logOutputUUID = undefined

      this.updateExportProgress(5)

      /* exportに必要なlog_idを識別するため、タスクIDをpecker moduleからgetする */
      try { 
        let response = await this.axios.get('/pecker/' +  this.task_id)

        this.updateExportProgress(10)

        console.log('pecker task for exporting:' + response.data.status)

        log_id = response.data.log_id
        logOutputUUID = response.data.output
        console.log(log_id)
      }
      catch(error){
        this.$store.dispatch('UPDATE_EXPORT_PROGRESS', { 'processing': false, 'ratio': 0 })
        console.log(error)
        return
      }
      /* exporter moduleにexport対象のlogをtext化させる */
      try{
        let response = await this.axios.post('/exporter/',
          { 'log_id': log_id,
            'uuid': logOutputUUID
          })
        this.updateExportProgress(15)

        console.log('exporter task:' + response.data.task_id)
        /* 辞書データのtext化タスクが完了するまでポーリング */
        this.retrieveExportStatus(response.data.task_id, 15)
      }
      catch(error){
        this.$store.dispatch('UPDATE_EXPORT_PROGRESS', { 'processing': false, 'ratio': 0 })
        console.log(error)
        return
      }
    },

    retrieveExportStatus(task_id, ratio) {
      delay(3000)('retry').then((result) => {
        /* ファイルサイズが大きくexport時間が１分２５秒を超える場合、表示更新は85で止まる */
        if (ratio < 90){
          ratio = ratio + 5
        }

        this.axios.get('/exporter/' +  task_id)
        .then(response => {
          console.log('export task status:' + response.data.status)
          if(response.data.status == 'running') {
            this.$store.dispatch('UPDATE_EXPORT_PROGRESS', {'processing':true, 'ratio':ratio})
            this.retrieveExportStatus(task_id, ratio)
          }
          else if(response.data.status == 'success') {
            this.updateExportProgress(90)

            const linkEl = document.createElement('a')
            linkEl.href = this.axios.defaults.baseURL + '/exporter/download/' + response.data.output
            console.log(this.log_obj.filename)
            linkEl.download = this.log_obj.filename + 'txt'
            document.body.appendChild(linkEl)
            linkEl.click()
            linkEl.parentNode.removeChild(linkEl)

            this.updateExportProgress(100)

          }
          else if(response.data.status == 'failed') {
            this.$store.dispatch('UPDATE_EXPORT_PROGRESS', {'processing':false, 'ratio':0})           
          }
          else {
            console.log('retry')
            this.retrieveExportStatus(task_id,ratio)
          }
        })
        .catch(error=>{
          this.$store.dispatch('UPDATE_EXPORT_PROGRESS', {'processing':false, 'ratio':0})           
          console.log(error)
        });
      });
    },

    search() {
      console.log('open')
      this.$store.dispatch('SHOW_SEARCH_DIALOG')
    },

    gotoLog(index) {

      let gotoPage = Math.floor(index / this.perPageCount) + 1

      /** fetch logs in case page turning occurs */
      if ( gotoPage != this.page )
      {
        this.highLightIndex = Number(index)

        console.log('goto page:' + gotoPage)
        this.$router.push({ name: 'log_view',
          params: {
            task_id: this.task_id,
            page: gotoPage
          },
        })
      }
      else
      {
        /** set highlight here because fetch method doesn't work, */
        /** when there is no page turning.                        */
        this.highlight = [...this.logs.values()].map((log, idx) => {
          return log.index == Number(index)
        })
      } 
      this.focus = Number(index)

      this.$store.dispatch('UPDATE_CVLOG_CURRENT_LOGID',
        { 'logid': this.focus }
      )
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

      this.axios.post('/pecker/cvlog/' + task_id + '/search',
        {
          'retrieve' : true,
          'count': this.perPageCount
        })
      .then(response => {


        this.$store.dispatch('UPDATE_CVLOG_SEARCH_TASK_ID', {
          'search_task_id': task_id
        })

        this.$store.dispatch('UPDATE_CVLOG_SEARCH_OBJECT', {
          'search_log_obj': response.data
        })

        this.$store.dispatch('HIDE_PROCESS_PROGRESS')
        this.$store.dispatch('SHOW_SEARCH_CONTAINER')

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
      this.$store.dispatch('SHOW_GOTO_DIALOG')
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
      /* let the focus move to the first line, when turning pages*/
      this.focus = Number((nextPage-1)*this.perPageCount)  
    },

    fetchBackLog() {
      console.log('back forward')

      let prevPage = parseInt(this.page) - 1
      if(prevPage <= 0)
        return
            
      this.$router.push({ name: 'log_view',
        params: {
          task_id: this.task_id,
          page: prevPage
        }})
      /* let the focus move to the first line, when turning pages*/
      this.focus = Number((prevPage-1)*this.perPageCount)  
    },

    fetchLog(from, doneHandler = () => {} ) {
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

        console.log(response.data.filename)
        console.log(response.data.size)
        this.$store.dispatch('UPDATE_CVLOG_OBJECT', {
         'log_obj': response.data
        })

        doneHandler()

        /* set highlight if given a index to highlight by gotolog method */
        if( this.highLightIndex > -1 )
        {
          this.highlight = [...this.logs.values()].map((log, idx) => {
            return log.index == Number(this.highLightIndex)
          })
        }

        let page = (from / this.perPageCount) + 1
        let pageInfo = 'page: ' + page + '/' + this.log_obj.total_pages
        
        this.updateToolBar(pageInfo, (idx) => {
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
      'title': this.log_obj.filename,
        'menuComponents': [
          { 'type': 'export', 'iconType': 'get_app', 'handler': this.onExportClick },
          { 'compType': 'itemlistbutton', 'title': info,
            'items': items,
            'handler': handler
          },
          { 'type': 'flat', 'text': 'GOTO', 'handler': this.onGotoClick },
          { 'type': 'icon', 'iconType': 'arrow_back_ios', 'handler': this.fetchBackLog },
          { 'type': 'icon', 'iconType': 'arrow_forward_ios', 'handler': this.fetchForwardLog },
        ]})
    },

    handleResize() {
      this.$wood.logViewContainer.windowHeight = window.innerHeight
      this.$wood.logViewContainer.windowWidth = this.$el.clientWidth
    },
  },

  ready: function () {
  },

  mounted() {
    console.log('fetch cvlog')
    this.fetchLog((this.page - 1) * this.perPageCount)

    this.$nextTick().then(() => {
      this.handleResize()
    })
  },

  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
  },

  created() {
    this.$eventHub.$on('search-log-item-click', (idx) => {
      this.gotoLog(idx)
    })

    window.addEventListener('resize', this.handleResize)
  },

  components: {
    LogComponent,
    SearchDialog,
    GotoLogDialog,
    'logdata-table': MainLogDataTable,
    'multitoolbar': MultiFunctionToolBar,
    'searchresult-container': SearchResultContainer,
    'bottomview': BottomViewContainer,
  }
}

</script>
