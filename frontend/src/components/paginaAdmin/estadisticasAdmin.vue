<template>
    <div class="page-wrapper">
        <adminGeneral />
        <div class="page-container">
            <div class="main-content">
                <!-- Aqui va el contenido-->
                <div class="section__content section__content--p30">
                        <div class="container-fluid">
                            <div class="row">
                                <div class="col-md-12">
                                    <h1 id="tituloP">Mis Estadisticas</h1>
                                    <br>
                                    <div id= "conte1">
                                        <div>
                                            <estadisticaPago />
                                        </div>
                                        
                                    </div>
                                    <br>
                                    <div id= "conte2">
                                          <estadisitcaTop />      
                                    </div>
                                </div>
                            </div>
                        </div>
                </div>
                
            </div>
        </div>
    </div>
</template>

<script>
import estadisticaPago from './estadisticas/estadisitcaPagos'
import estadisitcaTop from './estadisticas/estadisticasTop'
import adminGeneral from './adminGeneral'
export default {
    components:{
        adminGeneral,
        estadisticaPago,
        estadisitcaTop
    }
}
</script>

<style scoped>
    #tituloP{
        text-align: center;
        font-weight: bold;
    }
    #botones{
        display: grid;
        grid-template-columns: repeat(3,1fr);
        grid-gap: 60px;
    }
    #conte1{
        width: 700px;
        display: table;
        margin: 0 auto;
    }
    #conte2{
        width: 700px;
        display: table;
        margin: 0 auto;
    }
</style>