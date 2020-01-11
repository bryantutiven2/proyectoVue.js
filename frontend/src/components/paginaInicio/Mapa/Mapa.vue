<template>
  <CargarMapa
    :configMapa="configMapa"
    apiKey="AIzaSyBiIT9xDY3rV5CzwleLuebQseYLHjxZMjU"
  >
 
    <template slot-scope="{ google, map }">
      <Marcadores
        v-for="marker in markers"
        :key="marker.id"
        :marker="marker"
        :google="google"
        :map="map"
      />
    </template>
 
  </CargarMapa>
 
</template>
 
<script>
  import CargarMapa from "./CargarMapa.vue";
  import Marcadores from "./Marcadores.vue";
  import { configMapa } from "@/constants/configMapa.js";
 
  export default {
    components: {
      CargarMapa,
      Marcadores
    },
 
    data() {
      return {
        markers: [
          {
            id: "0",
            position: { lat: -2.131496, lng: -79.939364 },
            title: "Ecuador"
          }
        ]
      };
    },
 
    computed: {
      configMapa() {
        return {
          ...configMapa,
          center: this.mapCenter
        };
      },
 
      mapCenter() {
        return this.markers[0].position;
      }
    }
  };
  
</script>