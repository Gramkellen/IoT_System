<script>
import * as echarts from 'echarts';

export default {
  name: 'subscribe',
  data() {
    return {
      user: "",       //用户

      theme: [],      //订阅主题
      options: [      //主题选项
        {
          value: 0,
          label: '温度(temperature)',
        },
        {
          value: 1,
          label: '湿度(humidity)',
        },
        {
          value: 2,
          label: '气压(pressure)',
        },
      ], 
      
      activeNames:[],   //打开的折叠面板
      details:[         //已订阅主题的信息
        {
          is_show: false,
          show_chart: false,
          label: '温度(temperature)',
          data: [],
          chart:{       //图表
            date: 0,    //选择的日期
            options:[],  //选项
          },
        },
        {
          is_show: false,
          show_chart: false,
          label: '湿度(humidity)',
          data: [],
          chart:{       //图表
            date: 0,    //选择的日期
            options:[],  //选项
          },
        },
        {
          is_show: false,
          show_chart: false,
          label: '气压(pressure)',
          data: [],
          chart:{       //图表
            date: 0,    //选择的日期
            options:[],  //选项
          },
        },
      ],

      myChart: null,
    }
  },
  methods: {
    disabledDate(time) {
      var that = this;
      var item = that.details[that.activeNames];

      var enable_times = item.chart.options.map(date => new Date(date).getTime());
      return !enable_times.includes(time.getTime());
      //return time.getTime() > Date.now();
    },
    dataProcessing(item){
      // 获取对象的键，并按时间排序
      var labels = Object.keys(item).sort();
      // 根据排序后的键，获取对应的值
      var values = labels.map(function(label) {
        return item[label];     //parseFloat(item[label])
      });
      var times = labels.map(function(label) {
        return label.slice(11);
      });
      return {
        labels: labels,
        values: values,
        times: times,
      };
    },
    init(){     //初始化函数
      var that = this;
      that.user = "";             //获取用户信息

      that.theme.push(0);         //预设选项，已订阅的主题
      
      var item = {"2014-02-13T06:20:00": "3.0", "2014-02-13T13:50:00": "7.0", "2014-02-13T06:00:00": "2", "2014-02-13T03:00:00": "3", "2014-02-13T13:00:00": "6", "2014-02-13T18:50:00": "4.0", "2014-02-13T13:20:00": "6.0", "2014-02-13T15:00:00": "6", "2014-02-13T08:50:00": "4.0", "2014-02-13T21:50:00": "4.0", "2014-02-13T08:00:00": "3", "2014-02-13T07:50:00": "3.0", "2014-02-13T08:20:00": "4.0", "2014-02-13T21:20:00": "3.0", "2014-02-13T11:50:00": "6.0", "2014-02-13T11:20:00": "6.0", "2014-02-13T17:50:00": "5.0", "2014-02-13T11:00:00": "6", "2014-02-13T05:50:00": "2.0", "2014-02-13T20:50:00": "3.0", "2014-02-13T20:20:00": "4.0", "2014-02-13T16:00:00": "6", "2014-02-13T23:50:00": "2.0", "2014-02-13T21:00:00": "3", "2014-02-13T07:20:00": "3.0", "2014-02-13T03:20:00": "3.0", "2014-02-13T07:00:00": "3", "2014-02-13T15:50:00": "6.0", "2014-02-13T03:50:00": "2.0", "2014-02-13T04:00:00": "2", "2014-02-13T12:00:00": "6", "2014-02-13T04:20:00": "2.0", "2014-02-13T12:20:00": "6.0", "2014-02-13T12:50:00": "6.0", "2014-02-13T22:50:00": "3.0", "2014-02-13T09:00:00": "4", "2014-02-13T09:20:00": "4.0", "2014-02-13T09:50:00": "4.0", "2014-02-13T18:00:00": "5", "2014-02-13T05:20:00": "2.0", "2014-02-13T15:20:00": "6.0", "2014-02-13T00:50:00": "4.0", "2014-02-13T14:50:00": "7.0", "2014-02-13T00:00:00": "4", "2014-02-13T00:20:00": "4.0", "2014-02-13T06:50:00": "3.0", "2014-02-13T22:00:00": "4", "2014-02-13T18:20:00": "5.0", "2014-02-13T02:50:00": "3.0", "2014-02-13T02:20:00": "3.0", "2014-02-13T04:50:00": "2.0", "2014-02-13T02:00:00": "3", "2014-02-13T23:00:00": "3", "2014-02-13T16:50:00": "5.0", "2014-02-13T19:50:00": "4.0", "2014-02-13T19:20:00": "4.0", "2014-02-13T05:00:00": "2", "2014-02-13T19:00:00": "4", "2014-02-13T23:20:00": "3.0", "2014-02-13T14:20:00": "7.0", "2014-02-13T10:20:00": "5.0", "2014-02-13T10:00:00": "4", "2014-02-13T10:50:00": "5.0", "2014-02-13T17:00:00": "5", "2014-02-13T01:00:00": "4", "2014-02-13T17:20:00": "5.0", "2014-02-13T01:20:00": "4.0", "2014-02-13T01:50:00": "4.0", "2014-02-13T22:20:00": "3.0", "2014-02-13T16:20:00": "6.0"};
      var result = that.dataProcessing(item);
      that.details[0].data.push(
        {
          receive: '2023-12-14-00:00:00',   //接收时间
          time: '2014/02/13',         //如为2014-02-13在限制时间范围时会有bug
          labels:result.labels,       //标签
          values:result.values,       //数值
          times: result.times,        //标签提取出时间
        },
        {
          receive: '2023-12-14-00:00:10',   //接收时间
          time: '2014/02/14',         //如为2014-02-13在限制时间范围时会有bug
          labels:result.labels,       //标签
          values:result.values,       //数值
          times: result.times,        //标签提取出时间
        },
        {
          receive: '2023-12-14-00:00:50',   //接收时间
          time: '2014/02/15',         //如为2014-02-13在限制时间范围时会有bug
          labels:result.labels,       //标签
          values:result.values,       //数值
          times: result.times,        //标签提取出时间
        },
      );
      that.details[0].is_show = true;
      
      for(var i=0; i<3; i++)
        that.updateDate(i);
    },
    handleClick_subscribe(){      //订阅
      var that = this;
      for(var i = 0; i < 3; i++){       //取消订阅
        if(that.details[i].is_show && !that.theme.includes(i)){
          that.details[i].data = [];
          that.details[i].is_show = false;
          if(that.activeNames === i){
            that.activeNames = [];
          }
        }
      }
      for(var i = 0; i < that.theme.length; i++){   //新订阅
        var index = that.theme[i];
        if(!that.details[index].is_show){
          var item = {"2014-02-13T06:20:00": "3.0", "2014-02-13T13:50:00": "7.0", "2014-02-13T06:00:00": "2", "2014-02-13T03:00:00": "3", "2014-02-13T13:00:00": "6", "2014-02-13T18:50:00": "4.0", "2014-02-13T13:20:00": "6.0", "2014-02-13T15:00:00": "6", "2014-02-13T08:50:00": "4.0", "2014-02-13T21:50:00": "4.0", "2014-02-13T08:00:00": "3", "2014-02-13T07:50:00": "3.0", "2014-02-13T08:20:00": "4.0", "2014-02-13T21:20:00": "3.0", "2014-02-13T11:50:00": "6.0", "2014-02-13T11:20:00": "6.0", "2014-02-13T17:50:00": "5.0", "2014-02-13T11:00:00": "6", "2014-02-13T05:50:00": "2.0", "2014-02-13T20:50:00": "3.0", "2014-02-13T20:20:00": "4.0", "2014-02-13T16:00:00": "6", "2014-02-13T23:50:00": "2.0", "2014-02-13T21:00:00": "3", "2014-02-13T07:20:00": "3.0", "2014-02-13T03:20:00": "3.0", "2014-02-13T07:00:00": "3", "2014-02-13T15:50:00": "6.0", "2014-02-13T03:50:00": "2.0", "2014-02-13T04:00:00": "2", "2014-02-13T12:00:00": "6", "2014-02-13T04:20:00": "2.0", "2014-02-13T12:20:00": "6.0", "2014-02-13T12:50:00": "6.0", "2014-02-13T22:50:00": "3.0", "2014-02-13T09:00:00": "4", "2014-02-13T09:20:00": "4.0", "2014-02-13T09:50:00": "4.0", "2014-02-13T18:00:00": "5", "2014-02-13T05:20:00": "2.0", "2014-02-13T15:20:00": "6.0", "2014-02-13T00:50:00": "4.0", "2014-02-13T14:50:00": "7.0", "2014-02-13T00:00:00": "4", "2014-02-13T00:20:00": "4.0", "2014-02-13T06:50:00": "3.0", "2014-02-13T22:00:00": "4", "2014-02-13T18:20:00": "5.0", "2014-02-13T02:50:00": "3.0", "2014-02-13T02:20:00": "3.0", "2014-02-13T04:50:00": "2.0", "2014-02-13T02:00:00": "3", "2014-02-13T23:00:00": "3", "2014-02-13T16:50:00": "5.0", "2014-02-13T19:50:00": "4.0", "2014-02-13T19:20:00": "4.0", "2014-02-13T05:00:00": "2", "2014-02-13T19:00:00": "4", "2014-02-13T23:20:00": "3.0", "2014-02-13T14:20:00": "7.0", "2014-02-13T10:20:00": "5.0", "2014-02-13T10:00:00": "4", "2014-02-13T10:50:00": "5.0", "2014-02-13T17:00:00": "5", "2014-02-13T01:00:00": "4", "2014-02-13T17:20:00": "5.0", "2014-02-13T01:20:00": "4.0", "2014-02-13T01:50:00": "4.0", "2014-02-13T22:20:00": "3.0", "2014-02-13T16:20:00": "6.0"};
          var result = that.dataProcessing(item);
          that.details[index].data.push(
            {
              receive: '2023-12-14-00:00:30',   //接收时间
              time: '2014/02/13',         //如为2014-02-13在限制时间范围时会有bug
              labels:result.labels,       //横轴标签
              values:result.values,       //数值
              times: result.times,        //标签提取出时间
            }
          );
          that.details[index].is_show = true;          
        }
      }
      for(var i=0; i<3; i++)
        that.updateDate(i);
      //alert(that.details[0].data[0].labels);
      //alert('theme:' + that.theme);
      //alert(that.details[0].is_show);
      //alert(that.details[1].is_show);
      //alert(that.details[2].is_show);
    },
    handleClick_draw(index){           //生成图像
      var that = this;
      that.details[index].show_chart = !that.details[index].show_chart;     //显示图像/隐藏图像切换

      for(var i=0; i<3; i++){           //确保一次只有一个子面板生成图像
        if(index != i){
          that.details[i].show_chart = false;
        }
      }
      
      if(that.details[index].show_chart){
        that.$nextTick(() => {
          that.myChart = this.$echarts.init(document.getElementById("myChart"));
          that.updateChart();
        });
      }
    },
    updateDate(index){            //更新日期选项
      var that = this;
      var dates = [];
      var item = that.details[index];
      for(var i = 0; i < item.data.length; i++){
        dates.push(item.data[i].time);
      }
      item.chart.date = dates[0];
      item.chart.options = dates;
    },
    updateChart() {
      //alert(this.activeNames);
      var that = this;
      var y_name = '';
      var x_data = [];
      var y_data = [];
      var item = that.details[that.activeNames];
      var index = item.chart.options.indexOf(item.chart.date);
      x_data = item.data[index].times;
      y_data = item.data[index].values;
      if(that.activeNames === 0){
        y_name = '℃(摄氏度)';
      }
      else if(that.activeNames === 1){
        y_name = 'RH(相对湿度%)';
      }
      else{
        y_name = 'hPa(百帕)';
      }
      const option = {
        xAxis: {
          type: 'category',
          data: x_data,
        },
        yAxis: {
          type: 'value',
          name: y_name,
        },
        series: [{
          data: y_data,
          type: 'line',
        }]
      };
      that.myChart.setOption(option);
    },
  },
  created() {
    this.init();
  },
  mounted() {
    
  },
}
</script>

