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
                                <div class="col-md-3 bg-info m-1 rounded" id="compra1">
                                    <p>Fecha: 2/10/2019</p>
                                    <p>Productos:</p>
                                    <p>Paracetamol 0.50</p>
                                    <p>Ibuprofeno 2.50</p>
                                    <p>Calcibon 1.50</p>
                                </div>
                                <div class="col-md-3 bg-info m-1 rounded" id="compra2">
                                    <p>Fecha: 4/10/2019</p>
                                    <p>Productos:</p>
                                    <p>Paracetamol 0.60</p>
                                    <p>Ibuprofeno 2.50</p>
                                    <p>Calcibon 1.50</p>
                                </div>
                                <div class="col-md-3 bg-info m-1 rounded" id="compra3">
                                    <p>Fecha: 1/10/2018</p>
                                    <p>Productos:</p>
                                    <p>Paracetamol 0.60</p>
                                    <p>Ibuprofeno 2.50</p>
                                    <p>Calcibon 1.50</p>
                                </div>
                                <div class="col-md-3 bg-info m-1 rounded" id="compra4">
                                    <p>Fecha: 1/10/2018</p>
                                    <p>Productos:</p>
                                    <p>Paracetamol 0.60</p>
                                    <p>Ibuprofeno 2.50</p>
                                    <p>Calcibon 1.50</p>
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
            pagos:[],
            idCliente:'',
            datos:[]
        }
    },created(){
        this.cargar(),
        this.cargarVentas()
        this.cargarPagos ()
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
                const response = await axios.get('http://localhost:8000/ventas',
                        { headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'} } )
                this.ventas=response.data;
            }
            catch(e){
                console.log(e)
            }
        },
        async cargarPagos() {
            try {
                const response = await axios.get('http://localhost:8000/pagos',
                        { headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'} })
                this.pagos=response.data;
            }
            catch(e){
                console.log(e)
            }
        },
        rellenarDatos(){
            for(let venta of this.ventas){
                let arreglo=[]
                if(venta.idUsuario==this.idCliente){
                    arreglo.push(venta.factura)
                    arreglo.push(venta.total)
                }
                for(let pago of this.pagos){
                    if(venta.idPago==pago.idPago){
                        arreglo.push(pago.fechaHora)
                    }
                }
                console.log(arreglo)
                this.datos.push(arreglo)
            }

        }
    }
}
</script>

<style>

</style>