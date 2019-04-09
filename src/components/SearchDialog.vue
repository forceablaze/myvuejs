<template>
  <v-dialog v-model="dialog" max-width="800">
    <v-card>
      <v-card-title>
        <span class="headline">Search/Filter</span>
      </v-card-title>

      <v-layout row align-center>
        <v-flex xs12 sm2>
          <v-subheader>apitype</v-subheader>
        </v-flex>

        <v-flex xs12 sm5>
          <v-card-text>
            <v-select
              :items="apitypeItems"
              v-model="apitypeModel"
              label="log format"
              @change="apitypeChange"
            ></v-select>
          </v-card-text>
        </v-flex>

        <v-flex v-if="apitypeModel == -1" xs12 sm5>
          <v-text-field single-line
            label="decimal"
            v-model="apitypeValue"></v-text-field>
        </v-flex>
      </v-layout>

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
      apitypeModel: -1,
      apitypeValue: 0,
      apitypeItems: [
        { text: "Dbgl API direct", value: 0 },
        { text: "API種別APP用ベース値", value: 65536 },
        { text: "API種別PF用ベース値", value: 41943294 },
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
      ]
    }
  },
  methods: {
    open() {
			this.dialog = true
    },
    search() {
      let apitype = null
      if(this.apitypeModel == -1)
        apitype = this.apitypeValue
      else
        apitype = this.apitypeModel
      console.log(apitype)
      console.log(this.logformatModel)
      console.log(this.dataAreaValue)
    },
    upload() {
    },
    pickFile() {
      this.$refs.file.click()
    },
    onFilePicked(e) {
    },
    apitypeChange(value) {
    }
  }
}

</script>
