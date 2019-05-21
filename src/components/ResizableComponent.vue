<template>
  <div class='resizers' :style="styleObject">
    <slot>No content.</slot>
  </div>
</template>

<style>

.resizers, resizer{
  box-sizing: border-box;
  bottom: 0px;
  right: 0px;
  background-color: white;
  border-left: 4px solid #DDDDDD;
}

.resizers::after{
  content: " ";
  width: 4px;
  height: 100%;
  left: 0px;
  top: 0px;
  cursor: w-resize;
  position: absolute;
  background-color: transparent;
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
        width: `${this.width}` + 'px'
      }
    },
    resizers () {
      return this.$el
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
    this.$el.addEventListener('mousedown', this.mouseDown)

    this.height = this.defaultHeight
    this.width = this.defaultWidth
  },

  beforeDestroy() {
    this.$el.removeEventListener('mousedown', this.mouseDown)
  },

}
</script>
