<template>
    <div class = 'layout'>
        <div>
            <Farmacia />
            <Nav />
            <br>
            <Promociones />
            <PromocionesUnitario />
            <br>
            <br><br><br><br>
        </div>
        <Footer />
    </div>
</template>

<script>
    
    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Promociones from './Promociones.vue'
    import PromocionesUnitario from './PromocionesUnitarios.vue'
    import Footer from './../principales/Footer'
    
    export default {
        name: 'NoticiasGeneral',
            components: {
            Farmacia,
            Nav,
            Promociones,
            PromocionesUnitario,
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