<template>

  <component
    ref="root"
    v-bind:is="compType"
    :icon="showIcon"
    :flat="!showIcon"
    :title="title"
    :items="items"
    @click="clickHandler"
    :disabled="processing"
    :export="showProgress"
    >
    <template v-if="text">
      <div>{{ text }}</div>
    </template>
    <v-icon v-if="showIcon || !showProgress">
      {{ iconType }}
    </v-icon>

    <v-progress-circular v-if="showProgress"
      :rotate="90"
      :size="35"
      :width="3"
      :value="ratio"
      color="orange"
    >
      {{ ratio }}
    </v-progress-circular>
  </component>

</template>

<script>

import { isFunction } from '@/utils'
import ItemListButton from '@/components/buttons/ItemListButton'

export default {
  name: 'toolbar-component',

  data: () => ({
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
  /** 
   * get_app && processing -> progress 
   * !get_app && processing -> showicon 
   * get_app && !processing -> showicon 
   * !get_app && !processing -> showicon 
  */
    'showProgress' () {
      if(this.$store.state.toolbar.processing && this.iconType == "get_app")
        return true
      return false
    },

    processing () {
      return this.$store.state.toolbar.processing
    },

    ratio () {
      return this.$store.state.toolbar.ratio
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
