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
                <form>
                  <div class="form-row">
                    <div class="form-group col-md-6">
                      <label for="inputEmail4">Nombres</label>
                      <input type="text" class="form-control" placeholder="Nombres" required>
                    </div>
                    <div class="form-group col-md-6">
                      <label for="inputEmail4">Apellidos</label>
                      <input type="text" class="form-control" placeholder="Apellidos" required>
                    </div>
                    <div class="form-group col-md-6" >
                      <label for="inputEmail4">Email</label>
                      <input type="email"  class="form-control" id="inputEmail4" placeholder="Email" required>
                    </div>
                    <div class="form-group col-md-6">
                      <label for="birthday">Fecha de Nacimiento</label>
                      <input type="text"   class="form-control" id="birthday" placeholder="dd/mm/yy" required>
                    </div>
                  </div>
                  <div class="form-row">
                    <div class="form-group col-md-6">
                      <label for="inputCity">Ciudad</label>
                      <input type="text" class="form-control" id="inputCity" required>
                    </div>
                    <div class="form-group col-md-4">
                      <label for="inputState">Provincia</label>
                      <select id="inputState" class="form-control" v-model="selected">
                          <option v-for="(option,clave) in options" :key="clave" v-bind:value="option">{{ option }}</option>   
                      </select>
                    </div>
                    <div class="form-group col-md-12">
                      <label for="inputAddress">Dirección</label>
                    <input type="text" class="form-control" id="inputAddress" placeholder="Cdla La Fae Mz 12" required>
                    </div>
                 </div>
                  <div class="form-group">
                  <div class="form-group md-3">
                    <label for="validationTextarea">Detalles</label>
                    <textarea class="form-control" id="validationTextarea"  required></textarea>
                  </div>
                  </div>
                  <button type="submit" class="btn btn-primary" >Enviar Datos</button>
                </form>
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
            selected: 'Guayas',
            options:{
                '1':'Guayas',
                '2':'Esmeraldas',
                '3':'Pichincha',
                '4':'Azuay',
                '5':'Los Rios'
            }
        }
    }
}
</script>