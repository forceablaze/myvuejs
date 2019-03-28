<template>
  <v-container>
    <v-layout column>
      <v-flex>
        <router-view></router-view>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
  data() {
    return {
      profiles: [],
      count: 0,
      loading: true,
    }
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
  },

  watch: {
    '$route' (to, from) {
      console.log(to)
      console.log(from)
    }
  },

  mounted() {
  },
}

</script>
