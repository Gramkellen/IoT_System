<template>
  <div class="business-container"> 
    <div class="tabs" id="chartleft1"></div>   
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "stress",
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
      let myChart = echarts.init(document.getElementById('chartleft1'));
      let data = [93, 66, 91, 84, 55, 93, 61];
      // 指定配置和数据
      let option = {
  color: ['rgba(40, 237, 250, .3)'],
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
      barWidth: 20,
      barHeight: 55,
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

.tabs {
  height: 5.5rem;
  margin-top: -18%;
}
}
</style>