<template>
    <div class = 'layout'>
        <div>
            <Farmacia />
            <Nav />
            <br>
            <section class="page-section cta">
                <div class="container" id="login">
                    <form id="formulario"  @submit.prevent="redirigirVentana">
                        <br>
                        <h2>Login</h2>
                        
                        <div class="col-xs-4">
                            <input class="form-control" v-model="user" id="nombre-input" type="text" placeholder="Usuario" required>
                        </div>
                        <br>
                        <div class="col-xs-4">
                            <input class="form-control" v-model="clave" id="pwd-input" type="password" placeholder="Contraseña" required>
                        </div>
                        <br>
                        <div id="botonSesion">
                            <input type="submit" id="iniciar-sesion" value="Iniciar Sesión" class="btn btn-success btn-lg-1 col-sm-7" >
                        </div>
                    </form>
                    <pre>
                        {{$data.user}}
                        {{$data.clave}}
                    </pre>
                </div>
            </section>
        </div>
        
        <Footer />
    </div>
</template>

<script>
    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Footer from './../principales/Footer.vue'
    import axios from 'axios'
    
    export default {
        name: 'SesionGeneral',
        components: {
            Farmacia,
            Nav,
            Footer
        },data(){
            return{
                user:'',
                clave:'',
                usuarios:[],
            }
        },
        created(){
            this.cargar()
        },
        mounted() {
            
        }, 
        methods:{
            redirigirVentana(){
                let bandera=false
                for (let usuario of this.usuarios){
                    if(usuario.usuario== this.user && usuario.contrasena==this.clave){
                        console.log(usuario.usuario)
                        console.log(usuario.edad)
                        bandera=true
                        this.$router.push("/perfilCliente/"+usuario.usuario) 
                    }
                }
                if(!bandera)
                    alert('Usuario no válido')
                               
            },
            async cargar () {
                try {
                    const response = await axios.get('http://localhost:8000/usuarios/')
                    this.usuarios=response.data;
                    //console.log(response.data);
                }
                catch(e){
                    console.log(e)
                }
            },
        }
    }
</script>

<style>
    .layout {
    display: flex;
    flex-direction: column;
    }
    #botonSesion{
        text-align: center;
    }
</style>