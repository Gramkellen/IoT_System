<script scoped>
import * as echarts from 'echarts';
import axios  from "axios";
import mqtt from 'mqtt'
export default {
  name: 'subscribe',
  data() {
    return {
      /* 以下为mqtt相关 */
      connection: {
        protocol: "ws",           //mqtt服务器协议（ws/mqtt）
        //host: "broker.emqx.io",   //mqtt服务器主机名或ip地址
        //port: 8083,               //mqtt服务器端口号
        host: "100.80.222.123",        
        port: 1883,
        endpoint: "/mqtt",        //mqtt服务器端点

        clean: true,
        connectTimeout: 30 * 1000, // ms
        reconnectPeriod: 4000, // ms
        clientId: "emqx_vue_" + Math.random ().toString (16).substring (2, 8),    //客户端id
      },
      subscription: {
        topic: "topic/mqttx",
        qos: 0,                 //服务质量
      },
      publish: {
        topic: "topic/browser",
        qos: 0,
        payload: '{ "msg": "Hello, I am browser." }',     //有效载荷
      },
      receiveNews: "",          //订阅接收到的信息
      qosList: [0, 1, 2],       //mqtt三种服务质量等级
      client: {                 //客户端是否已连接到mqtt服务器
        connected: false,
      },
      subscribeSuccess: false,    //是否成功订阅到主题
      connecting: false,          //是否正在尝试连接到mqtt服务器
      retryTimes: 0,              //尝试重新连接到MQTT服务器的次数  
      
      topics:['temperature','humidity','pressure'],   //可订阅主题

      /* 以下为订阅相关 */
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

      ip:'100.80.222.123',

      myChart: null,
    }
  },
  methods: {
    /* 以下为mqtt相关 */
    initData () {
      this.client = {
        connected: false,
      };
      this.retryTimes = 0;
      this.connecting = false;
      this.subscribeSuccess = false;
    },
    handleOnReConnect () {
      this.retryTimes += 1;
      if (this.retryTimes > 5) {
        try {
          this.client.end ();
          this.initData ();
          this.$message.error ("Connection maxReconnectTimes limit, stop retry");
        } catch (error) {
          this.$message.error (error.toString ());
        }
      }
    },
    createConnection () {
      try {
        this.connecting = true;
        const { protocol, host, port, endpoint, ...options } = this.connection;
        const connectUrl = `${protocol}://${host}:${port}${endpoint}`;
        //const connectUrl = ' http://100.78.169.243:1883/';
        this.client = mqtt.connect (connectUrl, options);
        if (this.client.on) {
          this.client.on ("connect", () => {
            this.connecting = false;
            console.log ("Connection succeeded!");
          });
          this.client.on ("reconnect", this.handleOnReConnect);
          this.client.on ("error", (error) => {
            console.log ("Connection failed", error);
          });
          this.client.on ("message", (topic, message) => {
            this.receiveNews = this.receiveNews.concat (message);
            console.log (`Received message ${message} from topic ${topic}`);
            //alert(`Received message ${message} from topic ${topic}`);
            this.updateDetails(topic, message);
          });
        }
      } catch (error) {
        this.connecting = false;
        console.log ("mqtt.connect error", error);
      }
    },
    subscribeTopic(topic) {
      const qos = this.subscription.qos;
      this.client.subscribe(topic, { qos }, (error) => {
        if (!error) {
          this.subscribeSuccess = true;
          console.log(`Subscribe to topic ${topic} successfully!`);
        } else {
          console.log(`Subscribe to topic ${topic} failed: `, error);
        }
      });
    },
    unsubscribeTopic(topic) {
      this.client.unsubscribe(topic, error => {
        if (!error) {
          console.log(`Unsubscribed from topic ${topic} successfully!`);
        } else {
          console.log(`Unsubscribe from topic ${topic} failed: `, error);
        }
      });
    },
    publishMessage(topic, message) {
      const qos = this.publish.qos;
      this.client.publish(topic, message, { qos }, (error) => {
        if (!error) {
          console.log(`Publish message to topic ${topic} successfully!`);
          //alert(`Published message ${message} to topic ${topic}`);
        } else {
          console.log(`Publish message to topic ${topic} failed: `, error);
        }
      });
    },
    /* 以下为订阅相关 */
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
      var time = labels[0].split("T")[0];
      return {
        time:time.replace(/-/g,'/'),
        labels: labels,
        values: values,
        times: times,
      };
    },
    init(){     //初始化函数-----初始化数据待补充(initial)
      var that = this;
      axios.get('http://'+that.ip+':8000/query_sub?id=1').then(res =>{
        console.log(res.data);
        that.theme = res.data;
        for(var i=0; i<that.theme.length; i++){
          that.details[that.theme[i]].is_show = true;
          that.subscribeTopic(that.topics[that.theme[i]]);
        }
      });
    },
    handleClick_subscribe(){      //订阅-----调用接口上传订阅状态
      var that = this;
      //axios.post('/weathersystem/history/',{
      axios.post('http://'+that.ip+':8000/update_sub/',{      //上传订阅状态
        id:1,       // 用户
        topic:that.theme,     // 已订阅列表数组 例：[0,2] 表示已订阅温度气压，未订阅湿度   0-温度 1-湿度 2-气压
      });   //{id:1,topic:[0,1,2]}
      
      for(var i = 0; i < 3; i++){       //取消订阅
        if(that.details[i].is_show && !that.theme.includes(i)){
          that.details[i].data = [];
          that.details[i].is_show = false;
          if(that.activeNames === i){
            that.activeNames = null;
          }
          this.unsubscribeTopic(that.topics[i]);
        }
      }
      for(var i = 0; i < that.theme.length; i++){   //新订阅
        var index = that.theme[i];
        if(!that.details[index].is_show){
          this.subscribeTopic(that.topics[index]);
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
    updateChart() {               //更新图像
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
          min: 'dataMin', // 最小值
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
          type: 'line',
          smooth: true,
          itemStyle: {
            color: '#1CFEF0'  // 这里设置线的颜色
          }
        }]
      };
      that.myChart.setOption(option);
    },
    updateDetails(topic, message){       //更新已订阅信息-----调用接口传历史记录
      var that = this;
      var jsonObject = JSON.parse(message);           //string转json
      var result = that.dataProcessing(jsonObject);   //数据处理
      var index = that.topics.indexOf(topic);         //订阅主题
      var item = that.details[index];                 
      if(!item.chart.options.includes(result.time)){  //忽略重复日期
        var receivetime = new Date();
        that.details[index].data.push(
          {
            receive: receivetime.toLocaleString(),   //接收时间
            time: result.time,          //如为2014-02-13在限制时间范围时会有bug
            labels:result.labels,       //横轴标签
            values:result.values,       //数值
            times: result.times,        //标签提取出时间
          }
        );
        that.updateDate(index);         //更新日期
      }
    },

    /* 以下为测试相关 */
    test_1(topic){
      var tmp = {"2014-02-13T06:20:00": "3.0", "2014-02-13T13:50:00": "7.0", "2014-02-13T06:00:00": "2", "2014-02-13T03:00:00": "3", "2014-02-13T13:00:00": "6", "2014-02-13T18:50:00": "4.0", "2014-02-13T13:20:00": "6.0", "2014-02-13T15:00:00": "6", "2014-02-13T08:50:00": "4.0", "2014-02-13T21:50:00": "4.0", "2014-02-13T08:00:00": "3", "2014-02-13T07:50:00": "3.0", "2014-02-13T08:20:00": "4.0", "2014-02-13T21:20:00": "3.0", "2014-02-13T11:50:00": "6.0", "2014-02-13T11:20:00": "6.0", "2014-02-13T17:50:00": "5.0", "2014-02-13T11:00:00": "6", "2014-02-13T05:50:00": "2.0", "2014-02-13T20:50:00": "3.0", "2014-02-13T20:20:00": "4.0", "2014-02-13T16:00:00": "6", "2014-02-13T23:50:00": "2.0", "2014-02-13T21:00:00": "3", "2014-02-13T07:20:00": "3.0", "2014-02-13T03:20:00": "3.0", "2014-02-13T07:00:00": "3", "2014-02-13T15:50:00": "6.0", "2014-02-13T03:50:00": "2.0", "2014-02-13T04:00:00": "2", "2014-02-13T12:00:00": "6", "2014-02-13T04:20:00": "2.0", "2014-02-13T12:20:00": "6.0", "2014-02-13T12:50:00": "6.0", "2014-02-13T22:50:00": "3.0", "2014-02-13T09:00:00": "4", "2014-02-13T09:20:00": "4.0", "2014-02-13T09:50:00": "4.0", "2014-02-13T18:00:00": "5", "2014-02-13T05:20:00": "2.0", "2014-02-13T15:20:00": "6.0", "2014-02-13T00:50:00": "4.0", "2014-02-13T14:50:00": "7.0", "2014-02-13T00:00:00": "4", "2014-02-13T00:20:00": "4.0", "2014-02-13T06:50:00": "3.0", "2014-02-13T22:00:00": "4", "2014-02-13T18:20:00": "5.0", "2014-02-13T02:50:00": "3.0", "2014-02-13T02:20:00": "3.0", "2014-02-13T04:50:00": "2.0", "2014-02-13T02:00:00": "3", "2014-02-13T23:00:00": "3", "2014-02-13T16:50:00": "5.0", "2014-02-13T19:50:00": "4.0", "2014-02-13T19:20:00": "4.0", "2014-02-13T05:00:00": "2", "2014-02-13T19:00:00": "4", "2014-02-13T23:20:00": "3.0", "2014-02-13T14:20:00": "7.0", "2014-02-13T10:20:00": "5.0", "2014-02-13T10:00:00": "4", "2014-02-13T10:50:00": "5.0", "2014-02-13T17:00:00": "5", "2014-02-13T01:00:00": "4", "2014-02-13T17:20:00": "5.0", "2014-02-13T01:20:00": "4.0", "2014-02-13T01:50:00": "4.0", "2014-02-13T22:20:00": "3.0", "2014-02-13T16:20:00": "6.0"};
      var jsonString = JSON.stringify(tmp);
      //var jsonObject = JSON.parse(jsonString);
      this.publishMessage(topic, jsonString);
    },
  },
  created() {
    var that = this;
    that.init();                  //初值--用户订阅状态/历史记录
    that.createConnection();      //连接mqtt
    that.client.on("connect", () => {
      for(var i = 0; i < 3; i++){   
        if(that.theme.includes(i)){   //订阅
          this.subscribeTopic(that.topics[i]);
        }
      }
    });
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
      <el-button class='sub_button' @click="handleClick_subscribe">
        确定
      </el-button>
    </el-row>

    <el-row style="margin-top: 2%;" v-if="0">
      测试：
      <el-button class='sub_button' @click="test_1('temperature')">温度</el-button>
      <el-button class='sub_button' @click="test_1('humidity')">湿度</el-button>
      <el-button class='sub_button' @click="test_1('pressure')">气压</el-button>
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
          <el-card class="topic_bkground">
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
              <el-button class='sub_button' @click="handleClick_draw(index)">
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
  width:80%;
  line-height: 3.5vh;
  color: white;
  font-size: 2vh;
}
.sub_button{
  color:white;
  background-color: #5e7dcc;
}
.el-collapse {
  --el-collapse-border-color: #001953;
  --el-collapse-header-bg-color: rgba(62, 75, 144, 0.50);
  --el-collapse-content-bg-color: rgba(62, 75, 144, 0.50);
}
.el-collapse-item__header{
  color:rgb(189, 221, 243);
}
.el-input{
  --el-input-bg-color: rgba(126, 177, 243, 0.5);
}
.topic_bkground{
  background-color: rgba(103, 122, 223, 0.30);
  color: white;
}
</style>