<template>
    <nav class="navbar navbar-expand-lg navbar-dark py-lg-4" id="mainNav">
    <div class="container">
      <a class="navbar-brand text-uppercase text-expanded font-weight-bold d-lg-none" href="#">FARMACIA NARCISA DE JESÚS</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id=" navbarResponsive" >
        <ul class="navbar-nav mx-auto" >
          <li class="nav-item active px-lg-4">
            <router-link class="nav-link text-uppercase text-expanded" to="/">Inicio
            <span class="sr-only">(current)</span> </router-link>
          </li>
          <li class="nav-item px-lg-4">
            <router-link class="nav-link text-uppercase text-expanded " to="/nosotros">Nosotros</router-link>
          </li>
          <li class="nav-item px-lg-4">
            <router-link class="nav-link text-uppercase text-expanded " to="/noticias">Noticias</router-link>
          </li>
          <li class="nav-item px-lg-4">
            <router-link class="nav-link text-uppercase text-expanded " to="/productos">Productos</router-link>
          </li>
          <li class="nav-item px-lg-4">
            <button class="nav-link text-uppercase text-expanded " type="button" @click="redireccionar()">Iniciar Sesión</button>
          </li>
          <li class="nav-item px-lg-4">
            <router-link class="nav-link text-uppercase text-expanded " to='/registrar'>Registrar</router-link>
          </li>
          <!--<li class="nav-item px-lg-4">
            <router-link class="nav-link text-uppercase text-expanded " to='/ventasAdmin'>Admin</router-link>
          </li>-->
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
    data(){
      return{
        
      }
    },
    methods:{
      redireccionar(){
        var cookies = null;
        cookies = localStorage.getItem("user");
        if(cookies != null){
              if(cookies == 'admin'){
                  this.$router.push("/ventasAdmin") 
              }
              else{
                this.$router.push("/perfilCliente/"+cookies+"/") 
              }
              
          }
          else{
            this.$router.push("/iniciarSesion") 
          }
    }
    }
}
</script>
<style scoped>
    
</style>