<template>
  <v-container>
    <v-layout column>
      <button v-on:click="add()">add</button>
      <v-btn @click="all">all</v-btn>
      <v-btn @click="none">none</v-btn>

      <v-flex>
        <v-expansion-panel v-model="panel" expand>
          <log-component
            v-for="(log, index) in logs"
            :key="index"
            :log="log">
          </log-component>
        </v-expansion-panel>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

import LogComponent from '@/components/LogComponent'

export default {
  data() {
    return {
      logs: [],
      panel: [],
      count: 0,
      log_obj: {},
      log: {}
    }
  },

  props: ['log_id'],

  watch: {
    '$route' (to, from) {
      console.log(to)
      console.log(from)
    }
  },
  methods: {
    add() {
      this.count++
      console.log('add')
      console.log(this.log_id)
      this.logs.push({
        id: this.count
      })
    },
    all() {
      this.panel = [...this.logs.keys()].map(_ => true)
    },
    // Reset the panel
    none() {
      this.panel = []
    }
  },

  mounted() {
    console.log('fetch cvlog')
    this.axios.post('/pecker/cvlog', {
      log_id: this.log_id
    })
    .then(response => {
      // Automatic transforms for JSON data
      this.log_obj = response.data
      this.logs = this.log_obj.logs
      console.log(this.log_obj.product)
      console.log(this.log_obj.serial_number)
    })
    .catch(error => {
      console.log(error)
    });
  },


  components: {
    LogComponent
  }
}

</script>
