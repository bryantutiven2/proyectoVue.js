<template>
    <div class="page-wrapper">
        <clienteGeneral />
        <div class="page-container">
            <div class="main-content">
                <!-- Aqui va el contenido-->
                <div class="section__content section__content--p30">
                        <div class="container-fluid">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="col-md-2 float-left text-center"> 
                                        <img src="./../../assets/img/user1.png" class="img-thumbnail " alt="Bienvenido" />                                        
                                    </div>
                                    <div class="col-md-10 float-right">
                                        <h1 class="text-center "><u>Información Personal</u></h1>
                                        <p><strong>Datos: </strong> {{this.usuarios.nombre}} {{this.usuarios.apellido}}</p>
                                        <p><strong>Teléfono: </strong>{{this.usuarios.telefono}}</p>
                                        <p><strong>Cédula: </strong> {{this.usuarios.cedula}}</p>
                                        <p><strong>Edad: </strong>{{this.usuarios.edad}}</p>
                                        <p><strong>Correo: </strong>{{this.usuarios.correo}}</p>
                                        <p><strong>Dirección: </strong>{{this.usuarios.direccion}}</p>
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
import axios from 'axios'
import clienteGeneral from './clienteGeneral'
export default {
    components:{
        clienteGeneral
    },data(){
        return{
            idUser: this.$route.params.idUser,
            //clienteId: this.$route.params.clienteId,
            usuarios:[]
        }

    },
    created(){
        this.cargar()
    },
    methods:{
        async cargar () {
            try {
                const response = await axios.get('http://localhost:8000/usuarios/'+this.idUser+"/")
                this.usuarios=response.data;
                //console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        }
    }
}
</script>

<style>

</style>