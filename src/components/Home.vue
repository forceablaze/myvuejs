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
        { 'type': 'icon', 'iconType': 'info', 'handler':
          () => {

            window.open("http://10.156.2.84/c/redmine/projects/integ/wiki/%E3%83%AD%E3%82%B0%E8%A7%A3%E6%9E%90%E6%94%AF%E6%8F%B4%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E4%BB%95%E6%A7%98")
            /*
            window.open("/#/log","windowName",
              "height=300,width=800,toolbar=no,menubar=no,status=no,location=no");
            */
          }
        },
      ]})
  },
}
</script>
