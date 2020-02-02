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
                                            <!-- Mis productos -->
                                            <h1 id="tituloP">Mis Productos</h1>
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
                                            <br><br>
                                            <!-- Editar Producto -->
                                            <h1 id="tituloP">Editar Producto</h1>
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
                                                                <label for="inputEmail4">Id</label>
                                                                <input id="id" type="text" class="form-control" placeholder="Id" disabled>
                                                                </div>
                                                                <div class="form-group col-md-9">
                                                                <label for="inputEmail4">Nombre</label>
                                                                <input id="nombre" type="text" class="form-control" placeholder="Nombre" required>
                                                                </div>
                                                                <div class="form-group col-md-6">
                                                                <label for="birthday">Precio</label>
                                                                <input id="precio" type="number"   class="form-control"  placeholder="Precio" step="0.01" required>
                                                                </div>
                                                            </div>
                                                            <div class="form-row">
                                                                <div class="form-group col-md-12" >
                                                                    <label for="inputEmail4">Descripción</label>
                                                                    <textarea id="descripcion" class="form-control"   required></textarea>
                                                                </div>
                                                            </div>
                                                            <div class="form-row">
                                                                <div class="form-group col-md-6">
                                                                <label for="inputCity">Cantidad</label>
                                                                <input id="cantidad" type="number" class="form-control"  placeholder="Cantidad" required>
                                                                </div>
                                                                <div class="form-group col-md-4">
                                                                <label for="inputState">Es Medicamento</label>
                                                                <select id="inputState" class="form-control" v-model="selected">
                                                                    <option v-for="(option,clave) in options" :key="clave" v-bind:value="option">{{ option }}</option>   
                                                                </select>
                                                                </div>
                                                                <div class="form-group col-md-12">
                                                                <label for="inputAddress">URL</label>
                                                                <input id="url" type="text" class="form-control"  placeholder="link de la imagen" required>
                                                                </div>
                                                                <div class="form-group col-md-12">
                                                                <label for="inputAddress">Estado</label>
                                                                <input id="estado" type="text" class="form-control"  placeholder="true o false" required>
                                                                </div>
                                                            </div>
                                                            <div id="botones">
                                                                <button type="submit" class="btn btn-primary" @click="enviar">Enviar</button>
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
import adminGeneral from './adminGeneral'
import axios from 'axios'
export default {
    components:{
        adminGeneral
    },
    data(){
        return{
            id:"",
            nombre:"",
            descripcion:"",
            precio:"",
            cantidad:"",
            url:"",
            medicamento:"",
            estado:"",
            selected: 'true',
            options:{
                '1':'true',
                '2':'false'
            },
            itemSelecionado: "",
            columns: [
                {
                label: 'Id',
                field: 'idProducto',
                },
                {
                label: 'Nombre',
                field: 'nombreComercial',
                },
                {
                label: 'Descripción',
                field: 'descripcion',
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
                label: 'Estado',
                field: 'estado',
                },
            ],
            rows: [
                
            ]
        }
    },
    created(){
        this.cargar()
    },
    methods:{
            async enviar(){
                try {
                this.medicamento = "true";
                this.nombre = $('#nombre').val();
                this.precio = $('#precio').val();
                this.descripcion = $('#descripcion').val();
                this.cantidad = $('#cantidad').val();
                this.url = $('#url').val();
                this.estado = $('#estado').val();
                const response = await axios.post('http://localhost:8000/productos/', {
                    idProducto: "100",
                    nombreComercial: this.nombre.toString(),
                    descripcion: this.descripcion.toString(),
                    precio: this.precio.toString(),
                    cantidadDisponible: this.cantidad.toString(),
                    esMedicamento: this.medicamento.toString(),
                    url: this.url.toString(),
                    estado: this.estado.toString()
                })
                    this.rows=response.data;
                    console.log(response.data);
                }
                catch(e){
                    console.log(e)
                }
            },
            async actualizar(){
                try {
                    this.id = $("#id").val();
                    this.medicamento = "true";
                    this.nombre = $('#nombre').val();
                    this.precio = $('#precio').val();
                    this.descripcion = $('#descripcion').val();
                    this.cantidad = $('#cantidad').val();
                    this.url = $('#url').val();
                    this.estado = $('#estado').val();
                    const url = 'http://localhost:8000/productos/'+$("#id").val()+"/";
                    const response = await axios.put(url,
                        {
                            idProducto: this.id.toString(),
                            nombreComercial: this.nombre.toString(),
                            descripcion: this.descripcion.toString(),
                            precio: this.precio.toString(),
                            cantidadDisponible: this.cantidad.toString(),
                            esMedicamento: this.medicamento.toString(),
                            url: this.url.toString(),
                            estado: this.estado.toString()
                        },
                        { headers: {'Content-Type': 'application/json'} }
                    )
                        this.rows=response.data;
                        console.log(response.data);
                    }
                    catch(e){
                        console.log(e)
                    }
            },
            async eliminar(){
                try{
                    this.id = $("#id").val();
                    const url = 'http://localhost:8000/productos/'+$("#id").val()+"/";
                    const response = await axios.delete(url)
                    this.rows=response.data;
                    console.log(response.data);
                }
                catch(e){
                    console.log(e)
                }
            },
            async cargar () {
                try {
                    const response = await axios.get('http://localhost:8000/productos/')
                    this.rows=response.data;
                    console.log(response.data);
                }
                catch(e){
                    console.log(e)
                }
            },
            onRowClick(params) {
                this.itemSelecionado = params.row.idProducto;
                
                for(var i=0; i<this.rows.length; i++){
                    if(this.rows[i].idProducto == params.row.idProducto){
                        this.url=this.rows[i].url;
                        this.medicamento = this.rows[i].esMedicamento;
                    }
                }
                $('#id').val(params.row.idProducto);
                $('#nombre').val(params.row.nombreComercial);
                this.nombre=params.row.nombreComercial;
                $('#precio').val(params.row.precio);
                this.precio = params.row.precio;
                $('#descripcion').val(params.row.descripcion);
                this.descripcion = params.row.descripcion;
                $('#cantidad').val(params.row.cantidadDisponible);
                this.cantidad = params.row.cantidadDisponible;
                $('#url').val(this.url);
                $('#estado').val(params.row.estado);
                this.estado = params.row.estado;
                console.log(this.itemSelecionado)
                // params.row - row object 
                // params.pageIndex - index of this row on the current page.
                // params.selected - if selection is enabled this argument 
                // indicates selected or not
                // params.event - click event
            }
    }
}
</script>

<style scoped>
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