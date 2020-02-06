<template>
  <div>
      <br>
       <h4>Ventas Realizadas por Mes</h4>
        <br>
        <GChart
            :settings="{packages: ['bar']}"    
            :data="chartData"
            :options="chartOptions"
            :createChart="(el, google) => new google.charts.Bar(el)"
            @ready="onChartReady"
        />
  </div>
</template>

<script>
import axios from 'axios'
import { GChart } from 'vue-google-charts'
export default {
    components:{
        GChart
    },
    data(){
        return{
            chartsLib: null,
            pagos:[],
            chartData: [
                ['\n', ''],
                ['Ene',0],
                ['Feb',0],
                ['Mar',0],
                ['Abr',0],
                ['May',0],
                ['Jun',0],
                ['Jul',0],
                ['Ago',0],
                ['Sep',0],
                ['Oct',0],
                ['Nov',0],
                ['Dic',0],
            ]
        }
    },
    created(){
        this.cargar()
    },
    computed:{
        chartOptions () {
            this.ventasPorMes();
            if (!this.chartsLib) return null
            return this.chartsLib.charts.Bar.convertOptions({
                chart: {
                    title: '\n',

                },
                width: 700,
                fillOpacity: 0.3,
                bars: 'horizontal', // Required for Material Bar Charts.
                hAxis: { format: 'decimal' },
                height: 450,
                colors: ['#1b9e77']
            })
        }
    },
    methods:{
        onChartReady (chart, google) {
            this.chartsLib = google
        },
        async cargar () {
            try {
                const response = await axios.get('http://localhost:8000/pagos/')
                this.pagos=response.data;
                console.log(response.data);
            }
            catch(e){
                console.log(e)
            }
        },
        ventasPorMes(){
            var pagos = this.pagos
            for(var i=0; i<pagos.length; i++){
                var splitMes = pagos[i].fechaHora.split("-");
                var digitoMes = splitMes[1];
                if(digitoMes=='01'){
                    this.chartData[1][1]+=1;
                }
                else if(digitoMes=='02'){
                    this.chartData[2][1]+=1;
                }
                else if(digitoMes=='03'){
                    this.chartData[3][1]+=1;
                }
                else if(digitoMes=='04'){
                    this.chartData[4][1]+=1;
                }
                else if(digitoMes=='05'){
                    this.chartData[5][1]+=1;
                }
                else if(digitoMes=='06'){
                    this.chartData[6][1]+=1;
                }
                else if(digitoMes=='07'){
                    this.chartData[7][1]+=1;
                }
                else if(digitoMes=='08'){
                    this.chartData[8][1]+=1;
                }
                else if(digitoMes=='09'){
                    this.chartData[1][8]+=1;
                }
                else if(digitoMes=='10'){
                    this.chartData[10][1]+=1;
                }
                else if(digitoMes=='11'){
                    this.chartData[11][1]+=1;
                }
                else if(digitoMes=='12'){
                    this.chartData[12][1]+=1;
                }
            }
            console.log(this.chartData)
        }
    },
    mounted(){
        
    }
}
</script>

<style scoped>
</style>