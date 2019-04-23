<template>
  <v-dialog v-model="dialog" max-width="500">
    <v-card>
			<v-card-title primary-title class="headline">
				{{ message }}
			</v-card-title>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" flat @click="onClick()">
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
    return {}
  },

  computed: {
    dialog () {
      return this.$store.state.popupmessage.show
    },
    message () {
      return this.$store.state.popupmessage.title
    }
  },

  props: {
    handler: {
      type: Function,
      default: () => {}
    }
  },
  methods: {
    onClick() {
      this.$store.dispatch('HIDE_POPUP_MESSAGE')
      this.handler()
    }
  }
}

</script>
