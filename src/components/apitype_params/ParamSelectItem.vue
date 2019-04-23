<template>
      <v-layout row align-center style="max-height: 50px;">
        <v-flex xs12 sm2>
          <v-subheader>{{ label }}</v-subheader>
        </v-flex>

        <v-flex xs12 sm10>
          <v-card-text>
            <v-autocomplete
              :items="items"
              v-model="model"
              @change="onChanged"
            ></v-autocomplete>
          </v-card-text>
        </v-flex>
      </v-layout>
</template>

<script>

export default {
  name: 'param-select',

  data() {
    return {
      model: 0
    }
  },

  props: ['items', 'label', 'dest'],

  methods: {
    onChanged() {
      let filtered = this.items.filter((e) => {
        return e.value == this.model
      })
      if(filtered !== undefined) {
        let item = filtered[0]
        this.$emit('changed', { label: this.label, item: item, dest: this.dest })
      }
    }
  },

  mounted() {
    this.onChanged()
  }
}
</script>
