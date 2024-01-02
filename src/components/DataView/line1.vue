<template>
    <div class="business-container"> 
      <div class="tabs" id="chart"></div>   
    </div>
  </template>
  
  <script>
  import * as echarts from 'echarts';
  export default {
    name: "line1",
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
        let myChart = echarts.init(document.getElementById('chart'));
        
        // 指定配置和数据
        let option = {
  /*  grid: {
    top: "20%",
    bottom: "12%"
  },*/
  
  //backgroundColor: "rgba(173, 216, 230, 0.5)",
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "shadow",
      label: {
        show: true,
      },
    },
  },
  legend: {
    data: ["气压", "温度", "湿度"],
    top: "2%",
    right: "10",
    textStyle: {
      color: "rgba(250,250,250,0.6)",
      fontSize: 14,
    },
  },
  xAxis: {
    data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"],
    axisLine: {
      show: true, //隐藏X轴轴线
      lineStyle: {
        color: "#26D9FF",
        width: 2,
      },
    },
    axisTick: {
      show: true, //隐藏X轴刻度
    },
    axisLabel: {
      show: true,
      textStyle: {
        color: "rgba(250,250,250,0.6)", //X轴文字颜色
        fontSize: 12,
      },
    },
    splitArea: {
      show: true,
      areaStyle: {
        color: ["rgba(250,250,250,0.1)", "rgba(250,250,250,0)"],
      },
    },
  },
  yAxis: [
    {
      type: "value",
      min:980,
      max:1050,
      /*name: "气压",*/
      nameTextStyle: {
        color: "#ebf8ac",
        fontSize: 8,
      },
      splitLine: {
        show: false,
      },
      axisTick: {
        show: true,
      },
      axisLine: {
        show: true,
        lineStyle: {
          color: "#26D9FF",
          width: 2,
        },
      },
      axisLabel: {
        show: true,
        formatter: "{value}", //右侧Y轴文字显示
        textStyle: {
          color: "rgba(250,250,250,0.6)",
          fontSize: 8,
        },
      },
    },
    {
      type: "value",
      /*name: "湿度",*/

      nameTextStyle: {
        color: "#ebf8ac",
        fontSize: 8,
      },
      position: "right",
      splitLine: {
        show: false,
      },
      axisTick: {
        show: false,
      },
      axisLine: {
        show: false,
      },
      axisLabel: {
        show: true,
        formatter: "{value} ", //右侧Y轴文字显示
        textStyle: {
          color: "rgba(250,250,250,0.6)",
          fontSize: 8,
        },
      },
    },
    {
      type: "value",
      /*name: "温度",*/
      nameTextStyle: {
        color: "#ebf8ac",
        fontSize: 8,
      },
      offset: 26,
      position: "right",
      splitLine: {
        show: false,
      },
      axisTick: {
        show: false,
      },
      axisLine: {
        show: false,
      },
      axisLabel: {
        margin:10,
        show: true,
        formatter: "{value}", //右侧Y轴文字显示
        textStyle: {
          color: "rgba(250,250,250,0.6)",
          fontSize: 8,
        },
      },
    },
  ],
  series: [
    {
      name: "气压",
      type: "line",
      yAxisIndex: 1, //使用的 y 轴的 index，在单个图表实例中存在多个 y轴的时候有用
      smooth: true, //平滑曲线显示
      showAllSymbol: true, //显示所有图形。
      symbol: "circle", //标记的图形为实心圆
      symbolSize: 8, //标记的大小
      itemStyle: {
        //折线拐点标志的样式
        color: "#1045A0",
        borderColor: "#3D7EEB",
        width: 2,
        shadowColor: "#3D7EEB",
        shadowBlur: 4,
      },
      lineStyle: {
        color: "#3D7EEB",
        width: 2,
        shadowColor: "#3D7EEB",
        shadowBlur: 4,
      },
      areaStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: "rgba(61,126,235, 0.5)",
          },
          {
            offset: 1,
            color: "rgba(61,126,235, 0)",
          },
        ]),
      },
      data: [988, 1020, 1001, 990, 1018, 989,1020],
    },
    {
      name: "湿度",
      type: "bar",
      barWidth: 15,
      yAxisIndex: 1,
      itemStyle: {
        normal: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "rgba(61,126,235, 1)",
            },
            {
              offset: 1,
              color: "rgba(61,126,235, 0)",
            },
          ]),
          borderColor: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "rgba(160,196,225, 1)",
            },
            {
              offset: 1,
              color: "rgba(61,126,235, 1)",
            },
          ]),
          borderWidth: 2,
        },
      },
      data: [41, 93, 66, 89, 45, 90,51],
    },
    {
      name: "温度",
      type: "bar",
      barWidth: 15,
      yAxisIndex: 2,
      itemStyle: {
        normal: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "rgba(15,197,243,1)" },
            { offset: 1, color: "rgba(15,197,243,0)" },
          ]),
          borderColor: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "rgba(180,240,255,1)" },
            { offset: 1, color: "rgba(15,197,243,1)" },
          ]),
          borderWidth: 2,
        },
      },
      data: [15, 25, 21, 13, 26, 17,13],
    },
    
  ],
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
    width: auto;
  height: 380px;

  .tabs {
    height: 100%;
  }
}
  </style>