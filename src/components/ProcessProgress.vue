<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <v-card>
			<v-card-title primary-title class="headline">
				{{status}}
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
      dialog: false,
    }
  },
  props: {
    status: {
      type: String,
      default: 'Uploading'
    }
  },
  methods: {
    show() {
      this.dialog = true
    },
    hide() {
      this.dialog = false
    }
  }
}

</script>
