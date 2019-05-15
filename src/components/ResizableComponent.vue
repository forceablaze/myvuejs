<template>
    
  <div class='resizable'>
    <div class='resizers' :style="styleObject">
      <div class='resizer top-center'></div>
      <slot>No content.</slot>
    </div>
  </div>

</template>

<style>

.resizable .resizers, resizer{
  position: absolute;
  width: 100%;
  box-sizing: border-box;
  bottom: 0px;
  background-color: inherit;
}

.resizer.top-center{
  border-radius: 50%;
  width: 10px;
  height: 10px;
  left: 50%;
  top: 0;
  cursor: n-resize;
  position: relative;
  box-sizing: border-box;
	border: 3px solid #4286f4;
}

</style>


<script>
export default {
  name: 'resizable',

  data() {
    return {
      'height': 0,
      'mouseY': 0,
      'originHeight': 0
    }
  },

  props: ['defaultHeight'],

  computed: {
    styleObject () {
      return {
        height: `${this.height}px`
      }
    },
    resizers () {
      return this.$el.querySelector('.resizers')
    },
  },

  methods: {
    mouseDown(e) {
      e.preventDefault()
      this.mouseY = e.pageY
      this.originHeight = this.height

      window.addEventListener('mousemove', this.resize)
      window.addEventListener('mouseup', this.stopResize)
    },

    resize(e) {

      const diffMouseY = this.mouseY - e.pageY
      const originY = this.resizers.clientHeight + this.resizers.clientTop * 2
      this.height = this.originHeight + diffMouseY
    },
    stopResize(e) {
      window.removeEventListener('mousemove', this.resize)
    }
  },

  mounted() {
    const topCenterResizer = this.$el.querySelector('.resizer.top-center')
    topCenterResizer.addEventListener('mousedown', this.mouseDown)

    if(this.defaultHeight === undefined)
      this.height = 300
    else
      this.height = this.defaultHeight
  },

  beforeDestroy() {
    const topCenterResizer = this.$el.querySelector('.resizer.top-center')
    topCenterResizer.removeEventListener('mousedown', this.mouseDown)
  },

}
</script>
