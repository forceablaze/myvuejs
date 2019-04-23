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

    <v-data-table
      ref="table"
      :headers="headers"
      :items="logs"
      :expand="true"
      item-key="index"
      loading="true"
      :rows-per-page-items="rowsPerPageItems"
			:pagination.sync="pagination"
      hide-actions
    >

      <template v-slot:items="props">
        <tr @click="itemClicked(props)"
          v-bind:style="[highlight[props.index] ? { 'background-color': '#FF3333' } : { 'background-color': '#CBFFD3' }]"
        >
            <td>{{ props.item.index }}</td>
            <td>{{ props.item.time }}</td>
            <td v-if="checkAPIType(props.item.apitype)">{{ props.item.apitype }}</td>
            <td v-else>{{ 'PF ' + props.item.own_domain + '/' + props.item.own_subsys  }}</td>
            <td>{{ props.item.flag }}</td>
            <td>{{ props.item.direction }}</td>
            <td>{{ props.item.logid }}</td>
            <td v-if="props.item.format=='binary'">{{ props.item.formatted_text.substring(0, 90) }}</td>
            <td v-else-if="props.item.format=='text'">{{ props.item.text.substring(0, 90) }}</td>
        </tr>
      </template>
      <template v-slot:expand="props">
        <log-component
          :log="props.item"
        >
        </log-component>
      </template>
    </v-data-table>
    </v-container>


    <div
      v-show="showSearchResult"
    >
      <v-flex d-flex xs12 style="background-color: #DDDDDD;">
        <span>Search Result</span>
      </v-flex>

      <v-container
        class="scroll-y"
        style="max-height: 400px"
      >

        <v-data-table
          height="400"
          ref="table"
          :headers="headers"
          :items="searchResultLogs"
          :expand="true"
          item-key="index"
          loading="true"
          hide-headers
          :rows-per-page-items="searchRowsPerPageItems"
          :pagination.sync="searchPagination"
        >
          <template v-slot:items="props">
            <tr @click="itemClicked(props)"
              v-bind:style="{ 'background-color': '#CBFFD3' }"
            >
              <td>{{ props.item.index }}</td>
              <td>{{ props.item.time }}</td>
              <td v-if="checkAPIType(props.item.apitype)">{{ props.item.apitype }}</td>
              <td v-else>{{ props.item.apitype + ' ' + props.item.own_domain + '/' + props.item.own_subsys  }}</td>
              <td>{{ props.item.flag }}</td>
              <td>{{ props.item.direction }}</td>
              <td>{{ props.item.logid }}</td>
              <td v-if="props.item.format=='binary'">{{ props.item.formatted_text }}</td>
              <td v-else-if="props.item.format=='text'">{{ props.item.text }}</td>
            </tr>
          </template>
          <template v-slot:expand="props">
            <log-component
              :log="props.item"
            >
           </log-component>
          </template>
        </v-data-table>
      </v-container>
    </div>

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

export default {
  data() {
    return {
      logs: [],
      searchResultLogs: [],
      highlight: [],
      bodyHeight: 0,
      expand: false,
      count: 0,
      log_obj: {},
      showAll: false,
      showSearchResult: false,
      watchScrollHeightTimer: undefined,
      headers: [
        { text: 'index', value: 'index'},
        { text: 'time', value: 'time' },
        { text: 'apitype', value: 'apitype' },
        { text: 'flag', value: 'flag' },
        { text: 'direction', value: 'direction' },
        { text: 'logid', value: 'logid' },
        { text: 'data', value: 'data' },
      ],
      rowsPerPageItems: [{text: 'All', value: -1}],
      pagination: {
        rowsPerPage: 200
      },
      searchRowsPerPageItems: [{text: 'All', value: -1}],
      searchPagination: {
        rowsPerPage: 20
      },
    }
  },

  props: ['task_id', 'page'],

  computed: {
    'pageInfo' () {
      return 'page: ' + this.page + '/' + this.log_obj.total_pages
    },
    'upperContainerHeight' () {
      return String(this.bodyHeight - 800) + 'px'
    }
  },

  watch: {
    '$route' (to, from) {
      console.log(to.query)
      this.fetchLog((this.page - 1) * 200)
    },
    'window.scrollY' (to) {
      console.log('scroll height changed:' + to)
    }
  },
  methods: {
    checkAPIType(apitype) {
      return isNaN(Number(apitype))
    },
    handleResize() {
      console.log('size changed')
      window.scrollTo(0, document.body.scrollHeight)
    },

    itemClicked(props) {
      props.expanded = !props.expanded
    },

    showAllLog() {
      for(let i = 0; i < this.logs.length; i += 1) {
        const log = this.logs[i]
        this.$set(this.$refs.table.expanded, log.index, true)
      }
    },
    // Reset the panel
    hideAllLog() {
      for(let i = 0; i < this.logs.length; i += 1) {
        const log = this.logs[i]
        this.$set(this.$refs.table.expanded, log.index, false)
      }
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

    searchLog(data) {
      console.log('search log')
      console.log(data)

      this.$store.dispatch('SHOW_PROCESS_PROGRESS', {
        'title': 'Loading...'
      })

      this.axios.post('/pecker/cvlog/' + this.task_id + '/search', data)
      .then(response => {
        // relese obj
        this.searchResultLogs = null

        // Automatic transforms for JSON data
        this.searchResultLogs = response.data.logs


        let lastHeight = document.body.scrollHeight
        console.log(lastHeight)

        this.updateToolBar('BACK', () => {
          this.fetchLog((this.page - 1) * 200)
          this.showSearchResult = false
        })

        this.showSearchResult = true

        let run = () => {
          let newHeight = document.body.scrollHeight

          if(newHeight != lastHeight) {
            window.scrollTo(0, newHeight)
            this.bodyHeight = newHeight
            clearTimeout(this.watchScrollHeightTimer)
            return
          }

          if(this.watchScrollHeightTimer)
            clearTimeout(this.watchScrollHeightTimer)

          this.watchScrollHeightTimer = setTimeout(run, 200)
        }

        this.watchScrollHeightTimer = setTimeout(run, 200)

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
      //let from = (this.page - 1) * 200
      console.log(typeof from)

      console.log('fetch log ' + from)
      this.$store.dispatch('SHOW_PROCESS_PROGRESS', {
        'title': 'Loading...'
      })

      this.axios.post('/pecker/cvlog', {
        task_id: this.task_id,
        from: from,
      })
      .then(response => {
        // relese obj
        this.log_obj = null
        delete this.log_obj

        // Automatic transforms for JSON data
        this.log_obj = response.data
        this.logs = this.log_obj.logs

        doneHandler()
        this.updateToolBar(this.pageInfo)

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
          { 'type': 'flat', 'text': info, 'handler': handler },
          { 'type': 'flat', 'text': 'GOTO', 'handler': this.onGotoClick },
          { 'type': 'icon', 'iconType': 'search', 'handler': this.search },
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

  ready: function () {
    window.addEventListener('resize', this.handleResize)
  },

  beforeDestroy: function () {
    window.removeEventListener('resize', this.handleResize)
    clearInterval(this.watchScrollHeightTimer)
    this.logs = null
    delete this.logs
    this.log_obj = null
    delete this.log_obj
    this.searchResultLogs = null
    delete this.searchResultLogs
  },

  mounted() {
    console.log('fetch cvlog')

    this.fetchLog((this.page - 1) * 200)
  },

  components: {
    LogComponent,
    SearchDialog,
    GotoLogDialog
  }
}

</script>
