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
        <Footer />
    </div>
    

</template>
<script>
    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Horarios from './Horarios.vue'
    import Mapa from './SeccionMapa.vue'
    import Footer from './../principales/Footer.vue'
    //import axios from 'axios'
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
        },
        data () {
            return {
            info: []
            }
        },
        methods:{
            
        }
    }
</script>
<style scoped>
    .layout {
    display: flex;
    flex-direction: column;
    }
</style>