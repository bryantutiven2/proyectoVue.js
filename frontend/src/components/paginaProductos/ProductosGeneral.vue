<template>
    <div class = 'layout'>
        <div>
            <Farmacia />
            <Nav />
            <br>
            <paginacionProductos />
            <br>
            <br><br><br><br>
        </div>
        <Footer />
        </div>
    
</template>
<script>
    import paginacionProductos from './PaginacionProductos.vue'
    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Footer from './../principales/Footer'
    export default {
        components:{
            Farmacia,
            Nav,
            paginacionProductos,
            Footer
        }
        
    }
</script>