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
            this.cargar()
        },
        data () {
            return {
            info: []
            }
        },
        methods:{
            cargar () {
            //axios.get('http://127.0.0.1:8000/usuarios/')
            //.then(response => (this.info = response))
            axios.get('http://localhost:8000/usuarios/').then((response) => {
                this.info=response.data;
            //console.log(response.data);
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