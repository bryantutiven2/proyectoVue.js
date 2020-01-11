<template>
    <div class="container">
      <div class="intro">
        <img class="intro-img img-fluid mb-3 mb-lg-0 rounded" src='./../../assets/img/horario.png' alt="">
        <div class="intro-text left-0 text-center bg-faded p-5 rounded " >
          <h2 class="section-heading mb-4">
            <span class="section-heading-upper">Ven Visitanos</span>
            <span class="section-heading-lower">Atendemos los Días </span>
          </h2>  
          <ul class="Datencion" v-for="(horario, horarioId) in horarios" v-bind:key="horarioId">
           <li class="list-unstyled-item list-hours-item d-flex ">
                  {{horarioId}}
                  <span class="ml-auto">{{horario}}</span> 
           </li>
         </ul>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    data(){
      return{
          horarios:{
            'Domingo' : '7:00 AM to 8:00 PM',
            'Lunes' : '7:00 AM to 8:00 PM',
            'Martes' : '7:00 AM to 8:00 PM',
            'Miércoles' : '7:00 AM to 8:00 PM',
            'Jueves' : '7:00 AM to 8:00 PM',
            'Viernes' : '7:00 AM to 8:00 PM',
            'Sábado' : '7:00 AM to 8:00 PM'
          }
      }
    }
  }
</script>