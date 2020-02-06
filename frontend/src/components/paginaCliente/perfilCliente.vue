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
                                        <input class="col-3" type="text" placeholder="Teléfono" name="telf" v-model.trim="telf">
                                        <p><strong>Cédula: </strong> {{this.usuarios.cedula}}</p>
                                        <p><strong>Edad: </strong>{{this.usuarios.edad}}</p>
                                        <p><strong>Correo: </strong>{{this.usuarios.correo}}</p>
                                        <p><strong>Dirección: </strong>{{this.usuarios.direccion}}</p>
                                        <b-button type="submit" variant="primary" v-on:click="actualizar" >Actualizar</b-button>
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
            usuarios:[],
            /*idUsuario: this.usuarios.idUsuario,
            cedula: this.usuarios.cedula,
            nombre: this.usuarios.nombre,
            apellido: this.usuarios.apellido,*/
            telf:'',
            /*edad: this.usuarios.edad,
            direccion: this.usuarios.direccion,
            correo: this.usuarios.correo,
            usuario: this.usuarios.usuario,
            contrasena: this.usuarios.contrasena*/
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
                this.telf=response.data.telefono;
                //console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        async actualizar() {
            alert("Campo Actualizado")
            try {
                
                const url = 'http://localhost:8000/usuarios/'+this.idUser+"/";
                const response = await axios.put(url,
                        {
                            idUsuario: this.usuarios.idUsuario.toString(),
                            cedula: this.usuarios.cedula.toString(),
                            nombre: this.usuarios.nombre.toString(),
                            apellido: this.usuarios.apellido.toString(),
                            telefono:this.telf.toString(),
                            edad: this.usuarios.edad.toString(),
                            direccion: this.usuarios.direccion.toString(),
                            correo: this.usuarios.correo.toString(),
                            usuario: this.usuarios.usuario.toString(),
                            contrasena: this.usuarios.contrasena.toString()
                        },
                        { headers: {'Content-Type': 'application/json'} }
                    )
                console.log(response.data);
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