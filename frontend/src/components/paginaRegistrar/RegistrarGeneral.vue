<template>
  <div class = 'layout'>
        <Farmacia />
        <Nav />
        <br>
        <Stepper />
        <br>
        <br>
        <Footer />
  </div>
</template>

<script>

    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Stepper from './stepperRegistrar.vue'
    import Footer from './../principales/Footer.vue'
 
    export default {
        name: 'RegistrarGeneral',
        components: {
            Farmacia,
            Nav,
            Stepper,
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