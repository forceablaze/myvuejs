<template>
  <div class='resizers' :style="styleObject">
    <div v-show="left" class='left-resizer'/>
    <div v-show="right" class='right-resizer'/>
    <div v-show="top" class='top-resizer'/>
    <div v-show="bottom" class='bottom-resizer'/>
    <slot>No content.</slot>
  </div>
</template>

<style>

.resizers, resizer{
  box-sizing: border-box;
  background-color: white;
}

.resizers .left-resizer{
  left: 0px;
  top: 0px;
  bottom: 0px;
  cursor: w-resize;
  position: absolute;
  border-left: 4px solid #aaa;
}

.resizers .top-resizer{
  top: 0px;
  left: 0px;
  right: 0px;
  cursor: n-resize;
  position: absolute;
  border-top: 4px solid #aaa;
}

.resizers .right-resizer{
  right: 0px;
  top: 0px;
  bottom: 0px;
  cursor: e-resize;
  position: absolute;
  border-right: 4px solid #aaa;
}

.resizers .bottom-resizer{
  bottom: 0px;
  left: 0px;
  right: 0px;
  cursor: s-resize;
  position: absolute;
  border-bottom: 4px solid #aaa;
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

  props: {
    defaultHeight: Number,
    defaultWidth: Number,
    minHeight: Number,
    minWidth: Number,
    vertical: Boolean,
    horizontal: Boolean,

    top: { type: Boolean },
    bottom: { type: Boolean },
    right: { type: Boolean },
    left: { type: Boolean },
  },

  computed: {
    styleObject () {
      let obj = {}

      if(this.horizontal)
        obj.width = `${this.width}` + 'px'
      else
        obj.width = `${this.defaultWidth}` + 'px'

      if(this.vertical)
        obj.height = `${this.height}` + 'px'
      else
        obj.height = `${this.defaultHeight}` + 'px'

      return obj
    },
    resizers () {
      return this.$el
    },

    topResizer() {
      return this.$el.querySelector('.top-resizer')
    },
    bottomResizer() {
      return this.$el.querySelector('.bottom-resizer')
    },
    leftResizer() {
      return this.$el.querySelector('.left-resizer')
    },
    rightResizer() {
      return this.$el.querySelector('.right-resizer')
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


      let newHeight = this.originHeight + diffMouseY
      if(newHeight < this.minHeight)
        newHeight = this.minHeight

      let newWidth = this.originWidth + diffMouseX
      if(newWidth < this.minWidth)
        newWidth = this.minWidth

      this.height = newHeight
      this.width = newWidth

      this.$emit('resize', {
        height: this.height,
        width: this.width
      })
    },
    stopResize(e) {
      window.removeEventListener('mousemove', this.resize)
    },

    setupResizer() {
      if(this.top)
        this.topResizer.addEventListener('mousedown', this.mouseDown)

      if(this.left)
        this.leftResizer.addEventListener('mousedown', this.mouseDown)

      if(this.right)
        this.rightResizer.addEventListener('mousedown', this.mouseDown)

      if(this.bottom)
        this.bottomResizer.addEventListener('mousedown', this.mouseDown)
    },

    releaseResizer() {
      if(this.top)
        this.topResizer.removeEventListener('mousedown', this.mouseDown)

      if(this.left)
        this.leftResizer.removeEventListener('mousedown', this.mouseDown)

      if(this.right)
        this.rightResizer.removeEventListener('mousedown', this.mouseDown)

      if(this.bottom)
        this.bottomResizer.removeEventListener('mousedown', this.mouseDown)
    }
  },

  mounted() {
    this.setupResizer()

    this.height = this.defaultHeight
    this.width = this.defaultWidth


    this.$emit('resize', {
      height: this.height,
      width: this.width
    })
  },

  beforeDestroy() {
    this.releaseResizer()
  },

}
</script>
