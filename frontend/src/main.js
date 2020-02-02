import Vue from 'vue'
import App from './App.vue'
import './assets/css/business-casual.min.css'
import './assets/css/bootstrap.min.css'
import './assets/css/style.css'
import './assets/css/step.css'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueRouter from 'vue-router'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueGoodTablePlugin from 'vue-good-table';
import 'vue-good-table/dist/vue-good-table.css'


Vue.use(VueGoodTablePlugin);
Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
