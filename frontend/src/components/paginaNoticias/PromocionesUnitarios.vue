<template>
    <div class="container">
    <div class="row ">
      <div class="col-12 mx-1">
        <div class="row text-center promociones">    
            <div :class="'m-5 col-md-2  text-center bg-light'"  v-for="promo in promocionesL" :key='promo.id'>
                <img :class="'img-fluid textpromo'+promo.id+' my-1'" v-bind:src="'/img/' +promo.url+'.jpg'"/>
                <h6 :class="'promo'+promo.id">{{promo.descripcion}}</h6>
            </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import promocion from '../../../public/json/promociones.json'
export default {
    data(){
      return{
          promocionesL: promocion.promociones
      }
    }
    ,/*
    created(){
      this.listarPromociones();
    },*/
    methods:{
      /*getImgUrl(pet) {
        return require('@/static/'+pet+'.jpg')
      }*/
    }
}
</script>

<style scoped>
    
    
</style>