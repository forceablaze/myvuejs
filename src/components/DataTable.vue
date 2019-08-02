<template>
  <div>
    <div id="table_overflow" class="table__overflow" :style="overflowStyle">
      <table class="table__container">
        <thead>
          <tr>
            <th v-for="(header, index) in headers"
             >
             {{ header.value }}
            </th>
          </tr>
        </thead>
        <tbody>
          <slot name="item">No items</slot>
        </tbody>
      </table>
    </div>
  </div>

</template>

<style scoped>

.table__container {
  border-radius: 2px;
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
}

.table__container thead th {
  top: 0;
  position: sticky;
  background:#eee; 
  text-align: left;
  padding-right: 20px;
  padding-left: 20px;
}

</style>

<script>

export default {
  name: 'datatable',

  props: {
    headers: {
      type: Array,
      default: () => []
    },

    items: {
      type: Array,
      default: () => []
    },

    itemKey: {
      type: String,
      default: 'id'
    }
  },

  data() {
    return {
    }
  },

  computed: {
    overflowStyle() {
      return {
        width: `${this.dataTableWidth}px`,
        height: `${this.dataTableHeight}px`,
        overflowX: 'hidden',
        overflowY: 'auto',

        transition: "width .1s cubic-bezier(.4,0,.2,1)",
      }
    },

    /* please override me */
    dataTableHeight() {
      return 300
    },

    /* please override me */
    dataTableWidth() {
      return 300
    }
  }
}

</script>
