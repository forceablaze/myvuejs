<template>

  <resizable class="sidebar-bottom"
    vertical
    top
    :defaultHeight="defaultHeight"
    :minHeight="32"
    @resize="resize"
  >
    <v-layout style="padding-top: 4px">
      <v-flex grow  style="background-color: #DDDDDD;">
        <span style="font-size: 20px;">Log Information</span>
      </v-flex>
    </v-layout>

    <slot>No content.</slot>

  </resizable>

</template>

<style>

.sidebar-bottom {
  position: fixed;
  margin-top: 0px;
  padding-bottom: 0px;
  bottom: 0px;
  width: 100%;
  z-index: 3;
}

</style>


<script>

import ResizableComponent from '@/components/ResizableComponent'

import { mapState } from 'vuex'

export default {

  name: 'bottomview',

  data() {
    return {
    }
  },

  props: ['defaultHeight'],

  methods: {
    resize(dim) {
      this.$wood.logViewContainer.bottomViewHeight = dim.height
    }
  },

  computed: mapState({

  }),

  mounted() {
  },

  created() {
  },

  beforeDestroy() {
  },

  components: {
    'resizable': ResizableComponent,
  }
}
</script>
