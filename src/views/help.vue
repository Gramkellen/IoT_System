<script>
import * as echarts from 'echarts';
import axios  from "axios";
export default {
  name: 'help',
  data(){
    return{
      ip:'100.80.222.123',
    };
  },
  components:{
    data_t:{},    //温度
    data_h:{},    //湿度
    data_p:{},    //气压
    myChart_t: null,
    myChart_h: null,
    myChart_p: null,
    temperature:{},
    humidity:{},
    pressure:{},
  },
  methods: {
    init(){
      var that = this;
    axios.get('http://'+that.ip+':8000/analysis?type=temperature').then(res =>{
        that.data_t = res.data;
        //console.log(that.data_t);
        var result = that.dataProcessing(that.data_t);
        that.temperature={
          time: result.time,          //如为2014-02-13在限制时间范围时会有bug
          labels:result.labels,       //横轴标签
          values:result.values,       //数值
          times: result.times,        //标签提取出时间
        };

        that.$nextTick(() => {
          that.myChart_t = this.$echarts.init(document.getElementById("myChart_t"));
          that.updateChart(0);
        });

      });
      //axios.get('http://100.78.169.243:8000/analysis?type=temperature').then(res =>{
    axios.get('http://'+that.ip+':8000/analysis?type=humidity').then(res =>{
        that.data_h = res.data;
        //console.log(that.data_h);
        var result = that.dataProcessing(that.data_h);
        that.humidity={
          time: result.time,          //如为2014-02-13在限制时间范围时会有bug
          labels:result.labels,       //横轴标签
          values:result.values,       //数值
          times: result.times,        //标签提取出时间
        };
        that.$nextTick(() => {
          that.myChart_h = this.$echarts.init(document.getElementById("myChart_h"));
          that.updateChart(1);
        });
      });
      //axios.get('http://100.78.169.243:8000/analysis?type=temperature').then(res =>{
    axios.get('http://'+that.ip+':8000/analysis?type=pressure').then(res =>{
        that.data_p = res.data;
        //console.log(that.data_p);
        var result = that.dataProcessing(that.data_p);
        that.pressure={
          time: result.time,          //如为2014-02-13在限制时间范围时会有bug
          labels:result.labels,       //横轴标签
          values:result.values,       //数值
          times: result.times,        //标签提取出时间
        };
        that.$nextTick(() => {
          that.myChart_p = this.$echarts.init(document.getElementById("myChart_p"));
          that.updateChart(2);
        });
      });
    
    },
    dataProcessing(item){
      //var result = that.dataProcessing(item);
      // 获取对象的键，并按时间排序
      var labels = Object.keys(item).sort();
      // 根据排序后的键，获取对应的值
      var values = labels.map(function(label) {
        return item[label];     //parseFloat(item[label])
      });
      var times = labels.map(function(label) {
        return label.slice(11);
      });
      var time = labels[0].split("T")[0];
      return {
        time:time.replace(/-/g,'/'),
        labels: labels,
        values: values,
        times: times,
      };
    },
    updateChart(state) {               //更新图像
      //alert(this.activeNames);
      var that = this;
      var y_name = '';
      var x_data = [];
      var y_data = [];
      var item;
      var bar_color='#1CFEF0';
      if(state === 0){
        item = that.temperature;
        y_name = '℃(摄氏度)';
        bar_color='#F1FFB8';
      }
      else if(state === 1){
        item = that.humidity;
        y_name = 'RH(相对湿度%)';
      }
      else{
        item = that.pressure;
        y_name = 'hPa(百帕)';
        bar_color='#8CFF8A';
      }
      x_data = item.labels;
      y_data = item.values;      
      const option = {
        xAxis: {
          type: 'category',
          data: x_data,
          axisLine: {
            lineStyle: {
              color: 'white'  // 这里设置x轴颜色
            }
          },
          axisLabel: {
            color: 'white'  // 这里设置x轴文字颜色
          },
        },
        yAxis: {
          type: 'value',
          name: y_name,
          axisLine: {
            lineStyle: {
              color: 'white'  // 这里设置y轴颜色
            }
          },
          axisLabel: {
            color: 'white'  // 这里设置y轴文字颜色
          },
        },
        series: [{
          data: y_data,
          type: 'bar',
          smooth: true,
          itemStyle: {
            color: bar_color  // 这里设置线的颜色
          }
        }]
      };
      if(state === 0){
        that.myChart_t.setOption(option);
      }
      else if(state === 1){
        that.myChart_h.setOption(option);
      }
      else{
        that.myChart_p.setOption(option);
      }
    },
  },
  created() {
    var that = this;
    that.init(); 
  },
}
</script>

<template>
  <div>

    <el-card class="topic_bkground">
      <a>温度预测曲线：</a>
      <div id="myChart_t" ref="chart"  style="width: 1100px;height:400px;"></div> 
    </el-card>
    <el-card class="topic_bkground">
      <a>湿度预测曲线：</a>
      <div id="myChart_h" ref="chart"  style="width: 1100px;height:400px;"></div>  
    </el-card>
    <el-card class="topic_bkground">
      <a>气压预测曲线：</a>
      <div id="myChart_p" ref="chart"  style="width: 1100px;height:400px;"></div>   
    </el-card>
    <br>
  </div>
</template>

<style scoped>
.topic_bkground{
  background-color: rgba(103, 122, 223, 0.30);
  color: white;
  margin-left: 1%;
  width:97%;  
}
</style>