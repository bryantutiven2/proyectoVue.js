<template>
    <div class="page-wrapper">
        <adminGeneral />
        <div class="page-container">
            <div class="main-content">
                <!-- Aqui va el contenido-->
                <div class="section__content section__content--p30">
                        <div class="container-fluid">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="text-center m-1 ">
                                         <h1>Reporte de Lotes <br> para la devolución de medicamentos</h1>
                                        <img width="400" src="https://image.freepik.com/free-vector/medication-drugs-pills-pharmacy-drug-bottles-flat-illustration_102902-333.jpg">
                                        <div class="form-row">
                                        <div class="form-group col-md-6">
                                            <br>
                                        <input class="control form-control" type="text" v-model="producto" @keyup.enter="readProduct" placeholder="Nombre del producto">
                                        
                                        </div>
                                        <div class="form-group col-md-6">    
                                            <br>
                                        <button class="btn btn-primary" v-on:click="seen = !seen" @click="readProductoByNombre">Consultar lotes</button>
                                        </div>
                                        </div>
                                        <div>
                                        
                                        </div>

                                        <ul></ul>

                                    <div class="card" v-if="seen">
                                        <ul >
                                            
                                            <li  class="list-group-item list-group-item-action">

                                        
                                            <div class="card">
                                                <div class="card-header">
                                                <h3> {{ producto }} </h3>
                                                <h3> {{idProducto}} </h3>

                                                <img width="300" v-bind:src="url">
                                                <div>
                                                    <h4>Descripcion:</h4><p>  {{descripcion}} </p>
                                                </div>
                                                
                                                <div>
                                                    <h4>Precio: </h4><p>  {{precioCosto}} </p>
                                                </div>
                                                <div>
                                                    <h4>Precio Venta: </h4><p>  {{precioVenta}} </p>
                                                </div>
                                                <div>
                                                    <h4>Precio Venta: </h4><p> {{cantidadDisponible}} </p>
                                                </div>
                                                <div>
                                                    <h4>Estado: </h4><p> {{estado}} </p>
                                                </div>


                                                </div>
                                                <div class="card-body">
                                                <table class="table table-striped table-bordered">
                                                    <thead>
                                                    <tr>
                                                        <th> idLote </th>
                                                        <th>FechaExpiracion</th>
                                                        <th>FechaDevolucion</th>
                                                        <th>Stock</th>

                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                    <tr v-for="w in medicamentos" :key="w.idLote">
                                                    <td>
                                                        <a >{{w.idLote}}</a>
                                                        </td>
                                                        <td>
                                                        <a >{{w.FechaVencimiento}}</a>
                                                        </td>
                                                        <td> 
                                                        <a>{{w.FechaDevolucion}}</a>

                                                        </td>
                                                        <td>
                                                        {{w.Cantidad}}
                                                        </td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                                </div>
                                            </div>

                                            </li>
                                        </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                </div>
                
            </div>
        </div>
    </div>
</template>

<script>
import adminGeneral from './adminGeneral'
import axios from 'axios'
import { db } from "../../../public/script/firebase.js";
export default {
  name: "app",
  components:{
      adminGeneral
  },
  data() {
    return {
      seen: false,
      rows:[],
      idProducto: "",
      producto: "",
      precio: 0,
      medicamentos: [],
      genericos: [],
      descripcion:"",
      precioCosto:"",
      precioVenta:"",
      cantidadDisponible:"",
      url :"",
      estado:""
    };
  },
  firestore() {
    return {
    //  medicamentos: db.collection("medicamentos"),
     //genericos: db.collectionGroup("genericos")
    };
  },
  methods: {
    async cargar (id) {
        try {
            const url = "http://localhost:8000/productos/"+id+"/"
            const response = await axios.get(url)
            this.rows=response.data;
            this.descripcion= this.rows.descripcion;
            var str1 = String(this.rows.precio);
            this.precioCosto= "$"+ str1.slice(0, 5);
            var str = String(this.rows.precio*1.12)
            this.precioVenta = "$"+ str.slice(0, 5);
            this.cantidadDisponible= this.rows.cantidadDisponible;
            this.url = this.rows.url;
            this.estado = this.rows.estado;
            console.log(this.rows);
        }
        catch(e){
            console.log(e)
        }
    },
    readProductoByNombre: function() {
      this.medicamentos=[];
      let docRef = db.collection("lotes").where("nombreComercial", "==", this.producto);

    docRef.get()
    .then(querySnapshot => {

        querySnapshot.forEach(doc =>{
           // console.log(doc.id, " => ", doc.data());
            let datos = doc.data();
            this.idProducto = datos['idProducto'];// de aqui sacas el id para el GET
            //Cargar el productos
            this.cargar(this.idProducto);
            

            //console.log("idProducto", '=>', idProducto)
            this.medicamentos.push(datos); 


        });
    })
    .catch(function(error) {
        console.log("Error getting documents: ", error);
    });
        console.log('idProducto --> ', this.idProducto)


    }
  }
}
</script>

<style>

</style>