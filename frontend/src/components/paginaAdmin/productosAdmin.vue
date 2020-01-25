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
                                        <table class="table table-striped">
                                            <thead>
                                                <tr>
                                                    <th scope="col" v-for="(value,clave) in label" :key="clave">{{value}}</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="item in info" :key="item.idProducto">
                                                    <th scope="row">{{item.idProducto}}</th>
                                                    <td>{{item.nombreComercial}}</td>
                                                    <td>{{item.descripcion}}</td>
                                                    <td>{{item.precio}}</td>
                                                    <td>{{item.cantidadDisponible}}</td>
                                                    <td>{{item.estado}}</td>
                                                </tr> 
                                            </tbody>
                                        </table>
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
export default {
    components:{
        adminGeneral
    },
    data(){
        return{
            label:{
                1: 'ID',
                2: 'Nombre',
                3: 'Descripcion',
                4: 'Precio',
                5: 'Cantidad',
                6: 'Estado'
            },
            info: []
        }
    },
    created(){
        this.cargar()
    },
    methods:{
            cargar () {
            axios.get('http://localhost:8000/productos/').then((response) => {
                this.info=response.data;
                console.log(response.data);
            })
            .catch((e)=>{
                console.log(e)
            })
        }
    }
}
</script>

<style>

</style>