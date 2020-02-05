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
                                        <img src="./../../assets/img/image.png" class="img-thumbnail " alt="Bienvenido" />
                                        <h6><strong>@jupgiuv</strong></h6>
                                    </div>
                                    <div class="col-md-10 float-right">
                                        <h1 class="text-center "><u>Información Personal</u></h1>
                                        <p><strong>Datos: </strong> Juana Piguave</p>
                                        <p><strong>Sexo: </strong>Masculino</p>
                                        <p><strong>Cédula: </strong>0987456328</p>
                                        <p><strong>Edad: </strong>22</p>
                                        <p><strong>Correo: </strong>jogv@gmail.com</p>
                                        <pre>
                                            {{$data}}
                                        </pre>
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
                const response = await axios.get('http://localhost:8000/usuarios/')
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