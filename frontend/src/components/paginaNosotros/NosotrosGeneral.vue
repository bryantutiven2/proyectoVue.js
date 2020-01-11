<template>

    <div class = 'layout'>
        <div>
            <Farmacia />
            <Nav />
            <br>
            <Mision />
            <br>
            <EquipoDeDesarrollo />
            <br>
            <Contactenos />
        </div>
        <Footer />
    </div>
</template>

<script>
    
    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Mision from './Mision.vue'
    import EquipoDeDesarrollo from './EquipoDeDesarrollo'
    import Contactenos from './Contactenos'
    import Footer from './../principales/Footer'
    
    export default {
        name: 'InicioGeneral',
            components: {
            Farmacia,
            Nav,
            Mision,
            EquipoDeDesarrollo,
            Contactenos,
            Footer
        }

    }
</script>

<style scoped>
    .layout {
    display: flex;
    flex-direction: column;
    }
</style>