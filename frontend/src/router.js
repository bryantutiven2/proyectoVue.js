import Vue from 'vue'
import Router from 'vue-router'
import Inicio from './views/Inicio.vue'
import Nosotros from './views/Nosotros.vue'
import Noticias from './components/paginaNoticias/NoticiasGeneral.vue'
import Productos from './views/Productos.vue'
import IniciarSesion from './views/IniciarSesion.vue'
import Registrar from './views/Registrar.vue'
import Cliente from './components/paginaCliente/clienteGeneral.vue'
import compraCliente from './components/paginaCliente/compraCliente.vue'
import perfilCliente from './components/paginaCliente/perfilCliente.vue'
import estadisticasCliente from './components/paginaCliente/estadisticasCliente.vue'
import Admin from './components/paginaAdmin/adminGeneral.vue'
import clienteAdmin from './components/paginaAdmin/clienteAdmin.vue'
import estadisticasAdmin from './components/paginaAdmin/estadisticasAdmin.vue'
import productosAdmin from './components/paginaAdmin/productosAdmin.vue'
import reporteAdmin from './components/paginaAdmin/reporteAdmin.vue'
import ventasAdmin from './components/paginaAdmin/ventasAdmin.vue'
Vue.use(Router)



export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'inicio',
            component: Inicio
        },
        {
            path: '/nosotros',
            name: 'nosotros',
            component: Nosotros
        },
        {
            path: '/noticias',
            name: 'noticias',
            component: Noticias
        },
        {
            path: '/productos',
            name: 'productos',
            component: Productos
        },
        {
            path: '/iniciarSesion',
            name: 'IniciarSesion',
            component: IniciarSesion
        },
        {
            path: '/registrar',
            name: 'Registrar',
            component: Registrar
        }
        ,
        {
            path: '/admin',
            name: 'admin',
            component: Admin
        },
        {
            path: '/clienteAdmin',
            name: 'clienteAdmin',
            component: clienteAdmin
        },
        {
            path: '/estadisticasAdmin',
            name: 'estadisitcasAdmin',
            component: estadisticasAdmin
        },
        {
            path: '/productosAdmin',
            name: 'productosAdmin',
            component: productosAdmin
        },
        {
            path: '/reporteAdmin',
            name: 'reporteAdmin',
            component: reporteAdmin
        },
        {
            path: '/ventasAdmin',
            name: 'ventasAdmin',
            component: ventasAdmin
        },
        {
            path: '/clienteGeneral/:idUser',
            name: 'clienteGeneral',
            component: Cliente
        },
        {
            path: '/compraCliente/:idUser',
            name: 'compraCliente',
            component: compraCliente
        },
        {
            path: '/perfilCliente/:idUser',
            name: 'perfilCliente',
            component: perfilCliente
        },
        {
            path: '/estadisticasCliente/:idUser',
            name: 'estadisticasCliente',
            component: estadisticasCliente
        }
    ]
})