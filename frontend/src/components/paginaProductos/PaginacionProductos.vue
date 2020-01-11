<template>
  <div>
    <div class="row d-flex justify-content-center">
      <!-- Entrada de texto con boton -->
      <div class="input-group col-md-5">
        <input type="text" id="entradaBuscar" @keyup.enter="resultadoBusqueda" class="form-control" placeholder="Ingrese producto..."  aria-label="Ingrese producto..." aria-describedby="button-addon2">
        <div class="input-group-append">
          <button class="btn btn-success" type="button" id="buscar" @click="resultadoBusqueda">Buscar</button>
        </div>
      </div>
    </div>

    <br>
    <br>
    <!-- Listar Productos -->
    <div id="container"  class="row  text-center">
        <div class='col-md-3' id="product.id" v-for="product in displayProductos" :key="product.id">
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
      <div class="btn-group">
          <b-button
              type="button"
              :disabled="page==1"
              @click="page--"
              variant="light"
              class="bg-white text-primary">
              {{izquierda1}}
          </b-button>
          <b-button
              type="button"
              v-for="pageNumber in pages.slice(page-1, limitePage)" :key="pageNumber"
              @click="page=pageNumber"
              variant="light"
              class=" bg-white text-dark">
              {{pageNumber}}
          </b-button>
          <b-button
              type="button"
              @click="page++"
              :disabled="page==pages.length"
              variant="light"
              class="bg-white text-primary">
              {{derecha1}}
          </b-button>
      </div>
    </div>
  </div>

</template>

<script>
  const $ = require('jquery')
  window.$ = $

  import productosJ from '../../../public/json/productos.json';
  export default {
    data(){
      return{
          izquierda1: '<',
          derecha1: '>',
          izquierda: '<<',
          derecha: '>>',
          productos: [], //articles
          listaProductos: productosJ,
          numeroProductos: 0,
          page: 1,
          limitePage: 8,
          totalPaginas: 0, //perPage
          pages: []
      }
    },
    methods:{
      obtenerProductos(){
        this.productos =productosJ;
        return this.productos;
      },
      contarProductos(){
        this.numeroProductos = this.listaProductos.length;
        console.log('Numero de productos es: '+this.numeroProductos);
        return this.numeroProductos;
      },
      sacarNumeroPaginas(){
          this.totalPaginas = Math.ceil(this.numeroProductos/this.limitePage);
          console.log(this.totalPaginas)
          return this.totalPaginas;
      },
      paginate(productos){
          let page = this.page;
          let perPage = this.limitePage;
          let from = (page * perPage) - perPage;
          let to = (page * perPage);
          return productos.slice(from, to);

      },
      setProductos(){
          let numberOfPages = this.totalPaginas;
          for(let i=1; i<=numberOfPages; i++){
              this.pages.push(i);
          }
      },
      resultadoBusqueda(){
          let search = document.getElementById("entradaBuscar").value;
          let productoSearch = search.toLowerCase();
          console.log(productoSearch);
          if(productoSearch.length>0){
              var divs = $('.col-md-3');
              divs.each(function(){
                var h5 = $(this).find('h5') 
                if(h5.text().toLowerCase().indexOf(productoSearch)>=0) {
                  $(this).show()
                }
                else {
                  $(this).hide()
                }

              })
          }
          return false;
      }
    },
    mounted(){
      this.obtenerProductos(),
      this.contarProductos(),
      this.sacarNumeroPaginas()
    },
    computed:{
        displayProductos(){
          return this.paginate(this.productos)
        }
    },
    watch:{
      productos(){
        this.setProductos();
      }
    } 
  }
</script>
<style scoped>
  
</style>