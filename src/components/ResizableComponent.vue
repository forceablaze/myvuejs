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
  right: 0px;
  background-color: white;
  border-left: 2px solid #DDDDDD;
}

.resizer.top-center{
  border-radius: 50%;
  width: 10px;
  height: 10px;
  left: 0px;
  top: 50%;
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
      'width': 0,
      'mouseY': 0,
      'mouseX': 0,
      'originHeight': 0,
      'originWidth': 0
    }
  },

  props: ['defaultHeight', 'defaultWidth'],

  computed: {
    styleObject () {
      return {
        height: '100%',
        width: `${this.width}` + 'px'
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
      this.mouseX = e.pageX
      this.originHeight = this.height
      this.originWidth = this.width

      window.addEventListener('mousemove', this.resize)
      window.addEventListener('mouseup', this.stopResize)
    },

    resize(e) {

      const diffMouseY = this.mouseY - e.pageY
      const originY = this.resizers.clientHeight + this.resizers.clientTop * 2

      const diffMouseX = this.mouseX - e.pageX
      const originX = this.resizers.clientWidth

      this.height = this.originHeight + diffMouseY
      this.width = this.originWidth + diffMouseX
    },
    stopResize(e) {
      window.removeEventListener('mousemove', this.resize)
    }
  },

  mounted() {
    const topCenterResizer = this.$el.querySelector('.resizer.top-center')
    topCenterResizer.addEventListener('mousedown', this.mouseDown)

    this.height = this.defaultHeight
    this.width = this.defaultWidth
  },

  beforeDestroy() {
    const topCenterResizer = this.$el.querySelector('.resizer.top-center')
    topCenterResizer.removeEventListener('mousedown', this.mouseDown)
  },

}
</script>
