<template>
  <v-dialog v-model="dialog" persistent max-width="800">
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

      <v-layout row align-center v-if="advanceSearch">
        <v-flex xs12 sm2>
        </v-flex>
        <v-flex xs12 sm10>
          <v-card-text>
            <component @change="paramsChange" v-if="currentApitypeParams" :is="currentApitypeParams"/>
          </v-card-text>
        </v-flex>
      </v-layout>

      <v-layout row align-center v-if="advanceSearch">
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

      <v-layout row align-center v-else>
        <v-flex xs12 sm2>
          <v-subheader>formatted text</v-subheader>
        </v-flex>

        <v-flex xs12 sm10>
          <v-card-text>
            <multitext-combobox @change="formattedTextChange"/>
          </v-card-text>
        </v-flex>
      </v-layout>


      <v-card-actions>
        <v-switch v-model="advanceSearch" label="advance" />
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" flat="flat" @click="search">
          Search
        </v-btn>
        <v-btn color="green darken-1" flat="flat" @click="close">
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

import ServiceCallParams from '@/components/apitype_params/ServiceCallParams.vue'
import MultiTextCombobox from '@/components/MultiTextCombobox.vue'

import apitypes from '@/constants/apitypes'

export default {
  name: 'search-dialog',

  data () {
    return {
      advanceSearch: false,
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
      apitypeItems: apitypes,
      currentApitypeParams: null,
      params: null,
      formattedTextModel: null
    }
  },
  computed: {
    dialog () {
      return this.$store.state.searchdialog.show
    },

    dataAreaHolder () {
      if(this.dataAreaModel == 0)
        return 'Please input string. e.g., ShowMessage'
      else
        return 'Please input hex string (big endian, case-insensitive). e.g, 53686F774D657373616765'
    }
  },

  methods: {
    close() {
      this.$store.dispatch('HIDE_SEARCH_DIALOG')
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

      if(!this.advanceSearch) {
        data.formatted_texts = this.formattedTextModel
      }

      this.$store.dispatch('HIDE_SEARCH_DIALOG')
      this.$emit('search', data)
    },

    paramsChange(params) {
      console.log(this.params)
      this.params = params
    },

    formattedTextChange(model) {
      this.formattedTextModel = model.map(v => {
        return { text: v.text }
      })
    },

    apitypeChange(value) {
      let apitype = this.apitypeItems.filter((e) => {
        return e.value == value
      })[0]

      if(apitype === undefined) {
        this.currentApitypeParams = null
        return
      }

      let comp_name = apitype.text.substring(4, apitype.text.length - 2).toLowerCase() + '-params'
      if(Object.prototype.hasOwnProperty.call(this.$options.components, comp_name))
        this.currentApitypeParams = comp_name
      else
        this.currentApitypeParams = null
    }
  },

  components: {
    'servicecall-params': ServiceCallParams,
    'multitext-combobox': MultiTextCombobox,
  }
}

</script>
