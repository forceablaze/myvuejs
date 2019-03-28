<template>
  <v-list two-line subheader>
    <log-profile v-for="(profile, index) in profiles"
      :profile="profile"
      :key="index"
      @click="onProfileClick"></log-profile>
  </v-list>
</template>

<script>

import LogProfile from '@/components/LogProfile'

export default {
  data() {
    return {
      profiles: [],
      count: 0,
      loading: true,
      profileObjs: {}
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
    onProfileClick(id) {
      console.log(id)
      this.$router.push({ name: 'log_view', params: { log_id: id }})
    }
  },

  watch: {
    profileObjs: function(newProfiles) {

      if(newProfiles === undefined)
        return

      newProfiles.forEach((profile) => {
        this.profiles.push({
          id: profile.id,
          title: profile.file,
          subtitle: profile.timestamp
        })
      })
    },

    '$route' (to, from) {
      console.log(to)
      console.log(from)
    }
  },

  mounted() {
    this.axios.get('/file/')
    .then(response => {
      // Automatic transforms for JSON data
      this.profileObjs = response.data
    })
    .catch(error => {
      console.log(error)
    });
  },

  components: {
    LogProfile
  }
}

</script>
