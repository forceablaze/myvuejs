<template>
  <v-list-tile
    avatar
    @click='onClick'>

    <v-list-tile-avatar>
      <v-icon :class="['grey lighten-1 white--text']">done</v-icon>
    </v-list-tile-avatar>
    <v-list-tile-content>
      <v-list-tile-title>{{ profile.title }}</v-list-tile-title>
      <v-list-tile-sub-title>{{ profile.subtitle }}</v-list-tile-sub-title>
    </v-list-tile-content>

    <v-list-tile-action>
      <v-btn icon ripple>
        <v-icon color="grey lighten-1">arrow_forward</v-icon>
      </v-btn>
    </v-list-tile-action>
  </v-list-tile>
</template>

<script>
export default {
  name: 'log-profile',
  props: ["profile"],

  methods: {
    onClick(e) {
      this.$emit('click', this.profile.id)
      e.preventDefault()
    }
  }
}

</script>
