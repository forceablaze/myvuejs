<template>
  <v-layout class="item" row>

    <div class="cell index">{{ logitem.index }}</div>
    <div class="cell time" v-if="!simple">{{ logitem.time }}</div>
    <div class="cell api " v-if="checkAPITypeIsNotNumber(logitem.apitype)">{{ logitem.apitype }}</div>
    <div class="cell domain" v-else>{{ 'PF ' + logitem.own_domain + '/' + logitem.own_subsys  }}</div>
    <div class="cell flag" v-if="!simple">{{ logitem.flag }}</div>
    <div class="cell dir" v-if="!simple">{{ logitem.direction }}</div>
    <div class="cell logid" v-if="!simple">{{ logitem.logid }}</div>
    <div class="summary" >{{ getLogSummaryString(logitem) }}</div>

  </v-layout>

</template>


<style scoped>

.item {
  border-bottom: 1px solid rgba(0,0,0,.12);
}

.item > .index {
  width: 100px;
}

.item > .time {
  width: 150px;
}

.item > .api {
  width: 400px;
}

.item > .domain {
  width: 400px;
}

.item > .flag {
  width: 150px;
}

.item > .dir {
  width: 80px;
}

.item > .logid {
  width: 80px;
}

.item > .summary {
  max-width: 100%;
  word-wrap: true;
  break-word: true;
}

.item > .cell {
  padding: 0px 24px;
  border-left: 1px solid rgba(0,0,0,.12);
  border-right: 1px solid rgba(0,0,0,.12);
}

</style>


<script>

export default {
  name: 'logtableitem',

  data() {
    return {
    }
  },

  props: {
    logitem: Object,
    simple: {
      type: Boolean,
      default: false
    }
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
  },
}


</script>
