<template>
  <v-dialog v-model="dialog" max-width="500">
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
        <v-btn color="green darken-1" flat="flat" @click="dialog = false">
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
      dialog: false,
      logIndex: 0
    }
  },
  methods: {
    open() {
			this.dialog = true
    },
    goto() {
      console.log('goto ' + this.logIndex)
      this.dialog = false
      this.$emit('goto', this.logIndex)
    },
  }
}

</script>
