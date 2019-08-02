<template>
      <v-layout column class="logcomp">
        <v-flex d-flex>
          <v-layout row>
            <v-flex d-flex>
              <v-card class="loginfo-1" style="min-width: 200px;">
                <v-card-text>{{ log.logtype }}</v-card-text>
              </v-card>
              <v-card class="loginfo-1" style="max-width: 150px;">
                <v-card-text>{{ log.loglevel }}</v-card-text>
              </v-card>
              <v-card class="loginfo-1">
                <v-card-text>{{ 'logid: ' + log.logid }}</v-card-text>
              </v-card>
              <v-card class="loginfo-1">
                <v-card-text>{{ log.usage }}</v-card-text>
              </v-card>
              <v-card class="loginfo-1">
                <v-card-text>{{ payload_size_info + ', seq: ' + log.seq + ', cputype:' + log.cputype }}</v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>

        <v-flex d-flex>
          <v-layout row>
            <v-flex d-flex>
              <v-card class="loginfo-2">
                <v-card-text>{{ 'OwnID: ' + log.own_domain + '/' + log.own_subsys }}</v-card-text>
              </v-card>
              <v-card class="loginfo-2">

                <v-card-text style="max-width: 100%; word-wrap: break-word;">
                  {{ 'DestID: ' + log.dest_domain + '/' + log.dest_subsys }}
                </v-card-text>
              </v-card>
              <v-card class="loginfo-2">
                <v-card-text>{{ 'TaskID: ' + log.task_domain + '/' + log.task_subsys }}</v-card-text>
              </v-card>
              <v-card class="loginfo-2" style="min-width: 200px;">
                <v-card-text>{{ log.dest }}</v-card-text>
              </v-card>
              <v-card class="loginfo-2" style="max-width: 150px;">
                <v-card-text>{{ log.format }}</v-card-text>
              </v-card>
              <v-card class="loginfo-2" style="max-width: 150px;">
                <v-card-text>{{ '0x' + log.position }}</v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>

        <v-card class="logtext">
          <v-card-text
            style="white-space: pre-wrap; word-wrap: break-word;"
          >{{ text }}</v-card-text>
        </v-card>
        <hex-viewer-component :hexs="raw"/>
      </v-layout>

</template>

<style>

.logcomp .loginfo-1 {
  background-color: #88FFFF;
  font-size: 18px;
}

.logcomp .loginfo-2 {
  background-color: #13EEFF;
  font-size: 18px;
  align-item: center;
}

.logcomp .logtext {
  font-size: 18px;
}

.logcomp .v-card__text {
  padding: 0px;
}

</style>


<script>

import HexViewerComponent from '@/components/HexViewerComponent'

export default {
  name: 'log-component',

  data() {
    return {
      panel: false,
    }
  },

  props: ['log', 'show', 'highlight'],

  mounted() {
  },

  watch: {
    'panel' (to, from) {
      console.log('panel changed:' + to)
    },
    'show' (to, from) {
      console.log('show changed:' + to)
    }
  },

  computed: {
    'raw' () {
      let raw = ''
      this.log.raw.forEach((record) => {
        record.forEach((data) => {
          raw += data
        })
      })
      return raw
    },
    'text' () {
      return this.formatted_text
    },
    'formatted_text' () {
      if(this.log.format == 'binary') {
        return this.log.formatted_text
      }
      else if(this.log.foramt = 'text') {
        return this.log.text
      }
    },
    'payload_size_info' () {
      let str = 'payload size:' + this.log.payload_len

      if(this.log.format == 'binary')
        str += ' (binary data size: ' + this.log.binary_data_len + 'B)'

      return str
    }
  },
  components: {
    HexViewerComponent
  }

}

</script>
