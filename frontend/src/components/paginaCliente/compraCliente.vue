<template>
    <div class="page-wrapper">
        <clienteGeneral />
        <div class="page-container">
            <div class="main-content">
                <!-- Aqui va el contenido-->
                <div class="section__content section__content--p30">
                    <div class="container-fluid">
                        <h1 class="text-center col-md-12" ><u>Compras</u></h1>                            
                        <div class="row text-justify compras ">
                            <div class="text-center m-auto" v-if="bandera"><strong>NO HAY COMPRAS REGISTRADAS</strong></div>
                            <div v-else class="mx-auto my-2 col-lg-5 col-md-2 border border-primary bg-info" v-for="(desarrollador, desarrolladorID) in datos" v-bind:key="desarrolladorID" id="equipoD1">  
                                                
                            
                            <p v-if="desarrollador.length>1" >Número de factura: {{desarrollador[1]}}</p>  
                            <p v-if="desarrollador.length>1">Total: {{desarrollador[2]}}</p>  
                        </div>                                
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import clienteGeneral from './clienteGeneral'

export default {
    components:{
        clienteGeneral
    },
    data(){
        return{
            idUser: this.$route.params.idUser,
            usuarios:[],
            ventas:[],
            idCliente:'',
            datos:[],
            bandera:false,
            headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': false,
                        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
                        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE'}        
        }
    },created(){
        this.cargar(),
        this.cargarVentas()
        //this.cargarPagos ()
        //this.rellenarDatos()
    },
    methods:{
        async cargar() {
            try {
                const response = await axios.get('http://localhost:8000/usuarios/'+this.idUser+"/")
                this.idCliente=response.data.idUsuario;
                this.usuarios=response.data;
            }
            catch(e){
                console.log(e)
            }
        },
        async cargarVentas() {
            try {
                const response = await axios.get('http://localhost:8000/ventas', this.headers  )
                this.ventas=response.data;                
                for(let venta of this.ventas){
                    var d=[]
                    if(venta.idUsuario==this.idCliente){
                        d.push(venta.idUsuario)
                        d.push(venta.factura)
                        d.push(venta.total)
                    }
                    this.datos.push(d)
                }
            }
            catch(e){
                console.log(e)
            }
        },
        validarDatos(){
            let data = this.datos
            for(var i=0; i < data.length; i++){
                if(data[i][0].length==1)
                    this.bandera=true
            }
        }
    }
}
</script>

<style>

</style>