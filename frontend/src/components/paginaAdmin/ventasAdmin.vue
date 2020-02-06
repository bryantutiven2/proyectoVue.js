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
                                    <div class="row m-t-25">
                                        <div class="col-lg-11">
                                            <h1 id="tituloP">Mis Ventas</h1>
                                            <br>
                                            <div>
                                                <vue-good-table
                                                :columns="columns"
                                                :rows="rows"
                                                @on-row-click="onRowClick"
                                                :pagination-options="{
                                                    enabled: true,
                                                    perPage: 6,
                                                    mode: 'records'
                                                }"/>
                                            </div>
                                            <br>
                                            <br>
                                            <h3 id="tituloP">Venta Seleccionada</h3>
                                            <br>
                                            <br>
                                            <section class="page-section about-heading">
                                                <div class="container">
                                                    <div class="about-heading-content">
                                                    <div class="row">
                                                        <div class="col-xl-9 col-lg-10 mx-auto">
                                                        <div class="bg-faded rounded p-5">
                                                            <form>
                                                            <div class="form-row">
                                                                <div class="form-group col-md-3">
                                                                <label for="inputEmail4">Id Venta</label>
                                                                <input id="idventaf" type="text" class="form-control" placeholder="idventa" disabled>
                                                                </div>
                                                                <div class="form-group col-md-3">
                                                                <label for="inputEmail4">Producto</label>
                                                                <input id="prodf" type="text" class="form-control" placeholder="producto" disabled>
                                                                </div>
                                                            <div class='form-group col-md-6'>
                                                                <label for="inputEmail4">Total</label>
                                                                    <input type="text" class="form-control" id="totalf" disabled>
                                                            </div>
                                                                <div class="form-group col-md-4">
                                                                <label for="birthday">Cliente</label>
                                                                <input id="clientef" type="text"   class="form-control"  placeholder="cliente" disabled>
                                                                </div>
                                                                <div class="form-group col-md-4">
                                                                <label for="birthday">Precio</label>
                                                                <input id="preciof" type="number"   class="form-control"  placeholder="Precio" step="0.01" disabled>
                                                                </div>
                                                                <div class="form-group col-md-4">
                                                                    <label for="inputCity">Cantidad</label>
                                                                    <input id="cantidadf" type="number" class="form-control"  placeholder="Cantidad" required>
                                                                </div>
                                                            </div>
                                                            
                                                            <div id="botones" >
                                                                <button type="submit" class="btn btn-primary" @click="actualizar">Actualizar</button>
                                                                <button type="submit" class="btn btn-primary" @click="eliminar">Eliminar</button>
                                                            </div>
                                                            </form>
                                                        </div>
                                                        </div>
                                                    </div>
                                                    </div>
                                                </div>
                                                </section>
                                            <br>
                                            <br>
                                            <br>
                                            <h3 id="tituloP">Productos</h3>
                                            <br>
                                            <div>
                                                <vue-good-table
                                                :columns="columns1"
                                                :rows="listaProductos"
                                                @on-row-click="onRowClickP"
                                                :pagination-options="{
                                                    enabled: true,
                                                    perPage: 6,
                                                    mode: 'records'
                                                }"/>
                                            </div>
                                            <br>
                                            <h1 id="tituloP">Venta Unitaria</h1>
                                            <br>
                                            
                                            <section class="page-section about-heading">
                                                <div class="container">
                                                    <div class="about-heading-content">
                                                    <div class="row">
                                                        <div class="col-xl-9 col-lg-10 mx-auto">
                                                        <div class="bg-faded rounded p-5">
                                                            <form>
                                                            <div class="form-row">
                                                                <div class="form-group col-md-3">
                                                                <label for="inputEmail4">Id Usuario</label>
                                                                <input id="idusuario" type="text" class="form-control" placeholder="idusuario" required>
                                                                </div>
                                                                <div class="form-group col-md-3">
                                                                <label for="inputEmail4">cliente</label>
                                                                <input id="cliente" type="text" class="form-control" placeholder="usuario" required>
                                                                </div>
                                                            <div class='form-group col-md-6'>
                                                                <label for="inputEmail4">Fecha</label>
                                                                <div class="input-group date " id="datepicker">
                                                                    <input type="text" class="form-control" id="fecha">
                                                                </div>
                                                            </div>
                                                                <div class="form-group col-md-4">
                                                                <label for="birthday">id Producto</label>
                                                                <input id="idpro" type="text"   class="form-control"  placeholder="Precio" step="0.01" disabled>
                                                                </div>
                                                                <div class="form-group col-md-4">
                                                                <label for="birthday">Precio</label>
                                                                <input id="precio" type="number"   class="form-control"  placeholder="Precio" step="0.01" disabled>
                                                                </div>
                                                                <div class="form-group col-md-4">
                                                                    <label for="inputCity">Cantidad</label>
                                                                    <input id="cantidad" type="number" class="form-control"  placeholder="Cantidad" required>
                                                                </div>
                                                            </div>
                                                            
                                                            <div >
                                                                <button type="submit" class="btn btn-primary" @click="enviar()">Enviar</button>
                                                            </div>
                                                            </form>
                                                        </div>
                                                        </div>
                                                    </div>
                                                    </div>
                                                </div>
                                                </section>
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
const $ = require('jquery')
window.$ = $
import axios from 'axios'
import adminGeneral from './adminGeneral'

