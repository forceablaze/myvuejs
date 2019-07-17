<template>
  <v-container>
    <v-layout column>
      <v-flex>
        <router-view></router-view>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<style scoped>

.container {
  max-width: 100%;
  padding:0px;
}

</style>



<script>

export default {
  data() {
    return {
      profiles: [],
      count: 0,
      loading: true,
    }
  },

  mounted() {
  },

  methods: {
    add() {
      this.count++
      this.profiles.push({
        id: this.count,
        title: 'Title' + this.count,
        subtitle: 'subtitle' + this.count
      })
    },
    handleResize() {
      console.log('size changed')
      window.scrollTo(0, document.body.scrollHeight)
    }
  },
  ready: function () {
    window.addEventListener('resize', this.handleResize)
  },

  beforeDestroy: function () {
    window.removeEventListener('resize', this.handleResize)
    this.profiles = null
  },


  watch: {
    '$route' (to, from) {
    }
  },
}

</script>
