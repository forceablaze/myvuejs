<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <v-card>
      <v-card-title>
        <span class="headline">Goto</span>
      </v-card-title>

      <v-layout row align-center>
        <v-flex xs12 sm2>
          <v-subheader>index</v-subheader>
        </v-flex>

        <v-flex xs12 sm10>
          <v-card-text>
            <v-text-field single-line
              label="decimal"
              v-model="logIndex">
            </v-text-field>
          </v-card-text>
        </v-flex>
      </v-layout>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" flat="flat" @click="goto">
          Goto
        </v-btn>
        <v-btn color="green darken-1" flat="flat" @click="close">
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  name: 'goto-log-dialog',

  data () {
    return {
      logIndex: 0
    }
  },

  computed: {
    dialog () {
      return this.$store.state.gotodialog.show
    },
  },

  methods: {
    close() {
      this.$store.dispatch('HIDE_GOTO_DIALOG')
    },
    goto() {
      console.log('goto ' + this.logIndex)
      this.close()
      this.$emit('goto', this.logIndex)
    },
  }
}

</script>
