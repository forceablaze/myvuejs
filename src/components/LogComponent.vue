<template>
  <v-expansion-panel-content>
    <template v-slot:header>
      <div>{{ 'Index: ' + log.index + '    position: 0x' + log.position }}</div>
    </template>

    <v-layout row wrap><v-flex xs6>raw</v-flex><v-flex xs6><v-switch></v-switch></v-flex></v-layout>
    <v-layout row>

    <v-layout column>

    <v-layout row>
      <v-flex xs12 d-flex>
        <v-card dark tile flat color="red darken-2">
          <v-card-text>{{ log.index }}</v-card-text>
        </v-card>
        <v-card dark tile flat color="deep-orange lighten-1">
          <v-card-text>{{ log.position }}</v-card-text>
        </v-card>
        <v-card dark tile flat color="deep-orange darken-3">
          <v-card-text>{{ log.time }}</v-card-text>
        </v-card>
        <v-card dark tile flat color="deep-orange">
          <v-card-text>{{ log.logtype }}</v-card-text>
        </v-card>
        <v-card dark tile flat color="deep-orange darken-3">
          <v-card-text>{{ log.loglevel }}</v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout row>
      <v-flex xs12 d-flex>
        <v-card dark tile flat color="red lighten-1">
          <v-card-text>{{ log.apitype }}</v-card-text>
        </v-card>
        <v-card dark tile flat color="red lighten-2">
          <v-card-text>{{ log.logid }}</v-card-text>
        </v-card>
        <v-card dark tile flat color="red darken-1">
          <v-card-text>{{ log.usage }}</v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout row>
      <v-flex xs12 d-flex>
        <v-card dark tile flat color="red lighten-1">
          <v-card-text>{{ log.own_domain + '/' + log.own_subsys }}</v-card-text>
        </v-card>
        <v-card dark tile flat color="red lighten-2">
          <v-card-text style="max-width: 100%; word-wrap: break-word;">
            {{ log.dest_domain + '/' + log.dest_subsys }}
          </v-card-text>
        </v-card>
        <v-card dark tile flat color="red darken-1">
          <v-card-text>{{ log.task_domain + '/' + log.task_subsys }}</v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-card>
      <v-card-text>
        {{ log.text }}
      </v-card-text>
    </v-card>

    </v-layout>

    <v-flex d-flex xs12 sm6 md3>
      <v-layout row wrap>
        <v-flex>
          <v-card color="red lighten-2" dark>
            <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.flag }}</v-card-text>
          </v-card>
          <v-card color="red lighten-2" dark>
            <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.dest }}</v-card-text>
          </v-card>
          <v-card color="red lighten-2" dark>
            <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.format }}</v-card-text>
          </v-card>
          <v-card color="red lighten-2" dark>
            <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.direction }}</v-card-text>
          </v-card>
          <v-card color="red lighten-2" dark>
            <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.cputype }}</v-card-text>
          </v-card>
          <v-card color="red lighten-2" dark>
            <v-card-text style="max-width: 100%; word-wrap: break-word;">{{ log.seq }}</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>


    </v-layout>

  </v-expansion-panel-content>

</template>

<script>
export default {
  name: 'log-component',

  props: ['log']
}

</script>
