<template>
    <div class = 'layout'>
        <div>
            <Farmacia />
            <Nav />
            <br>
            <section class="page-section cta">
                <div class="container" id="login">
                    <form id="formulario">
                        <br>
                        <h2>Login</h2>
                        
                        <div class="col-xs-4">
                            <input class="form-control" id="nombre-input" type="text" placeholder="Usuario">
                        </div>
                        <br>
                        <div class="col-xs-4">
                            <input class="form-control" id="pwd-input" type="password" placeholder="Contraseña" >
                        </div>
                        <br>
                        <div id="botonSesion">
                            <input type="button" id="iniciar-sesion" value="Iniciar Sesión" class="btn btn-success btn-sm col-sm-7" >
                        </div>
                    </form>
                </div>
            </section>
        </div>
        
        <Footer />
    </div>
</template>

<script>
    import Farmacia from './../principales/Farmacia.vue'
    import Nav from './../principales/Nav.vue'
    import Footer from './../principales/Footer.vue'
    export default {
        name: 'SesionGeneral',
        components: {
            Farmacia,
            Nav,
            Footer
        }
    }
</script>

<style>
    .layout {
    display: flex;
    flex-direction: column;
    }
    #botonSesion{
        text-align: center;
    }
</style>