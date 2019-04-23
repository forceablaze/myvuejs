<template>
  <div>
    <param-select :items="funcid_items" :label="'funcid'" :dest="'logid'" @changed="onChanged"/>
    <param-select :items="execreq_items" :label="'execreq'" :dest="'part1'" @changed="onChanged"/>
  </div>
</template>

<script>

import ApiTypeBaseParams from '@/components/apitype_params/ApiTypeBaseParams'
import ParamSelectItem from '@/components/apitype_params/ParamSelectItem'

import funcid_items from '@/constants/params/funcid_items'
import execreq_items from '@/constants/params/execreq_items'

export default {
  extends: ApiTypeBaseParams,

  name: 'servicecall-params',
  
  data() {
    return {
      funcid_items: funcid_items,
      execreq_items: execreq_items,
      params: {}
    }
  },
  methods: {
    onChanged(obj) {
      this.params[obj.label] = { name: obj.item.text, dest: obj.dest }
      this.$emit('change', this.params)
    }
  },

  mounted() {
  },

  components: {
    'param-select': ParamSelectItem,
  }
}

</script>
