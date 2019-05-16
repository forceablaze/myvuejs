<template>

  <v-menu offset-y>
    <template v-slot:activator="{ on }">
      <v-btn
        color="primary"
        dark
        v-on="on"
        :style="{ fontSize: fontSize + 'px', height: height + 'px' }"
      >
        {{ title }}
      </v-btn>
    </template>
    <v-list style="max-height: 450px; z: 1;">
      <v-list-tile
        v-for="(item, index) in items"
        :key="index"
        @click="click(index)"
      >
        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<style scoped>
*[role="listitem"] {
  background-color: white;
  /* style these a buttons w/o relying on a .button class */
}
</style>

<script>

export default {
  name: 'itemlistbutton',
  data() {
    return {
    }
  },

  props: ['title', 'items', 'fontSize', 'height'],

  methods: {
    click(index) {
      let data = this.items[index]['title']
      this.$emit('click', data)
    }
  },
  mounted() {
  }
}

</script>
