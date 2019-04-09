<template>

  <component
    ref="root"
    v-bind:is="componentType"
    :icon="showIcon"
    :flat="!showIcon"
    >
    <template v-if="text">
      <div>{{ text }}</div>
    </template>
    <v-icon v-if="showIcon">
      {{ iconType }}
    </v-icon>
  </component>

</template>

<script>

import { isFunction } from '@/utils'

export default {
  name: 'toolbar-component',

  data: () => ({
    componentType: 'v-btn',
  }),

  props: {
    index: Number,
    handler: Function,
  },

  methods: {
    clickHandler() {
      if(isFunction(this.handler))
        this.handler()
    }
  },

  computed: {
    'showIcon' () {
      if(this.type == "icon")
        return true
      return false
    },

    type () {
      return this.$store.state.toolbar.menuComponents[this.index].type
    },

    iconType () {
      return this.$store.state.toolbar.menuComponents[this.index].iconType
    },

    text () {
      return this.$store.state.toolbar.menuComponents[this.index].text
    }
  },

  mounted() {
    this.$el.addEventListener('click', this.clickHandler)
  },

  beforeDestroy() {
    this.$el.removeEventListener('click', this.clickHandler)
  }
}

</script>
