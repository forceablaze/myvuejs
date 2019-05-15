<template>

  <component
    ref="root"
    v-bind:is="compType"
    :icon="showIcon"
    :flat="!showIcon"
    :title="title"
    :items="items"
    @click="clickHandler"
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
import ItemListButton from '@/components/buttons/ItemListBUtton'

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
    clickHandler(data) {
      if(isFunction(this.handler))
        this.handler(data)
    },
  },

  computed: {
    'showIcon' () {
      if(this.type == "icon")
        return true
      return false
    },

    compType () {
      if(this.$store.state.toolbar.menuComponents[this.index].compType === undefined)
        return 'v-btn'
      return this.$store.state.toolbar.menuComponents[this.index].compType
    },

    title () {
      return this.$store.state.toolbar.menuComponents[this.index].title
    },

    items () {
      return this.$store.state.toolbar.menuComponents[this.index].items
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
    //this.$el.addEventListener('click', this.clickHandler)
  },

  beforeDestroy() {
    //this.$el.removeEventListener('click', this.clickHandler)
  },

  components: {
    'itemlistbutton': ItemListButton,
  }
}

</script>
