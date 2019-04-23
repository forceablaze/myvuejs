<template>
  <v-list-tile
    avatar
    @click='onClick'>

    <v-list-tile-avatar>
      <v-icon color="$props.iconColor">{{ profile.iconType }}</v-icon>
    </v-list-tile-avatar>
    <v-list-tile-content>
      <v-list-tile-title>{{ fileName }}</v-list-tile-title>
      <v-list-tile-sub-title>{{ subtitle }}</v-list-tile-sub-title>
    </v-list-tile-content>

    <v-list-tile-action>
      <v-btn icon ripple>
        <v-icon color="grey lighten-1">arrow_forward</v-icon>
      </v-btn>
    </v-list-tile-action>
  </v-list-tile>
</template>

<script>

import { delay } from '@/utils'
import path from '@/utils/path'

export default {
  name: 'log-profile',

  data() {
    return {
      logPath: {},
      taskStatus: ''
    }
  },

  props: ["profile", "iconColor"],

  computed: {
    'fileName' () {
      return this.logPath.name
    },

    'subtitle' () {
      return this.profile.timestamp + '    size:' + this.profile.file_size + 'B'
    },
  },

  methods: {
    onClick(e) {
      if(this.profile.iconType != 'done')
        e.stopPropagation() 
      else
        this.$emit('click', this.profile.id)
      e.preventDefault()
    },
  },

  mounted() {
    this.logPath = path.parse(this.profile.title)
  }
}

</script>
