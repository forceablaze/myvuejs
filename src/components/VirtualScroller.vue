<template>
  <div class="content">

    <DynamicScroller
      :items="logs"
      :min-item-size="20"
      key-field="index"
      class="scroller"
    >

        <!--
      <template #before>
        <div class="header"
          v-for="(header, index) in tableHeaders"
        >
            {{ header.value }}
        </div>
      </template>
        -->

      <template v-slot="{ item, index, active }">
        <DynamicScrollerItem
          :item="item"
          :index="index"
          :active="active"
          :data-active="active"
          :data-index="index"
          class="logitem"
        >

          <logtableitem :logitem="item"/>

        </DynamicScrollerItem>
      </template>
    </DynamicScroller>

    <!--
    <RecycleScroller
      class="scroller"
      :items="logs"
      :item-size="30"
      key-field="index"
    >

      <template v-slot="props">


            <div class="td" v-if="!simple">{{ props.item.time }}</div>
            <div class="td" v-if="checkAPITypeIsNotNumber(props.item.apitype)">{{ props.item.apitype }}</div>
            <div class="td" v-else>{{ 'PF ' + props.item.own_domain + '/' + props.item.own_subsys  }}</div>
            <div class="td" v-if="!simple">{{ props.item.flag }}</div>
            <div class="td" v-if="!simple">{{ props.item.direction }}</div>
            <div class="td" v-if="!simple">{{ props.item.logid }}</div>
            <div class="td">{{ getLogSummaryString(props.item) }}</div>

          <td>{{ props.item.index }}</td>
          <td v-if="!simple">{{ props.item.time }}</td>
          <td v-if="checkAPITypeIsNotNumber(props.item.apitype)">{{ props.item.apitype }}</td>
          <td v-else>{{ 'PF ' + props.item.own_domain + '/' + props.item.own_subsys  }}</td>
          <td v-if="!simple">{{ props.item.flag }}</td>
          <td v-if="!simple">{{ props.item.direction }}</td>
          <td v-if="!simple">{{ props.item.logid }}</td>
          <td>{{ getLogSummaryString(props.item) }}</td>
      </template>
    </RecycleScroller>
    -->
  </div>

</template>

<style scoped>

.content {
  border: solid 5px #42b983;
  overflow: hidden;
  height: 500px;
}

.scroller {
  height: 100%;
  width: 100%;
  background-color: rgb(203, 255, 211);
}

</style>


<script>

import LogComponent from '@/components/LogComponent'
import LogTableItem from '@/components/LogTable/LogTableItem'

export default {
  name: 'virtualscroller',

  components: {
    LogComponent,
    'logtableitem': LogTableItem,
  },


  data() {
    return {
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

  props: {
    headers: Array,
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
    logs () {
      if(Object.keys(this.$store.state.cvlog.log_obj).length != 0)
        return this.$store.state.cvlog.log_obj.logs
      return []
    },
  },

  methods: {
    checkElement(element) {
      if(element == null)
        return 'null'
      return element
    },


    checkAPITypeIsNotNumber(apitype) {
      return isNaN(Number(apitype))
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

    fetchLog() {
      this.axios.post('/pecker/cvlog', {
        task_id: "141446ad-2498-4c07-af39-b44696e9d096",
        from: 0,
        count: 1000,
      })
      .then(response => {
        this.$store.dispatch('UPDATE_CVLOG_OBJECT', {
         'log_obj': response.data
        })
        console.log(response.data.logs.length)
      })
    }
  },

  mounted() {
    this.$nextTick(this.fetchLog())
  },
}

</script>
