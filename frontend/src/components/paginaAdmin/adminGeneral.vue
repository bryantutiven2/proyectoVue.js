<template>
    <div>
        <aside class="menu-sidebar d-none d-lg-block">
            <div class="logo">
                <a href="#">
                    <img src="./../../assets/img/logo.png" alt="Cool Admin" />
                </a>
            </div>
            <div class="menu-sidebar__content js-scrollbar1">
                <nav class="navbar-sidebar">
                    <ul class="list-unstyled navbar__list">
                        <li>
                            <router-link class="nav-link text-uppercase text-expanded " to='/ventasAdmin'><i class="fas fa-table"></i>Ventas</router-link>
                            
                        </li>
                        <li>
                            <router-link class="nav-link text-uppercase text-expanded " to='/estadisticasAdmin'><i class="fas fa-chart-bar"></i>Estadisticas</router-link>
                           
                        </li>
                        
                        <li>
                            <router-link class="nav-link text-uppercase text-expanded " to='/productosAdmin'><i class="fab fa-product-hunt"></i>Productos</router-link>
                        
                        </li>
                        <li>
                            <router-link class="nav-link text-uppercase text-expanded " to='/clienteAdmin'><i class="fas fa-users"></i>Cliente</router-link>
                        
                        </li>
                        <li>
                            <router-link class="nav-link text-uppercase text-expanded " to='/reporteAdmin'><i class="fas fa-users"></i>Reporte</router-link>
                        
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
                                            <h4>Magic Pills</h4>
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
    export default {

    }
</script>

<style>
    #userMagic{
        text-align: right;
    }
</style>