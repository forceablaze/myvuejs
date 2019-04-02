<template>
  <v-dialog v-model="dialog" max-width="500">
    <v-card>
			<v-card-title primary-title class="headline">
				{{ message }}
			</v-card-title>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" flat @click="dialog = false">
          OK
        </v-btn>
      </v-card-actions>
		</v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'popup-messagebox',
  data () {
    return {
      dialog: false,
    }
  },
  props: {
    message: {
      type: String,
      default: 'Message'
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
