<template>
  <v-layout column>
    <v-flex>
    <div id="hexview"
      v-for="(row, index) in tuples"
      :key="index"
    >

  <v-layout row>
    <v-flex d-flex xs1>
      <v-card>
        <v-card-text>
          {{ row.addr }}
        </v-card-text>
      </v-card>
    </v-flex>
    <v-flex d-flex xs8>
      <v-card>
        <v-card-text
          style="white-space: pre-wrap; word-wrap: break-word;"
        >{{ row.hexs }}</v-card-text>
      </v-card>
    </v-flex>
    <v-flex d-flex>
      <v-card>
        <v-card-text
          style="white-space: pre-wrap; word-wrap: break-word;"
        >{{ row.chars }}</v-card-text>
      </v-card>
    </v-flex>
  </v-layout>

    </div>
    </v-flex>

  </v-layout>
</template>

<style scoped>
.v-card__text {
  padding: 0px;
  font-size: 24px;
}

#hexview {
  font-family: monospace;
}

</style>


<script>
export default {
  name: 'hex-viewer-component',

  data() {
    return {
      tuples: []
    }
  },

  props: ['hexs'],

  watch: {
    'hexs' (to, from) {
      this.calc()
    },
  },

  methods: {
    calc() {

      this.tuples = null

      let tuples = []

      let addr = 0
      let eachRowCount = 4
      let eachElementSize = 4
      let nextAddr = eachRowCount * eachElementSize
    
      for(let i = 0; i < this.hexs.length; i += nextAddr * 2) {
        let obj = {}
        obj.addr = addr.toString(16).padStart(8, '0')
        let _str = this.hexs.substring(i, i + (nextAddr * 2))

        let hexs = ''
        let chars = ''

        for(let j = 0; j < _str.length; j++) {
          hexs += _str[j].toUpperCase()

          if(j & 1) {
            let charCode = parseInt(_str.substr(j - 1, 2), 16)
            if(charCode >= 0x20 && charCode <= 0x7e) {
              chars += String.fromCharCode(charCode)
            }
            else
              chars += '?'
          }

          if((j + 1) % 8 == 0) {
            hexs += ' '
            chars += ' '
          }
        }
        obj.hexs = hexs
        obj.chars = chars

        addr += nextAddr

        tuples.push(obj)
      }

      this.tuples = tuples
    },
  },

  mounted() {
    this.calc()
  },

  computed: {
  }
}

</script>
