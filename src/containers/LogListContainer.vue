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

  mounted() {
    if(this.$route.name == 'log_list')
        this.refreshToolBar()
  },

  methods: {
    refreshToolBar() {
      this.$store.dispatch('UPDATE_TOOLBAR_MENU', {
        'title': 'Uploaded Log',
        'menuComponents': [
          { 'type': 'icon', 'iconType': 'search' },
          { 'type': 'icon', 'iconType': 'refresh' },
        ]})
    },
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
      if(to.name == 'log_list')
        this.refreshToolBar()
    }
  },
}

</script>
