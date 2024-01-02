<template>
  <div class="business-container"> 
    <div class="chart" id="chart_left1"></div>   
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "business",
  data() {
    return {
      
    }
  },
  mounted() {
    this.getEchartLeft1();
  },
  methods: {
    getEchartLeft1() {
      // 实例化对象
      let myChart = echarts.init(document.getElementById('chart_left1'));
      let charts = { // 按顺序排列从大到小
        cityList: ['金融行业', '电子政务', '文创版权', '教育行业', '智慧停车', '医疗互联', '物流行业'],
        cityData: [1500, 1200, 900, 600, 400, 300, 100]
      }
      
      let lineY = [];
        let data = [20, 60, 70, 152, 70, 110, 130];
        lineY.push(data) 

      // 指定配置和数据
      let option = {
  
  color: ['blue'],
  textStyle: {
    color: '#fff'
  },
  yAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  xAxis: {
    type: 'value'
  },
  series: [
    {
      data: data,
      type: 'bar',
      barWidth: 20
    },
    {
      type: 'lines',
      coordinateSystem: 'cartesian2d',
      data: data.map((item, index) => {
        return {
          coords: [
            [0, index],
            [item, index]
          ]
        };
      }),
      effect: {
        show: true,
        period: 2.5,
        trailLength: 0.5, //控制拖尾长度
        symbolSize: 20,
        symbol:
          'rect',
        loop: true,
        color: '#fff' //流光颜色
      },
      lineStyle: {
        width: 0,
        opacity: 0.6,
        curveness: 0
      },
      z: 99
    }
  ]
};

      // 把配置给实例对象
      myChart.setOption(option, true);
      window.addEventListener('resize', () => {
        myChart.resize();
      });
    },
  },
  beforeDestroy() {
    
  }
};
</script>

<style lang="scss" scoped>
.business-container {
  .chart {
    height: 4.5rem;
  }
}
</style>