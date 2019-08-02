<template>
  <v-list-tile
    class='tile'
    avatar
  >

    <v-list-tile-avatar>

      <svg v-if="profile.iconType =='loop'" aria-hidden="true" width="20" height="20" viewBox="0 0 512 512" focusable="false" class="fa-icon fa-spin">
        <path d="M440.6 12.6c0-0.2 0-0.4 0-0.6 0-6.6 5.4-12 12-12h47.4c6.6 0 12 5.4 12 12v200.3c0 6.6-5.4 12-12 12h-200.2c-6.6 0-12-5.4-12-12v-47.4 0c0-6.6 5.4-12 12-12 0.2 0 0.4 0 0.6 0l101.5 4.9c-28.9-42.9-94.3-77.8-146-77.8-76.5 0-153.1 60.3-171 134.7-1.2 5.1-6.4 9.3-11.7 9.3h-49c-6.6 0-12-5.4-12-12 0-0.6 0.1-1.6 0.2-2.2 21.6-114.9 122.4-201.8 243.5-201.8h0.3c63.2 0 147.7 39.1 188.5 87.3zM255.8 432c76.5 0 153.1-60.4 171-134.7 1.2-5.1 6.4-9.3 11.7-9.3h49c6.6 0 12 5.4 12 12 0 0.6-0.1 1.6-0.2 2.2-21.6 114.9-122.4 201.8-243.6 201.8h-0.2c-63.1 0-147.5-39.1-188.4-87.2l4.1 82.6c0 0.2 0 0.4 0 0.6 0 6.6-5.4 12-12 12h0-47.3c-6.6 0-12-5.4-12-12v-200.3c0-6.6 5.4-12 12-12h200.2c6.6 0 12 5.4 12 12v47.4 0c0 6.6-5.4 12-12 12-0.2 0-0.4 0-0.6 0l-101.8-4.9c28.8 42.9 94.1 77.8 145.8 77.8h0.2z"/>
      </svg>

      <v-icon v-else-if="profile.iconType == 'done'"
              color="$props.iconColor">{{ profile.iconType }}</v-icon>

    </v-list-tile-avatar>

    <v-list-tile-content
      class='content'
      @click='onClick'>
      <v-list-tile-title>{{ fileName }}</v-list-tile-title>
      <v-list-tile-sub-title>{{ subtitle }}</v-list-tile-sub-title>
    </v-list-tile-content>

    <v-list-tile-avatar>
      <v-btn icon ripple
        @click='onRefresh'>
        <v-icon color="grey lighten-1" span>refresh</v-icon>
      </v-btn>
    </v-list-tile-avatar>
  </v-list-tile>
</template>

<style scoped>

.tile:hover {
  background: #eee;
}

.content:hover {
  cursor: pointer;
}

.fa-spin {
  animation: fa-spin 1s 0s infinite linear;
}

.fa-icon {
  fill: currentColor;
}


</style>

<script>

import { delay } from '@/utils'
import path from '@/utils/path'

import PeckerMixin from '@/mixins/pecker'

export default {
  name: 'log-profile',

  mixins: [ PeckerMixin ],

  data() {
    return {
    }
  },

  props: ["profile", "iconColor"],

  computed: {
    'fileName' () {
      return path.parse(this.profile.title).name
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

    onRefresh(e) {
      this.startPeckerTask(this.profile.logId)
    }
  },

  mounted() {
  }
}

</script>
