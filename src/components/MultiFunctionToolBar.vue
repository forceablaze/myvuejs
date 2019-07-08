<template>
  <div :style="styleObject">
    <span>
      Hello
    </span>
  </div>

</template>

<script>

export default {
  name: 'multitoolbar',

  data:() => ({
  }),

  computed: {
    computedPaddingLeft() {
      return this.$vuetify.application.left
    },
    computedMarginTop() {
      return this.$vuetify.application.top
    },
    styleObject() {
      return {
        width: '100%',
        height: '64px',
        background: 'red',
        position: 'fixed',
        paddingLeft: `${this.computedPaddingLeft}px`,
        marginTop: `${this.computedMarginTop}px`,
      }
    },
  },
}

</script>
