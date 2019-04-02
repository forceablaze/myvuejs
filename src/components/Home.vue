<template>
  <v-container>
    <h2>
      <a href="http://enosta.osw.olympus.co.jp/svn/ipf3pf-soft/doc/trunk/10_V-Model/10_CP/20_BasicDesign/01_Utility/01_Specification/CV-1500_CP_デバッグログフォーマット仕様書.doc">
        デバッグログの設計書
      </a> 
    </h2>
    <br>
    <h2>
      TLVRecord viewer is not implemented yet.
    </h2>
  </v-container>
</template>

<script>

export default {
  mounted() {

    this.$store.dispatch('UPDATE_TOOLBAR_MENU', {
      'title': 'WoodPecker',
      'menuComponents': [
        { 'type': 'icon', 'iconType': 'info' },
      ]})
  },
}
</script>