export default {
    components:{
        adminGeneral
    },
    data(){
        return{
            fecha:"",
            idusuario: "",
            factura :"",
            idventap: "",
            idventa: "",
            idproducto :"",
            cantidad :"",
            nombrep : "",
            preciop : "",
            idcliente:"",
            cnombre : "",
            capellido:"",
            totalp : "",
            clientec:"",

            listaPagos:[],
            listaProductos:[],
            listaClientes:[],
            listaVentas:[],
            listaVentasProducto:[],
            rows:[],
            selected: 'true',
            options:{
                '1':'true',
                '2':'false'
            },
            itemSelecionado: "",
            columns: [
                {
                label: 'IdVenta',
                field: 'idVenta',
                },
                {
                label: 'Producto',
                field: 'nombreComercial',
                },
                {
                label: 'Precio',
                field: 'precio',
                type: 'float',
                },
                {
                label: 'Cantidad',
                field: 'cantidadDisponible',
                type: 'number',
                },
                {
                label: 'Total',
                field: 'total',
                type: 'float',
                },
                {
                label: 'Cliente',
                field: 'cliente',
                },
            ],
            columns1: [
                {
                label: 'Id',
                field: 'idProducto',
                },
                {
                label: 'Nombre',
                field: 'nombreComercial',
                },
                {
                label: 'Precio',
                field: 'precio',
                type: 'float',
                }
            ]
        }
    },
    mounted(){
    },
    created(){
        this.cargarProductos();
        this.cargarClientes();
        this.cargarVentas();
        this.cargarVentasProducto();
        this.cargarPagos();
    },
    methods:{
        
        async actualizar(){
            try {
                let vent = $('#idventaf').val();
                $('#prodf').val();
                $('#totalf').val();
                $('#clientef').val();
                $('#preciof').val();
                let cant = $('#cantidadf').val();
                const url = 'http://localhost:8000/ventaProductos/'+$("#idventaf").val()+"/";
                const response = await axios.put(url,
                    {
                        idVentaProducto: "100",
                        cantidad: cant.toString(),
                        idProducto: '2',
                        idVenta: vent.toString()
                    },
                    { headers: {'Content-Type': 'application/json'} }
                )
                    console.log(response.data);
                }
                catch(e){
                    console.log(e)
                }
        },
        async eliminar(){
            try{
                const url = 'http://localhost:8000/ventaProductos/'+$("#idventaf").val()+"/";
                const response = await axios.delete(url)
                console.log(response.data);
                const url1 = 'http://localhost:8000/ventas/'+$("#idventaf").val()+"/";
                const response2 = await axios.delete(url1)
                console.log(response2.data);

            }
            catch(e){
                console.log(e)
            }
        },
        enviar(){
                try {
                this.idusuario = $('#idusuario').val();
                this.idcliente = $('#cliente').val();
                var fecha1 = new Date( $('#fecha').val());
                this.idproducto = $('#idpro').val();
                this.cantidad = $('#cantidad').val();
                this.preciop = $('#precio').val();
                this.totalp = this.cantidad * this.preciop;
                const resp1 =  axios.post('http://localhost:8000/pagos/', {
                    idPago: "100",
                    fechaHora: fecha1

                })
                console.log(resp1);
                const resp2 = axios.post('http://localhost:8000/ventas/', {
                    idVenta: "100",
                    total: this.totalp.toString(),
                    factura: this.factura,
                    idCliente : this.idcliente,
                    idUsuario: this.idusuario,
                    idPago: String(this.listaPagos.length+1)
                })
                console.log(resp2);
                const resp3= axios.post('http://localhost:8000/ventaProductos/', {
                    idVentaProducto: "100",
                    cantidad: this.cantidad.toString(),
                    idProducto: this.idproducto.toString(),
                    idVenta: (this.listaVentas.length+1).toString()
                })
                console.log(resp3.length)
                }
                catch(e){
                    console.log(e)
                }

        },
        async cargarPagos() {
            try {
                const response = await axios.get('http://localhost:8000/pagos/')
                this.listaPagos=response.data;
                console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        async cargarProductos() {
            try {
                const response = await axios.get('http://localhost:8000/productos/')
                this.listaProductos=response.data;
                console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        async cargarClientes() {
            try {
                const response = await axios.get('http://localhost:8000/clientes/')
                this.listaClientes=response.data;
                console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        async cargarVentas() {
            try {
                const response = await axios.get('http://localhost:8000/ventas/')
                this.listaVentas=response.data;
                console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        async cargarVentasProducto() {
            try {
                const response = await axios.get('http://localhost:8000/ventaProductos/')
                this.listaVentasProducto=response.data;
                this.cargarDatosTabla();
                console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        cargarDatosTabla(){
            for(let i=0; i<this.listaVentasProducto.length; i++){
                this.idventap = this.listaVentasProducto[i].idVentaProducto;
                this.idventa = this.listaVentasProducto[i].idVenta;
                this.idproducto = this.listaVentasProducto[i].idProducto;
                this.cantidad = this.listaVentasProducto[i].cantidad;
                for(let j=0; j< this.listaProductos.length; j++){
                    if(this.idproducto == this.listaProductos[j].idProducto){
                        this.nombrep = this.listaProductos[j].nombreComercial;
                        this.preciop = this.listaProductos[j].precio;
                    }
                }
                for(let k=0; k< this.listaVentas.length;k++ ){
                    if(this.idventa == this.listaVentas[k].idVenta){
                        this.idcliente = this.listaVentas[k].idCliente;
                    }
                }
                for(let l=0; l< this.listaClientes.length; l++){
                    if(this.idcliente == this.listaClientes[l].idCliente){
                        this.cnombre = this.listaClientes[l].nombre;
                        this.capellido = this.listaClientes[l].apellido;
                    }

                }
                this.totalp = parseInt(this.cantidad) * parseFloat(this.preciop);
                this.clientec = this.cnombre + " " + this.capellido;
                var listajson = {idVenta: this.idventap, nombreComercial: this.nombrep, precio: this.preciop, cantidadDisponible: this.cantidad, total: this.totalp, cliente: this.clientec}
                this.rows.push(listajson);
            }
            this.factura = "00"+String(parseInt(this.rows)+1)
            console.log(this.rows)
        },
        onRowClick(params) {
            this.itemSelecionado = params.row.idVenta;
            $('#idventaf').val(params.row.idVenta);
            $('#prodf').val(params.row.nombreComercial);
            $('#totalf').val(params.row.total);
            $('#clientef').val(params.row.cliente);
            $('#preciof').val(params.row.precio);
            $('#cantidadf').val(params.row.cantidadDisponible);
            
        },
        onRowClickP(params) {
            this.itemSelecionado = params.row.idProducto;
            
            $('#idpro').val(params.row.idProducto);
            $('#precio').val(params.row.precio);
            console.log(this.factura + parseInt(this.listaPagos.length+1))
        }
    }
}
</script>

<style>
    #tituloP{
        text-align: center;
        font-weight: bold;
    }
    #botones{
        display: grid;
        grid-template-columns: repeat(3,1fr);
        grid-gap: 60px;
    }
</style>