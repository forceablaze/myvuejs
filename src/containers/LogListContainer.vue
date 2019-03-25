<template>
  <v-container>
    <v-layout column>
      <v-flex>
        <v-list two-line subheader>
          <log-profile v-for="(profile, index) in profiles"
            :profile="profile"
            :key="index"
            @click="onProfileClick"></log-profile>
        </v-list>
      </v-flex>
    </v-layout>
  </v-container>
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
