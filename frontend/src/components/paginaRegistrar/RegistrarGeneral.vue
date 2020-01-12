<template>
  <div class = 'layout'>
        <Farmacia />
        <Nav />
        <br>
        <Footer />
  </div>
</template>

<script>

    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Footer from './../principales/Footer.vue'
 
    export default {
        name: 'RegistrarGeneral',
        components: {
            Farmacia,
            Nav,
            Footer
        },
        data(){
            return {
                
            }
        },
        methods: {
            
        }
    }
</script>

<style>
    .layout {
    display: flex;
    flex-direction: column;
    }
</style>