<template>
  <v-container>
    <search-dialog ref="search_dialog">
    </search-dialog>

    <v-data-table
      :headers="headers"
      :items="logs"
      :expand="true"
      item-key="index"
      loading="true"
      :rows-per-page-items="rowsPerPageItems"
			:pagination.sync="pagination"
    >

      <template v-slot:items="props">
        <tr @click="itemClicked(props)" style="background-color: #CBFFD3;">
            <td>{{ props.item.index }}</td>
            <td>{{ props.item.time }}</td>
            <td>{{ props.item.apitype }}</td>
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

export default {
  data() {
    return {
      logs: [],
      expand: false,
      count: 0,
      log_obj: {},
      log: {},
      showAll: false,
      currentPageIndex: 0,
      headers: [
        { text: 'index', value: 'index'},
        { text: 'time', value: 'time' },
        { text: 'apitype', value: 'apitype' },
        { text: 'flag', value: 'flag' },
        { text: 'direction', value: 'direction' },
        { text: 'logid', value: 'logid' },
        { text: 'data', value: 'data' },
      ],
      rowsPerPageItems: [25, 50, {text: 'All', value: -1}],
      pagination: {
        rowsPerPage: 50
      },
    }
  },

  props: ['task_id', 'page'],

  watch: {
    '$route' (to, from) {
      console.log(to.params.page)
      this.fetchLog()
    }
  },
  methods: {
    itemClicked(props) {
      props.expanded = !props.expanded
    },
    showAllLog() {
      this.panel = [...this.logs.keys()].map(_ => true)
    },
    // Reset the panel
    hideAllLog() {
      this.panel = []
    },

    search() {
      console.log('open')
      this.$refs.search_dialog.open()
    },

    fetchForwardLog() {
      console.log('fetch forward')
      this.$router.push({ name: 'log_view',
        params: {
          task_id: this.task_id,
          page: parseInt(this.page) + 1
        }})
    },

    fetchBackLog() {
      console.log('back forward')
      this.$router.push({ name: 'log_view',
        params: {
          task_id: this.task_id,
          page: parseInt(this.page) - 1
        }})
    },

    fetchLog() {
      let from = (this.page - 1) * 200

      console.log('fetch log ' + from)

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

  mounted() {
    console.log('fetch cvlog')
    this.fetchLog()
  },

  components: {
    LogComponent,
    SearchDialog
  }
}

</script>
