<script>

export default {
  
  data() {
    return {}
  },
  method: {
    onParamsChanged() {
      this.$emit('changed', data)
    }
  }
}

</script>
