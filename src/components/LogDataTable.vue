<template>
        <!--
        <v-data-table
          class="logtable"
          ref="table"
          :headers="headers"
          :items="logs"
          :expand="true"
          item-key="index"
          loading="true"
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
              <td v-if="checkAPITypeIsNotNumber(props.item.apitype)">{{ props.item.apitype }}</td>
              <td v-else>{{ 'PF ' + props.item.own_domain + '/' + props.item.own_subsys  }}</td>
              <td v-if="!simple">{{ props.item.flag }}</td>
              <td v-if="!simple">{{ props.item.direction }}</td>
              <td v-if="!simple">{{ props.item.logid }}</td>
              <td>{{ getLogSummaryString(props.item) }}</td>
            </tr>
          </template>
        </v-data-table>
          -->
  <datatable
    class="logtable"
    :headers="headers"
  >
    <template v-slot:item>
      <tr
        class="logitem"
        @click="itemClicked(index)"
        v-for="(item, index) in logs"
        v-bind:id="'log_' + `${item.index}`"
        v-bind:style="[highlight[index] ? { 'background-color': '#FF3333' } : { 'background-color': '#CBFFD3' }]"
      >
        <td style="min-width: 40px">{{ item.index }}</td>
        <td v-if="!simple">{{ item.time }}</td>
        <td v-if="checkAPITypeIsNotNumber(item.apitype)">{{ item.apitype }}</td>
        <td v-else>{{ 'PF ' + item.own_domain + '/' + item.own_subsys  }}</td>
        <td v-if="!simple">{{ item.flag }}</td>
        <td v-if="!simple">{{ item.direction }}</td>
        <td v-if="!simple">{{ item.logid }}</td>
        <td>{{ getLogSummaryString(item) }}</td>
      </tr>
    </template>
  </datatable>
</template>

<style scoped>

.logtable {
  height: 100%;
  width: 100%;
  max-width: 100%;
}

.logtable td {
  padding-right: 20px;
  padding-left: 20px;
  text-align: left;
}

.logtable .logitem {
  border-bottom: 1px solid rgba(0,0,0,0.12);
}

.logtable table.v-table tbody td, table.v-table tbody th {
  height: auto;
}

.logtable table.v-table thead tr {
  height: auto;
}

.logtable .v-table__overflow {
    width: 100%;
    height: 400px;
    overflow-x: auto;
    overflow-y: auto;
}

</style>

<script>

import LogComponent from '@/components/LogComponent'
//import { VDataTable } from '@/components/VDataTable'

import DataTable from '@/components/DataTable'

export default {
  name: 'logdata-table',

  data() {
    return  {
      rowsPerPageItems: [{text: 'All', value: -1}],
      pagination: { rowsPerPage: this.rowsPerPage }
    }
  },
  props: {
    headers: Array,
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

  computed: {
    computedTablePaddingRight() {
      console.log(this.$vuetify.application.height)
      return this.$vuetify.application.left
    },
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

    checkAPITypeIsNotNumber(apitype) {
      return isNaN(Number(apitype))
    },

    itemClicked(index) {
      this.$emit('click', index)
    },

    /*
    itemClicked(props) {
      props.expanded = !props.expanded
      this.$emit('click', props.item.index)
    },
    */

    focusTo(index) {
      const focusLogElem = this.$el.querySelector("#log_" + index)
      focusLogElem.scrollIntoView({behavior: "smooth", block: "center"});
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
    'datatable': DataTable,
  }
}
</script>
