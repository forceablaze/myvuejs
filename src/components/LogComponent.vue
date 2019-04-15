<template>

    <v-layout row>
      <v-layout column>
        <v-flex d-flex sm2>
          <v-layout row>
            <v-flex xs12 d-flex>
              <v-card style="background-color:#88FFFF; max-width: 200px">
                <v-card-text>{{ log.logtype }}</v-card-text>
              </v-card>
              <v-card
                style="background-color:#88FFFF;"
              >

                <v-card-text>{{ log.loglevel }}</v-card-text>
              </v-card>
              <v-card
                style="background-color:#88FFFF;"
              >
                <v-card-text>{{ 'logid: ' + log.logid }}</v-card-text>
              </v-card>
              <v-card
                style="background-color:#88FFFF;"
              >
                <v-card-text>{{ log.usage }}</v-card-text>
              </v-card>
              <v-card
                style="background-color:#88FFFF;"
              >
                <v-card-text>{{ payload_size_info }}</v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>

        <v-flex d-flex sm2>
          <v-layout row>
            <v-flex xs12 d-flex>
              <v-card
                style="background-color:#13EEFF; font-size:18px;"
              >
                <v-card-text>{{ 'OwnID: ' + log.own_domain + '/' + log.own_subsys }}</v-card-text>
              </v-card>
              <v-card
                style="background-color:#13EEFF; font-size:18px;"
              >

                <v-card-text style="max-width: 100%; word-wrap: break-word;">
                  {{ 'DestID: ' + log.dest_domain + '/' + log.dest_subsys }}
                </v-card-text>
              </v-card>
              <v-card
                style="background-color:#13EEFF; font-size:18px;"
              >
                <v-card-text>{{ 'TaskID: ' + log.task_domain + '/' + log.task_subsys }}</v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>

        <v-flex d-flex xs12>

          <hex-viewer-component
            v-if="showRaw"
            :hexs="raw"
          ></hex-viewer-component>
          <v-card v-else style="font-size: 24px;">
            <v-card-text
              style="white-space: pre-wrap; word-wrap: break-word;"
            >{{ text }}</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>

      <v-flex d-flex style="max-width: 6%;">
        <v-layout row wrap>
          <v-flex>
            <v-card
              style="background-color: #DDFFFF;"
            >
              <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.dest }}</v-card-text>
            </v-card>

            <v-card
              style="background-color: #DDFFFF;"
            >
              <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.format }}</v-card-text>
            </v-card>

            <v-card
              style="background-color: #DDFFFF;"
            >
              <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.seq }}</v-card-text>
            </v-card>

            <v-card
              style="background-color: #DDFFFF;"
            >
              <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.cputype }}</v-card-text>
            </v-card>

            <v-card
              style="background-color: #DDFFFF;"
            >
              <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ '0x' + log.position }}</v-card-text>
            </v-card>
            <v-switch
              v-model="showRaw"
              style="background-color: #EEEEEE;"
              label="生データ"></v-switch>
          </v-flex>
        </v-layout>
      </v-flex>

    </v-layout>

</template>

<style>
.v-label {
  font-size: 12px;
}

.v-input__slot {
  margin: auto;
}

.v-messages {
  min-height: 0px;
  min-width: 0px;
}

.v-input--selection-controls {
  margin: auto;
  padding-top: 0px;
}

.v-input--selection-controls:not(.v-input--hide-details) .v-input__slot {
  margin-bottom: 0px;
}

</style>


<script>

import HexViewerComponent from '@/components/HexViewerComponent'

export default {
  name: 'log-component',

  data() {
    return {
      showRaw: false,
      panel: false
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
