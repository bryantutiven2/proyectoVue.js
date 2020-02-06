<template>
    <div>
        <aside class="menu-sidebar d-none d-lg-block">
            <div class="logo">
                <a href="#">
                    <img src="./../../assets/img/bienvenido.png" alt="Bienvenido" />
                </a>
            </div>
            <div class="menu-sidebar__content js-scrollbar1" id="panelCliente">
                <nav class="navbar-sidebar" >
                    <ul class="list-unstyled navbar__list">
                        <li>
                            <router-link class="nav-link text-uppercase text-expanded " :to="{name:'perfilCliente', params:this.idUser}" ><i class="fas fa-table"></i>Perfil</router-link>
                            
                        </li>
                        <li>
                            <router-link class="nav-link text-uppercase text-expanded " :to="{name:'estadisticasCliente', params:this.idUser}"><i class="fas fa-chart-bar"></i>Estadisticas</router-link>
                           
                        </li>
                        
                        <li>
                            <router-link class="nav-link text-uppercase text-expanded " :to="{name:'compraCliente', params:this.idUser}"><i class="fab fa-product-hunt"></i>Compras</router-link>
                        
                        </li>
                        
                    </ul>
                </nav>
            </div>
        </aside>
        <div id="userMagic" >
            <!-- HEADER DESKTOP-->
            <header class="header-desktop">
                <div class="section__content section__content--p30">
                    <div class="container-fluid">
                        <div class="header-wrap">
                            <form class="form-header" action="" method="POST">
                                
                            </form>
                            <div class="header-button">
                                <div class="account-wrap">
                                    <div class="account-item clearfix js-item-menu">
                                        <div class="image">
                                            <img src="./../../assets/img/user.png" alt="usuario" />
                                        </div>
                                        <div class="content">
                                            <h4>@{{this.idUser}}</h4>
                                            <button v-on:click="di('Cerraste sesión')"><i class="fas fa-sign-out-alt" ></i>Cerrar Sesión</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        </div>
    </div>
</template>

<script>
    //const $ = require('jquery')  
    //window.$ = $
    export default {
        data(){
            return{
                idUser: this.$route.params.idUser,
                usuarios:[]
            }
        },
        methods:{            
            di: function (mensaje) {
                alert(mensaje)
                this.$router.push("/iniciarSesion")
                localStorage.removeItem("user") 
                localStorage.removeItem("clave") 
            }
        }
    }
</script>

<style>
    #userMagic{
        text-align: right;
    }
    #panelCliente{
        background-color: #9ae5ff;
    }
</style>