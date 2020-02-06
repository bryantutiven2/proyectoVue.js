<template>
  <div>
      <br>
      <h4>Venta de medicamentos genericos</h4>
      <br>
      <GChart      
      type="BubbleChart"
      :data="chartData"
      :options="chartOptions"
      style="width: 900px; height: 500px;"
    />
  
  </div>
</template>
<script>
import { GChart } from "vue-google-charts";
export default {
  name: "App",
  components: {
    GChart
  },
  data() {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        ["ID", "Dias", "Precio", "Ventas"],
        ["Acido clavulanico", 40, 0.50, 120],
        ["Paracetamol", 30, 0.30, 130],
        ["Acetominofen", 15, 0.25, 50],
        ["Levoceterizna", 20, 0.50, 230],
        ["Amoxicilina", 35, 1.30, 210],
        ["Montelukast", 10, 1.1, 100],
        ["Ibuprofeno", 7, 1.22, 80]
      ],
      chartOptions: {
        colorAxis: { colors: ["yellow", "red"] }
      }
    };
  }
};
</script>