<template>
  <div class="sub_wrapper">
    <el-row style="margin-top: 2%;">
      订阅主题：
      <el-select
        v-model="theme"
        multiple
        placeholder="Please select"
        style="width: 45vw"
      >
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        />
      </el-select>
      <el-button @click="handleClick_subscribe">
        确定
      </el-button>
    </el-row>
    <el-row>
      已订阅：
    </el-row>
    <el-row>
      <el-collapse v-model="activeNames" style="width: 80vw;" accordion>
        <el-collapse-item 
          v-for="(item, index) in details"
          :key="index"
          :title="item.label" 
          :name="index"
          :disabled="!item.is_show">
          <el-card>
            <el-row>
              接收信息：
            </el-row>

            <div v-if="!item.show_chart">
              <el-scrollbar  height="60vh">
                <el-row class="message">
                  <el-col :span="12" v-for="(data, index2) in item.data" :key="index2">
                    <el-row>{{ data.receive }}</el-row>
                    <el-row> { </el-row>
                    <el-row v-for="(label, index3) in data.labels" :key="index3">
                      &emsp;{{ label }} &emsp; : &emsp; {{ data.values[index3] }}
                    </el-row>            
                    <el-row> } </el-row>
                    <el-row><br></el-row>
                  </el-col>
                </el-row>
              </el-scrollbar>
            </div>

            <div v-else>
              <el-row class="message">
                <el-col :span="8">
                  <el-scrollbar  height="60vh">
                      <el-col v-for="(data, index2) in item.data" :key="index2">
                      <el-row>{{ data.receive }}</el-row>
                      <el-row> { </el-row>
                      <el-row v-for="(label, index3) in data.labels" :key="index3">
                        &emsp;{{ label }} &emsp; : &emsp; {{ data.values[index3] }}
                      </el-row>            
                      <el-row> } </el-row>
                      <el-row><br></el-row>
                    </el-col>
                  </el-scrollbar>
                </el-col>
                <el-col :span="16">
                  <el-row>
                      <el-date-picker
                        v-model="item.chart.date"
                        type="date"
                        placeholder="选择日期"
                        format="YYYY/MM/DD"
                        value-format="YYYY/MM/DD"
                        :disabled-date="disabledDate"
                        @change="updateChart"
                      />
                  </el-row>
                  <el-row>
                    <div id="myChart" ref="chart" style="width: 600px;height:400px;"></div>
                  </el-row>
                </el-col>
              </el-row>
            </div>

            <el-row style="margin-top: 2%;">
              <el-button @click="handleClick_draw(index)">
                <a v-if="!item.show_chart">生成图像</a>
                <a v-else>隐藏图像</a>
              </el-button>
            </el-row>
          </el-card>
        </el-collapse-item>
      </el-collapse>
    </el-row>
  </div>
</template>

<style>
.sub_wrapper{
  margin-left: 5%;
  line-height: 3.5vh;
}
.message{

}
</style>