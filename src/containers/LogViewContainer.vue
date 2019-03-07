<template>
  <v-container>
    <v-layout column>
      <button v-on:click="add()">add</button>
      <v-btn @click="all">all</v-btn>
      <v-btn @click="none">none</v-btn>

      <v-flex>
        <v-card dark color="primary">
          <v-card-text>one</v-card-text>
        </v-card>
      </v-flex>

      <v-flex>
        <v-expansion-panel v-model="panel" expand>
          <log-component v-for="(log, index) in logs" :key="index"></log-component>
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
      count: 0
    }
  },
  methods: {
    add() {
      this.count++
      console.log('add')
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

  components: {
    LogComponent
  }
}

</script>
