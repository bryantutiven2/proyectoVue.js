<template>
    <div class = 'layout'>
        <div>
            <Farmacia />
            <Nav />
            <br>
            <Horarios />
        </div>
        <div>
            <br><br><br><br><br><br><br><br><br>
            <Mapa />
        </div>
        <div>
            {{info}}
        </div>
        <Footer />
        <form action="">
            <label>Nombres</label>
             <input type="text"  placeholder="id" required>
             <label>direccion</label>
             <input type="text"  placeholder="direccion" required>
             <label>dueno</label>
             <input type="text"  placeholder="dueno" required>
             <button type="submit" class="btn btn-primary" @click="enviar">Enviar Datos</button>
        </form>
    </div>
    

</template>
<script>
    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Horarios from './Horarios.vue'
    import Mapa from './SeccionMapa.vue'
    import Footer from './../principales/Footer.vue'
    import axios from 'axios'
    export default {
        name: 'InicioGeneral',
        components: {
            Farmacia,
            Nav,
            Horarios,
            Mapa,
            Footer
        },
        created(){
            this.cargar(),
            this.enviar(),
            this.delete(),
            this.put()
        },
        data () {
            return {
            info: []
            }
        },
        methods:{/*
            put(){
                axios.put('http://localhost:8000/casas/2' + '1',
                    {descripcion: 'taller3'},
                    {dueno: 'bryanT'
                }).then(response => {
                    this.result.splice(id, '1')
                    console.log(this.result);
                });
            },

            delete(){
                axios.delete('http://localhost:8000/casas/1' )
                .then(response => {
                    this.result.splice(id, '1')
                    console.log(this.result);
                });
            },
            enviar(){
                let currentObj = this;
                this.axios.post('http://localhost:8000/casas/', {
                    id:'10',
                    descripcion: 'casaprueba',
                    dueno: 'taller3'
                })
                .then(function (response) {
                    currentObj.output = response.data;
                })
                .catch(function (error) {
                    currentObj.output = error;
                });
            }*/,
            cargar () {
            axios.get('http://localhost:8080/usuarios/').then((response) => {
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
<style scoped>
    .layout {
    display: flex;
    flex-direction: column;
    }
</style>