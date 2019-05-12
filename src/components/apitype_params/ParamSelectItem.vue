<template>
      <v-layout row align-center style="max-height: 50px;">

        <v-flex xs12 sm1>
          <v-checkbox v-model="selected" />
        </v-flex>
        <v-flex xs12 sm2>
          <v-subheader>{{ label }}</v-subheader>
        </v-flex>

        <v-flex xs12 sm9>
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
      model: 0,
      selected: false
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
        if(this.selected)
          this.$emit('changed', { label: this.label, item: item, dest: this.dest })
        else
          this.$emit('changed', { label: this.label })
      }
    }
  },

  watch: {
    'selected' (prop) {
      this.onChanged()
    }
  },

  mounted() {
    this.onChanged()
  }
}
</script>
