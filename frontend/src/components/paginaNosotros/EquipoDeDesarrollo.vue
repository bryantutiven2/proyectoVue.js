<template>
    <section class="page-section about-heading">
    <div class="container">
      <div class="about-heading-content">
        <div class="row">
          <div class="col-xl-9 col-lg-10 mx-auto">
            <div class="bg-faded rounded p-5 text-center" >
              <h2 class="section-heading mb-4">
                <span class="section-heading-lower">Equipo de desarrollo</span>
              </h2>
              <div class="row equipoD text-center ">
                <div class="mx-auto my-2 col-lg-5 col-md-2 border border-primary" v-for="(desarrollador, desarrolladorID) in desarrolladores" v-bind:key="desarrolladorID" id="equipoD1">
                  <img class ="contacto" src="./../../assets/img/usuario.png">
                  <p>{{desarrolladorID}}</p>
                  <p>{{desarrollador[0]}}</p>
                  <p>{{desarrollador[1]}}</p>  
                </div>
              </div>  
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
    data(){
        return{
            desarrolladores: {
                'Avilés García Roger' : ['rogiavil@espol.edu.ec','GH: RogerAviles22'],
                'Jimenez Calero Juan' : ['jurajime@espol.edu.ec','GH: juanj97'],
                'lasarang@espol.edu.ec' : ['lasarang@espol.edu.ec','GH: lasarang'],
                'Tutivén Acosta Bryan' : ['brcetuti@espol.edu.ec','GH: bryantutiven2']
            }
        }
    }
}
</script>