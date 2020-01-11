<template>
  <div>
    <div class="row d-flex justify-content-center">
      <!-- Entrada de texto con boton -->
      <div class="input-group col-md-5">
        <input type="text" class="form-control" placeholder="Ingrese producto..."  aria-label="Ingrese producto..." aria-describedby="button-addon2">
        <div class="input-group-append">
          <button class="btn btn-success" type="button" id="button-addon2" >Buscar</button>
        </div>
      </div>
    </div>

    <br>
    <br>
    <!-- Listar Productos -->
    <div id="container"  class="row  text-center">
        <div class='col-md-3' id="product.id" v-for="product in listaProductos" :key="product">
           <div class="card mb-4 shadow-sm border-top-0 border-right-0 border-bottom-0 border-info">
            <img class="card-img-top promo" id="adv"  :src="product.url"   alt="">
            <div class="card-body">
              <hr>
              <h5 class="card-title" >{{product.nombre}}</h5>
              <p class='card-text' >{{product.Descripcion}}</p>
              <div class="d-flex justify-content-between align-items-center">
                <small class="text-muted">{{product.Precio}} </small>
              </div>
            </div>
          </div>
	 		  </div>
    </div>

    <!--Paginacion-->
    <div class="row d-flex justify-content-center">
      <div class="mt-3">
        <b-pagination-nav number-of-pages="10" base-url="#"></b-pagination-nav>
      </div>
    </div>
  </div>

</template>

<script>
  import productosJ from '../../../public/json/productos.json';
  export default {
    data(){
      return{
          listaProductos: productosJ,
          numeroProductos: 0,
          limitePage: 8,
          totalPaginas: 0
      }
    },
    methods:{
      contarProductos(){
        this.numeroProductos = this.listaProductos.length;
        console.log('Numero de productos es: '+this.numeroProductos);
        return this.numeroProductos;
      },
      sacarNumeroPaginas(){
          this.totalPaginas = Math.round(this.numeroProductos/this.limitePage);
          return this.totalPaginas;
      }
    },
    mounted(){
      this.contarProductos(),
      this.sacarNumeroPaginas()
    } 
  }
</script>
<style scoped>
  
</style>