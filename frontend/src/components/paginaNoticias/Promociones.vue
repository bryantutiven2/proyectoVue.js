<template>
	<div class="oferta " id='outer'>
    <agile >
      <div class="slide" v-for="promoP in productosL" :key='promoP.id' >
        <img v-bind:src="'/img/' +promoP.url+'.png'" style="width:100%"/>
      </div>
    </agile>
  </div>
</template>

<script>
import { VueAgile } from 'vue-agile'
import product from '../../../public/json/promoProducto.json'
export default {
  data(){
    return{
      productosL: product.promoProducto
    }
  },
	components: {
    agile: VueAgile
  }
}
</script>
<style scoped>
   #outer {
    margin: 0 auto;
    width: 800px;
}
</style>