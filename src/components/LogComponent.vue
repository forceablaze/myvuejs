<template>
  <v-expansion-panel-content>
    <template v-slot:header>
      <v-flex>
        <v-layout row>
          <v-flex d-flex xs1 style="font-size: 18px;">
            <span>{{ log.index }}</span>
          </v-flex>
          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 100px;"> 
            <span>{{ log.time }}</span>
          </v-flex>
          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 200px"> 
            <span>{{ log.apitype }}</span>
          </v-flex>

          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 100px"> 
            <span>{{ log.flag }}</span>
          </v-flex>

          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 100px"> 
            <span>{{ log.direction }}</span>
          </v-flex>

          <v-divider vertical></v-divider>

          <v-flex d-flex style="width: 100px"> 
            <span>{{ log.logid }}</span>
          </v-flex>
          <v-divider vertical></v-divider>

          <v-flex d-flex xs12> 
            <span>{{ formatted_text }}</span>
          </v-flex>
        </v-layout>
      </v-flex>
    </template>

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
            <v-card-text>
              {{ text }}
            </v-card-text>
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

  </v-expansion-panel-content>

</template>

<style>
.v-expansion-panel__header {
  background-color: #CBFFD3;
  padding: 0px 0px 0px 0px;
  min-height: 0px;
}
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
    }
  },

  props: ['log'],

  mounted() {
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
