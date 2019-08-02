<template>

  <resizable class="sidebar-right"
    horizontal
    left
    :defaultWidth="defaultWidth"
    :defaultHeight="viewHeight"
    @resize="resize">
    <v-layout column style="padding-left: 4px;">
      <v-layout row>
        <v-flex grow  style="background-color: #DDDDDD;">
          <span style="font-size: 20px;">Search Result</span>
        </v-flex>
        <v-flex shrink style="background-color: #DDDDDD;">
          <itemlistbutton
            :fontSize="fontSize"
            :height="buttonHeight"
            @click="pageButtonClick"
            v-if="showResultPageButton" :title="searchPageInfo" :items="pageButtonItems"/>
        </v-flex>
      </v-layout>

      <div style="height: 100%;">
        <logdata-table
          style="padding-bottom: 32px;"
          @click="logItemClick"
          :headers="tableHeaders"
          :logs="searchResultLogs" :rowsPerPage="200" :simple="true"/>
      </div>
    </v-layout>
  </resizable>

</template>

<style>

.sidebar-right {
  position: fixed;
  margin-top: 128px;
  padding-bottom: 32px;

  bottom: 0px;
  right: 0px;

  border-bottom: 4px solid #DDDDDD;
  top: 0px;
  z-index: 3;
}

</style>


<script>

import LogDataTable from '@/components/LogDataTable'
import ResizableComponent from '@/components/ResizableComponent'
import ItemListButton from '@/components/buttons/ItemListButton'

import DataTable from '@/components/DataTable'
const SmallDataTable = {
  extends: DataTable,

  computed: {
    dataTableHeight() {
      return this.$wood.logViewContainer.windowHeight -
        this.$wood.logViewContainer.bottomViewHeight -
        160
    },
    dataTableWidth() {
      return this.$wood.logViewContainer.rightViewWidth
    }
  }
}

const MainLogDataTable = {
  extends:  LogDataTable,

  components: {
    'datatable': SmallDataTable,
  }
}


export default {

  name: 'searchresult-container',

  data() {
    return {
      fontSize: '14',
      buttonHeight: '20',
      perPageCount: 500,
      tableHeaders: [
        { text: 'index', value: 'index'},
        { text: 'apitype', value: 'apitype' },
        { text: 'data', value: 'data' },
      ],
    }
  },

  props: ['defaultWidth'],

  methods: {
    pageButtonClick(idx) {
      this.fetchSearchResult(Number(idx))
    },

    logItemClick(idx) {
      this.$eventHub.$emit('search-log-item-click',
        this.searchResultLogs[idx].index)
    },

    async fetchSearchResult(page) {
      console.log('fetch search result' + this.task_id)
      this.$store.dispatch('SHOW_PROCESS_PROGRESS', {
        'title': 'Loading...'
      })

      try {
        let response = await this.axios.post('/pecker/cvlog/' + this.task_id + '/search', {
          'retrieve' : true,
          'page': page,
          'count': this.perPageCount,
        })

        this.$store.dispatch('UPDATE_CVLOG_SEARCH_OBJECT', {
          'search_log_obj': response.data
        })

        this.$store.dispatch('SHOW_SEARCH_CONTAINER')

      }
      catch(error) {
      }

      this.$store.dispatch('HIDE_PROCESS_PROGRESS')
    },

    resize(dim) {
      this.$wood.logViewContainer.rightViewWidth = dim.width
    }
  },

  computed: {

    task_id() {
      return this.$store.state.cvlog.search_task_id
    },

    searchResultLogs() {
      return this.$store.state.cvlog.search_log_obj.logs
    },

    pageButtonItems() {
      if(this.$store.state.cvlog.search_log_obj === undefined)
        return []

      let totalPages = this.$store.state.cvlog.search_log_obj.total_pages
      return [...Array(totalPages).keys()].map((idx) => {
        return {'title': String(idx + 1) }
      })
    },

    showResultPageButton() {
      return Object.keys(this.$store.state.cvlog.search_log_obj).length !== 0
    },

    searchPageInfo() {
      if(Object.keys(this.$store.state.cvlog.search_log_obj).length === 0)
        return ''
      let page = this.$store.state.cvlog.search_log_obj.page
      let total_pages = this.$store.state.cvlog.search_log_obj.total_pages

      return 'page: ' + page + '/' + total_pages
    },

    viewHeight() {
      return this.$wood.logViewContainer.windowHeight -
        this.$wood.logViewContainer.bottomViewHeight -
        128
    },
  },

  mounted() {
    this.$el.addEventListener('resize', this.resize)

    this.$wood.logViewContainer.rightViewWidth = this.defaultWidth
  },

  beforeDestroy() {
    this.$el.removeEventListener('resize', this.resize)
  },

  components: {
    'logdata-table': MainLogDataTable,
    'resizable': ResizableComponent,
    'itemlistbutton': ItemListButton,
  }
}
</script>
