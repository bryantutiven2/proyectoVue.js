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
        <input type="text " @click="cargar">
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

    export default {
        name: 'InicioGeneral',
        components: {
            Farmacia,
            Nav,
            Horarios,
            Mapa,
            Footer
        },
        data () {
            return {
            info: null
            }
        },
        methods:{
            cargar () {
            //axios.get('http://127.0.0.1:8000/usuarios/')
            //.then(response => (this.info = response))
            this.axios.get('http://localhost:8000/usuarios/').then((response) => {
                this.info=response.data;
            //console.log(response.data);
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