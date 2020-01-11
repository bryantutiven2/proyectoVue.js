<template>
    <section class="page-section cta" >
    <div class="container col-11" id="MAPContanier"  >
      <div class="row">
        <div class="col-xl-4 mx-auto">
          <div class="cta-inner text-center rounded">
            <h2 class="section-heading mb-4">
              <span class="section-heading-upper">Estamos Para </span>
              <span class="section-heading-lower">Ayudarte</span>
            </h2>
            <img class="intro-img img-fluid mb-3 mb-lg-0 rounded" src="./../../assets/img/Combo.png" alt=""> 
          </div>
        </div >
        <div  class="col-xl-8 mx-auto ">
            <Mapa class="map"/>    
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import Mapa from "./Mapa/Mapa.vue";
  
  export default {
    name: "SeccionMapa",
    components: {
      Mapa
    }
  };
</script>
<style lang="scss" scoped>
  .map {
    height: 100%;
    width: 100%;
  }
</style>