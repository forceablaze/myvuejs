<template>
        <v-data-table
          height="400"
          ref="table"
          :headers="headers"
          :items="logs"
          :expand="true"
          item-key="index"
          loading="true"
          hide-headers
          :rows-per-page-items="rowsPerPageItems"
          :pagination.sync="pagination"
        >
          <template v-slot:items="props">
            <tr @click="itemClicked(props)"
              v-bind:style="{ 'background-color': '#CBFFD3' }"
            >
              <td>{{ props.item.index }}</td>
              <td>{{ props.item.time }}</td>
              <td v-if="checkAPIType(props.item.apitype)">{{ props.item.apitype }}</td>
              <td v-else>{{ 'PF ' + props.item.own_domain + '/' + props.item.own_subsys  }}</td>
              <td>{{ props.item.flag }}</td>
              <td>{{ props.item.direction }}</td>
              <td>{{ props.item.logid }}</td>
              <td v-if="props.item.format=='binary'">{{ checkElement(props.item.formatted_text).substring(0, 90) }}</td>
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

</template>

<style>
table.v-table tbody td, table.v-table tbody th {
  height: auto;
}
</style>

<script>

import LogComponent from '@/components/LogComponent'

export default {
  name: 'logdata-table',
  data() {
    return  {
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
      pagination: { rowsPerPage: this.rowsPerPage }
    }
  },
  props: [ "rowsPerPage", "logs"],

  methods: {
    checkElement(element) {
      if(element == null)
        return 'null'
      return element
    },

    checkAPIType(apitype) {
      return isNaN(Number(apitype))
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

  },
  components: {
    LogComponent,
  }
}
</script>
