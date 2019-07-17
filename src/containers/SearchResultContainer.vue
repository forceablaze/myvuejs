<template>

  <resizable class="sidebar-right" :defaultHeight="defaultHeight" :defaultWidth="defaultWidth">
    <v-layout>
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

    <div class="scroll-y" style="height: 100%;">
      <logdata-table
        style="padding-bottom: 32px;"
        @click="logItemClick"
        :headers="tableHeaders"
        :logs="searchResultLogs" :rowsPerPage="200" :simple="true"/>
    </div>
  </resizable>

</template>

<style>

.sidebar-right {
  position: fixed;
  margin-top: 128px;
  padding-bottom: 32px;
  top: 0px;
  z-index: 3;
}

</style>


<script>

import LogDataTable from '@/components/LogDataTable'
import ResizableComponent from '@/components/ResizableComponent'
import ItemListButton from '@/components/buttons/ItemListButton'

import { mapState } from 'vuex'

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

  props: ['defaultHeight', 'defaultWidth'],

  methods: {
    pageButtonClick(idx) {
      this.fetchSearchResult(Number(idx))
    },

    logItemClick(idx) {
      this.$eventHub.$emit('search-log-item-click', idx)
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
    }
  },

  computed: mapState({

    task_id: state => state.cvlog.search_task_id,

    searchResultLogs: state => state.cvlog.search_log_obj.logs,

    pageButtonItems: state => {
      if(state.cvlog.search_log_obj === undefined)
        return []

      let totalPages = state.cvlog.search_log_obj.total_pages
      return [...Array(totalPages).keys()].map((idx) => {
        return {'title': String(idx + 1) }
      })
    },

    showResultPageButton: state => {
      return Object.keys(state.cvlog.search_log_obj).length !== 0
    },

    searchPageInfo: state => {
      if(Object.keys(state.cvlog.search_log_obj).length === 0)
        return ''
      let page = state.cvlog.search_log_obj.page
      let total_pages = state.cvlog.search_log_obj.total_pages

      return 'page: ' + page + '/' + total_pages
    },
  }),

  components: {
    'logdata-table': LogDataTable,
    'resizable': ResizableComponent,
    'itemlistbutton': ItemListButton,
  }
}
</script>
