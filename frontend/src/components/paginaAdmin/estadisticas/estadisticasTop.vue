<template>
  <div>
      <br>
      <h4>Top Productos</h4>
      <br>
      <GChart
        :settings="{packages: ['bar']}"    
        :data="chartD"
        :options="chartO"
        :createChart="(el, google) => new google.charts.Bar(el)"
    />
  </div>
</template>

<script>
import axios from 'axios'
import { GChart } from "vue-google-charts";
export default {
    components: {
        GChart
    },
    data() {
        return {
            ventaProductos: [],
            topProducto: [],
            top:[],
            top5: [],
            listaProductos: [],
            chartD: [
                ["Producto", '']
            ],
            chartsL: null
        }
    },
    created(){
        this.cargar(),
        this.cargarProductos()
    },
    computed:{  
        chartO () {
            this.obtenerTop();
            this.formarData();
            if (!this.chartsL) return null
            return this.chartsL.charts.Bar.convertOptions({
                chart: {
                    title: '\n',

                },
                width: 600,
                fillOpacity: 0.3,
                //bars: 'horizontal', // Required for Material Bar Charts.
                hAxis: { format: 'decimal' },
                height: 450,
                colors: ['#7570b3']
            })
        }
    },
    methods:{
        async cargarProductos(){
            try {
                const response = await axios.get('http://localhost:8000/productos/')
                this.listaProductos = response.data;
                console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        async cargar () {
            try {
                const response = await axios.get('http://localhost:8000/ventaProductos/')
                this.ventaProductos = response.data;
                console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        obtenerTop(){
            this.topProducto=[]
            this.top=[]
            this.top5 =[]
            var ventasP = this.ventaProductos;
            for(var i=0; i < ventasP.length; i++){
                var idProducto = ventasP[i].idProducto;
                var cant = ventasP[i].cantidad;
                if(idProducto in this.topProducto){
                    this.topProducto[idProducto].valor +=cant ;
                }
                else{
                    var data1 = {id: idProducto, valor: cant}
                    this.topProducto[idProducto] = data1;
                }
            }
            for(var j =0; j<this.topProducto.length; j++){
                this.top.push(this.topProducto[j])
            }
            this.top = this.top.slice(1,)
            this.top.sort(function (a, b){
                return (b.valor- a.valor)
            })
            this.top5 = this.top.slice(0,5)
            console.log(this.top5)
            
        },
        
        formarData(){
            //this.chartData = this.chartData.splice(1,)
            for(var w=0; w<this.listaProductos.length; w++){
                var idProd = this.listaProductos[w].idProducto;
                var nombre = this.listaProductos[w].nombreComercial
                for(var x=0; x<this.top5.length; x++){
                    if(idProd == this.top5[x].id){
                        //var dat = [nombre, this.top5[x].valor]
                        this.chartD.push([nombre, this.top5[x].valor])
                    }
                }
            }
            console.log(this.chartData)
        }
    }
}
</script>

<style>

</style>