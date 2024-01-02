<template>
    <div class="business-container"> 
      <div class="tabs" id="chart_left2"></div>   
    </div>
  </template>
  
  <script>
  import * as echarts from 'echarts';
  export default {
    name: "temp",
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
        let myChart = echarts.init(document.getElementById('chart_left2'));
        // 指定配置和数据
        let option = {
    
    legend: {
          top: "20",
          x: "center",
          textStyle: {
            fontSize: 14,
            color: "rgba(101, 213, 255, 1)"
          },
          icon:
            "path://M512 881.777778 512 881.777778C716.222629 881.777778 881.777778 716.222629 881.777778 512 881.777778 307.777371 716.222629 142.222222 512 142.222222 307.777373 142.222222 142.222222 307.777371 142.222222 512 142.222222 716.222629 307.777373 881.777778 512 881.777778L512 881.777778ZM512 1024 512 1024C229.230208 1024 0 794.769789 0 512 0 229.230211 229.230208 0 512 0 794.769789 0 1024 229.230211 1024 512 1024 794.769789 794.769789 1024 512 1024L512 1024Z",
          itemWidth:9, // 设置宽度
          itemHeight:8, // 设置高度
          itemGap: 10 // 设置间距
        },
        tooltip: {
          show: true,
          trigger: "axis", //axis , item
          backgroundColor: "RGBA(0, 49, 85, 1)",
          borderColor: "rgba(0, 151, 251, 1)",
          borderWidth: 1,
          borderRadius: 0,
          textStyle: {
            color: "#BCE9FC",
            fontSize: 16,
            align: "left"
          }
        },
        grid: {
          right: "5%",
          top: "20%",
          left: "5%",
          bottom: "5%",
          containLabel: true
        },
        xAxis: {
          type: "category",
          boundaryGap: true,
          data: ["Mon","Tue",'Wed','Thu','Fri','Sat','Sun'],
          axisLabel: {
            //坐标轴刻度标签的相关设置。
            interval: 0, //设置为 1，表示『隔一个标签显示一个标签』
            //	margin:15,
            textStyle: {
                color: "#FFF",
                fontStyle: "normal",
                fontSize: 12
            }
          },
          axisTick: {
            //坐标轴刻度相关设置。
            show: false
          },
          axisLine: {
            //坐标轴轴线相关设置
            lineStyle: {
              color: "rgba(77, 128, 254, 0.2)"
            }
          },
          splitLine: {
            //坐标轴在 grid 区域中的分隔线。
            show: true,
            lineStyle: {
              color: "rgba(77, 128, 254, 0.2)"
            }
          }
        },
        yAxis: [
          {
            type: "value",
            splitNumber: 3,
            axisLabel: {
              textStyle: {
                color: "#FFF",
                fontStyle: "normal",
                fontSize: 12
              }
            },
            axisLine: {
              show: false
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: true,
              lineStyle: {
                color: "rgba(77, 128, 254, 0.2)"
              }
            }
          }
        ],
        series: [
            {
          name: '最高温度',
          type: "pictorialBar",
          barWidth: "60%",
          stack: "总量",
          label: {
            normal: {
              show: false
            }
          },
          itemStyle: {
            normal: {
              color: {
                type: "linear",
                x: 0,
                y: 0,
                x2: 0,
                y2: 1,
                colorStops: [
                  {
                    offset: 0,
                    color: "rgba(0, 151, 251, 1)" // 0% 处的颜色
                  },
                  {
                    offset: 1,
                    color: "rgba(0, 34, 66, 0.2)" // 100% 处的颜色
                  }
                ],
                globalCoord: false // 缺省为 false
              } //渐变颜色
            }
          },
          symbol:
            "path://M12.000,-0.000 C12.000,-0.000 16.074,60.121 22.731,60.121 C26.173,60.121 -3.234,60.121 0.511,60.121 C7.072,60.121 12.000,-0.000 12.000,-0.000 Z",
 
          data: [23,25,24,19,17,23,28]
        },  {
          name: '最低温度',
          type: "pictorialBar",
          barWidth: "60%",
          stack: "总量",
          label: {
            normal: {
              show: false
            }
          },
          itemStyle: {
            normal: {
              color: {
                type: "linear",
                x: 0,
                y: 0,
                x2: 0,
                y2: 1,
                colorStops: [
                  {
                    offset: 0,
                    color: "rgba(48, 236, 166, 1)" // 0% 处的颜色
                  },
                  {
                    offset: 1,
                    color: "rgba(0, 34, 66, 0.2)" // 100% 处的颜色
                  }
                ],
                globalCoord: false // 缺省为 false
              } //渐变颜色
            }
          },
          symbol:
            "path://M12.000,-0.000 C12.000,-0.000 16.074,60.121 22.731,60.121 C26.173,60.121 -3.234,60.121 0.511,60.121 C7.072,60.121 12.000,-0.000 12.000,-0.000 Z",
 
          data: [13,11,15,12,14,18,11]
        }],
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
    height: 4.5rem;
    margin-top: -8%;
  }
}
  </style>