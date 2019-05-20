<template>
        <v-data-table
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
              v-bind:id="'log_' + `${props.item.index}`"
              v-bind:style="[highlight[props.index] ? { 'background-color': '#FF3333' } : { 'background-color': '#CBFFD3' }]"
            >
              <td>{{ props.item.index }}</td>
              <td v-if="!simple">{{ props.item.time }}</td>
              <td v-if="checkAPIType(props.item.apitype)">{{ props.item.apitype }}</td>
              <td v-else>{{ 'PF ' + props.item.own_domain + '/' + props.item.own_subsys  }}</td>
              <td v-if="!simple">{{ props.item.flag }}</td>
              <td v-if="!simple">{{ props.item.direction }}</td>
              <td v-if="!simple">{{ props.item.logid }}</td>
              <td>{{ getLogSummaryString(props.item) }}</td>
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
  props: {
    rowsPerPage: Number,
    logs: Array,
    focus: Number,
    highlight: {
      type: Array,
      default: () => { return [] }
    },
    simple: {
      type: Boolean,
      default: false
    }
  },

  watch: {
    focus: function(val) {
      this.$nextTick(function () {
        setTimeout(() => {
          if(val !== undefined)
            this.focusTo(val)
        }, 300)
      })
    }
  },

  methods: {
    checkElement(element) {
      if(element == null)
        return 'null'
      return element
    },

    getLogSummaryString(item) {
      if(item.format == 'binary') {
        let len = 90
        if(this.simple)
          len = 30
        return this.checkElement(item.formatted_text).substring(0, len)
      }
      else if(item.format == 'text') {
        return item.text
      }
    },

    checkAPIType(apitype) {
      return isNaN(Number(apitype))
    },

    itemClicked(props) {
      props.expanded = !props.expanded
    },

    focusTo(index) {
      const focusLogElem = this.$el.querySelector("#log_" + index)
      window.scrollTo({
        top: focusLogElem.offsetTop,
        behavior: 'smooth'
      })
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

  mounted() {
  },

  components: {
    LogComponent,
  }
}
</script>
