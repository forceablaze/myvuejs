<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <v-card>
			<v-card-title primary-title class="headline">
				{{title}}
		  	<v-progress-linear :indeterminate="true"></v-progress-linear>
			</v-card-title>
		</v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'process-progress',
  data () {
    return {
    }
  },
  props: {
  },
  computed: {
    dialog () {
      return this.$store.state.progress.show
    },
    title () {
      return this.$store.state.progress.title
    }
  },

  methods: {
  }
}

</script>
