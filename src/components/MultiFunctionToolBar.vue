<template>
  <div :style="styleObject">
    <v-layout row fill-height :style="layoutStyle">

      <v-flex sm2>
        <v-autocomplete
          v-on:keyup.enter="search"
          style="padding: 12px 12px 0px;"
          :items="apitypeItems"
          v-model="apitypeModel"
          label="API Type"
          @change="apitypeChange"
        />
      </v-flex>

      <v-flex sm6>
        <multitext-combobox class="combotext"
          @enter="search"
          @change="formattedTextChange"/>
      </v-flex>

      <v-spacer></v-spacer>

      <v-btn icon @click.stop="filterButtonClick">
        <v-icon large >filter_list</v-icon>
      </v-btn>
    </v-layout>
  </div>

</template>

<style>

.v-text-field > .v-input__control > .v-input__slot::after, .v-text-field > .v-input__control > .v-input__slot::before {
    visibility: hidden;
}

.combotext .v-messages {
  flex: 1 1 auto;
  font-size: 12px;
  min-height: 0px;
  min-width: 0px;
  position: relative;
}

.combotext .v-input__control .v-text-field__details {
  margin-bottom: 0px;
}

.combotext .v-input__slot {
  margin-bottom: 0px;
}

</style>

<script>


import MultiTextCombobox from '@/components/MultiTextCombobox.vue'
import apitypes from '@/constants/apitypes'

export default {
  name: 'multitoolbar',

  data:() => ({
      apitypeModel: -2,
      apitypeValue: 0,
      apitypeItems: apitypes,
      layoutStyle: {
        alignItems: "center",
      },

      currentApitypeParams: null,
      formattedTextModel: null,
      params: null,
  }),

  computed: {
    computedPaddingLeft() {
      return this.$vuetify.application.left
    },
    computedMarginTop() {
      return this.$vuetify.application.top
    },
    styleObject() {
      return {
        width: '100%',
        height: '64px',
        background: '#FFFFFF',
        position: 'fixed',
        paddingRight: `${this.computedPaddingLeft}px`,
        transition: "padding .2s cubic-bezier(.4,0,.2,1)",
        borderBottom: "1px solid #ccc",
        zIndex: '2',
      }
    },
  },

  methods: {
    filterButtonClick() {
      this.$store.dispatch('TRIGGER_SEARCH_CONTAINER')
    },

    formattedTextChange(model) {
      this.formattedTextModel = model.map(v => {
        return { text: v.text }
      })

      //this.search()
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
    },

    search() {
      console.log('search')
      let data = {}

      let apitype = null

      apitype = this.apitypeItems.filter((e) => {
        return e.value == this.apitypeModel
      })[0]

      console.log(this.apitypeModel)
      console.log(this.apitypeValue)
      console.log(apitype.text)

      /* if ALL is not selected */
      if(this.apitypeModel != -2) {
        data.apitype = apitype.text
      }

      data.params = this.params
      data.formatted_texts = this.formattedTextModel

      console.log(data)
      this.$emit('search', data)
    },
  },

  components: {
    'multitext-combobox': MultiTextCombobox,
  }
}

</script>
