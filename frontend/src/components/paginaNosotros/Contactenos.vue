<template>
    <section class="page-section about-heading">
      <div class="container">
        <div class="about-heading-content">
          <div class="row">
            <div class="col-xl-9 col-lg-10 mx-auto">
              <div class="bg-faded rounded p-5">
                <h2 class="section-heading mb-4">
                <span class="section-heading-lower">CONTÁCTANOS</span>  
                </h2>
                <form @submit.prevent="sendEmail">
                  <div class="form-row">
                    <div class="form-group col-md-6">
                      <label for="inputEmail4">Nombres</label>
                      <input type="text" class="form-control" v-model="subject" id="Nombre" placeholder="Nombres" required>
                    </div>
                    <div class="form-group col-md-6">
                      <label for="inputEmail4">Apellidos</label>
                      <input type="text" class="form-control" v-model="apellido" id="Apellido" placeholder="Apellidos" required>
                    </div>
                    <div class="form-group col-md-6" >
                      <label for="inputEmail4">Email</label>
                      <input type="email"  class="form-control" v-model="email" id="inputEmail4" placeholder="Email" required>
                    </div>
                    <div class="form-group col-md-6">
                      <label for="birthday">Fecha de Nacimiento</label>
                      <input type="text"   class="form-control" id="birthday" placeholder="dd/mm/yy" required>
                    </div>
                  </div>
                  <div class="form-row">
                    <div class="form-group col-md-6">
                      <label for="inputCity">Ciudad</label>
                      <input type="text" class="form-control" v-model="ciudad" id="inputCity" required>
                    </div>
                    <div class="form-group col-md-4">
                      <label for="inputState">Provincia</label>
                      <select id="inputState" class="form-control" v-model="selected">
                          <option v-for="(option,clave) in options" :key="clave" v-bind:value="option">{{ option }}</option>   
                      </select>
                    </div>
                    <div class="form-group col-md-12">
                      <label for="inputAddress">Dirección</label>
                    <input type="text" class="form-control" v-model="direccion" id="inputAddress" placeholder="Cdla La Fae Mz 12" required>
                    </div>
                 </div>
                  <div class="form-group">
                  <div class="form-group md-3">
                    <label for="validationTextarea">Detalles</label>
                    <textarea class="form-control" id="validationTextarea" v-model="text"  required></textarea>
                  </div>
                  </div>
                  <button type="submit" class="btn btn-primary"  id="enviar">Enviar Datos</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
</template>
<script>
  const $ = require('jquery')  
  import emailjs from 'emailjs-com';
  window.$ = $

  export default {
    data(){
        return{
            selected: 'Guayas',
            options:{
                '1':'Guayas',
                '2':'Esmeraldas',
                '3':'Pichincha',
                '4':'Azuay',
                '5':'Los Rios'
            },
            email: '',
            text: '',
            subject: '',
            direccion: '',
            ciudad:'',
            apellido: ''
        }
    },

    methods:{     
      
      sendEmail(){
        alert("Mensaje Enviado");

        var params = {
          from_name: this.subject+" "+this.apellido,
          to_name: 'Dr. Luis Sarango',
          reply_email: this.email,
          message_html: this.text,
          address: this.direccion,
          ciudad: this.ciudad,
          provincia: this.selected
          };

          emailjs.send('gmail', 'template_fg0HOolf', params,'user_POQtWQNOyU183a9zEbQ9w')
          .then(function(response) {
            console.log('SUCCESS!', response.status, response.text);
          }, function(error) {
            console.log('FAILED...', error);
          });

          $('input[type="text"]').val('');
          $('textarea').val('');
          $('input[type="email"]').val('');
      }      
      
    }
}
</script>