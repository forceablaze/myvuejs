<template>

  <resizable class="bottom-container" :defaultHeight="defaultHeight">
    <v-layout row>
      <v-flex style="background-color: #DDDDDD;">
        <span style="font-size: 20px;">Search Result</span>
      </v-flex>
      <v-flex xs1 style="background-color: #DDDDDD;">
        <itemlistbutton
          :fontSize="fontSize"
          :height="buttonHeight"
          @click="pageButtonClick"
          v-if="showResultPageButton" :title="searchPageInfo" :items="pageButtonItems"/>
      </v-flex>
    </v-layout>

    <div class="scroll-y" style="height: 100%; margin-bottom: 36px">
      <logdata-table :logs="searchResultLogs" :rowsPerPage="200"/>
    </div>
  </resizable>

</template>

<style>

.bottom-container {
  background-color: white;
}

</style>


<script>

import LogDataTable from '@/components/LogDataTable'
import ResizableComponent from '@/components/ResizableComponent'
import ItemListButton from '@/components/buttons/ItemListBUtton'

import { mapState } from 'vuex'

export default {

  name: 'searchresult-container',

  data() {
    return {
      fontSize: '14',
      buttonHeight: '20',
      perPageCount: 500
    }
  },

  props: ['defaultHeight'],

  methods: {
    pageButtonClick(idx) {
      this.fetchSearchResult(Number(idx))
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

        this.$store.dispatch('SHOW_BOTTOM_CONTAINER')

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
