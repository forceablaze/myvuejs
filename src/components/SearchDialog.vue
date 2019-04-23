<template>
  <v-dialog v-model="dialog" max-width="800">
    <v-card>
      <v-card-title>
        <span class="headline">Search/Filter</span>
      </v-card-title>

      <v-layout row align-center>
        <v-flex xs12 sm2>
          <v-subheader>log format</v-subheader>
        </v-flex>
        <v-flex xs12 sm10>
          <v-card-text>
            <v-select
              :items="logformatItems"
              label="log format"
              v-model="logformatModel"
            ></v-select>
          </v-card-text>
        </v-flex>
      </v-layout>

      <v-layout row align-center>

        <v-flex xs12 sm2>
          <v-subheader>apitype</v-subheader>
        </v-flex>

        <v-flex xs12 sm5>
          <v-card-text>
            <v-autocomplete
              :items="apitypeItems"
              v-model="apitypeModel"
              label="log format"
              @change="apitypeChange"
            ></v-autocomplete>
          </v-card-text>
        </v-flex>

        <v-flex v-if="apitypeModel == -1" xs12 sm5>
          <v-card-text>
            <v-text-field single-line
              label="decimal"
              v-model="apitypeValue">
            </v-text-field>
          </v-card-text>
        </v-flex>
      </v-layout>

      <v-layout row align-center>
        <v-flex xs12 sm2>
        </v-flex>
        <v-flex xs12 sm10>
          <component @change="paramsChange" v-if="currentApitypeParams" :is="currentApitypeParams"/>
        </v-flex>
      </v-layout>

      <v-layout row align-center>
        <v-flex xs12 sm2>
          <v-card-text>
            <v-select
              :items="dataAreaItems"
              label="payload format"
              v-model="dataAreaModel"
            ></v-select>
          </v-card-text>
        </v-flex>

        <v-flex xs12 sm10>
          <v-card-text>
            <v-textarea
            outline
            label="payload"
            height="100"
            :placeholder="dataAreaHolder"
            v-model="dataAreaValue"
            ></v-textarea>
          </v-card-text>
        </v-flex>
      </v-layout>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" flat="flat" @click="search">
          Search
        </v-btn>
        <v-btn color="green darken-1" flat="flat" @click="dialog = false">
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

import ServiceCallParams from '@/components/apitype_params/ServiceCallParams.vue'

export default {
  name: 'search-dialog',

  data () {
    return {
      dialog: false,
      showApitypeInput: '',
      dataAreaLabel: 'text',
      dataAreaValue: '',
      dataAreaModel: 0,
      dataAreaItems: [
        { text: "text", value: 0, },
        { text: "binary", value: 1, },
      ],
      logformatModel: 0,
      logformatItems: [
        { text: "all", value: 0, },
        { text: "text", value: 1, },
        { text: "binary", value: 2, },
      ],
      apitypeModel: -2,
      apitypeValue: 0,
      apitypeItems: [
        { text: "All", value: -2 },
        { text: "API種別：Dbgl API direct", value: 0 },
        { text: "DbguSystemEvent()", value: (1 << 16) },
        { text: "DbguServiceCall()", value: (2 << 16) },
        { text: "DbguScenarioStart()", value: (3 << 16) }, 
        { text: "DbguScenarioStep()", value: (4 << 16) },
        { text: "DbguProhibitionTable()", value: (5 << 16) },
        { text: "DbguDataWrite()", value: (6 << 16) },
        { text: "DbguScenarioExecute()", value: (7 << 16) },
        { text: "DbguResponse()", value: (8 << 16) },
        { text: "DbguDataChanged()", value: (9 << 16) },
        { text: "DbguCancelResponse()", value: (10 << 16) },
        { text: "DbguScenarioCancel()", value: (11 << 16) },
        { text: "DbguStartDelegation()", value: (12 << 16) },
        { text: "DbguEndDelegation()", value: (13 << 16) },
        { text: "DbguServiceCallback()", value: (14 << 16) },
        { text: "DbguSignal()", value: (15 << 16) },
        { text: "DbguTrace()", value: (16 << 16) },
        { text: "DbguInputTrigger()", value: (17 << 16) },
        { text: "DbguPeripheralStart()", value: (18 << 16) },
        { text: "DbguPeripheralEnd()", value: (19 << 16) },
        { text: "DbguIPC()", value: (32 << 16) },
        { text: "DbguGuiIPC()", value: (33 << 16) },
        { text: "DbguServiceCallGui()", value: (34 << 16) },
        { text: "DbguTraceGui()", value: (35 << 16) },
        { text: "DbguSystemEventGui()", value: (36 << 16) },
        { text: "DbguDriverCallGui()", value: (37 << 16) },
        { text: "DbguDriverCallService()", value: (38 << 16) },
        { text: "DbguDriverCallback()", value: (39 << 16) },
        { text: "DbguScenarioEnd()", value: (40 << 16) },
        { text: "DbguTraceCheckPoint()", value: (41 << 16) },
        { text: "DbguDataLog()", value: ( 42 << 16) },
        { text: "DbguGuiDataLog()", value: (43 << 16) },
        { text: "数値で検索", value:  -1 },
      ],
      currentApitypeParams: null,
      params: null,
    }
  },
  computed: {
    dataAreaHolder () {
      if(this.dataAreaModel == 0)
        return 'Please input string. e.g., ShowMessage'
      else
        return 'Please input hex string (big endian, case-insensitive). e.g, 53686F774D657373616765'
    }
  },

  methods: {
    open() {
			this.dialog = true
    },
    search() {
      let data = {}

      let apitype = null
      if(this.apitypeModel == -1)
        apitype = { text: this.apitypeValue }
      else {
        apitype = this.apitypeItems.filter((e) => {
          return e.value == this.apitypeModel
        })[0]
      }

      console.log(this.apitypeModel)
      console.log(this.apitypeValue)
      console.log(apitype.text)
      if(this.apitypeModel != -2) {
        data.apitype = apitype.text
      }

      let log_format = this.logformatItems.filter((e) => {
        return e.value == this.logformatModel
      })[0]

      if(this.logformatModel != 0)
        data.log_format = log_format.text

      if(this.dataAreaModel == 0)
        data.text = this.dataAreaValue
      else
        data.hexs = this.dataAreaValue

      data.params = this.params

      this.dialog = false
      this.$emit('search', data)
    },

    paramsChange(params) {
      this.params = params
    },

    apitypeChange(value) {
      let apitype = this.apitypeItems.filter((e) => {
        return e.value == value
      })[0]
      console.log(apitype.text.substring(4, apitype.text.length - 2))

      let comp_name = apitype.text.substring(4, apitype.text.length - 2).toLowerCase() + '-params'
      if(Object.prototype.hasOwnProperty.call(this.$options.components, comp_name))
        this.currentApitypeParams = comp_name
      else
        this.currentApitypeParams = null
    }
  },

  components: {
    'servicecall-params': ServiceCallParams,
  }
}

</script>
