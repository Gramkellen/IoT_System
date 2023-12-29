<template>
  <div class="sub_wrapper">
    <el-row style="margin-top: 2%;color: rgb(255, 255, 255);">
      选择主题:
      <div style="margin: 0 5px;"></div>
      <el-select v-model="selectedTopic" clearable placeholder="请选择" style="width: 30%;">
        <el-option v-for="item in topicOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
      </el-select>
      <el-upload
        class="upload-demo"
        :action="uploadUrl"
        :before-upload="beforeUpload"
        :on-change="handleFileChange"
        :file-list="fileList"
        :accept="txt"
      >
      <div style="margin: 0 8px;"></div>
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip el-icon-warning-outline" style="margin-left: 10px; color: #ffffff">只能上传txt文件</div>
      </el-upload>
    </el-row>
      <el-row style="margin-top: 2%;">
  <el-row style="color:#ffffff"> 文件内容：</el-row>
  <el-input
  type="textarea"
  v-model="fileContent"
  :autosize="false"
  :rows="25"
  style="width: 400px; height: 500px;"
  readonly>
</el-input>
</el-row>
</div>
</template>

<script>
import mqtt from 'mqtt'

export default {
  data() {
    return {
      topicOptions: [
        { value: 'temperature', label: '温度(temperature)' },
        { value: 'humidity', label: '湿度(humidity)' },
        { value: 'pressure', label: '气压(pressure)' }
      ],
      connection: {
        protocol: "ws",           //mqtt服务器协议（ws/mqtt）
        host: "100.78.169.243",   //mqtt服务器主机名或ip地址
        port: 1883,               //mqtt服务器端口号
        endpoint: "/mqtt",        //mqtt服务器d端点
        clean: true,
        connectTimeout: 30 * 1000, // ms
        reconnectPeriod: 4000, // ms
      },
      selectedTopic: '',
      fileList: [],
      fileContent: '',
      stringContent: '',
      mqttClient: null,
      isConnected: false,
      publish: {
        topic: "topic/browser",
        qos: 0,
        payload: '{ "msg": "Hello, I am browser." }',     //有效载荷
      },
      
      client: {                 //客户端是否已连接到mqtt服务器
        connected: false,
      },
      
      connecting: false,          //是否正在尝试连接到mqtt服务器
      retryTimes: 0,    
    }
  },
  created() {
    this.createConnection();
  },
  methods: {
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
            alert(`Received message ${message} from topic ${topic}`);
          });
        }
      } catch (error) {
        this.connecting = false;
        console.log ("mqtt.connect error", error);
      }
    },
    publishMessage(topic, message) {
      const qos = this.publish.qos;
      this.client.publish(topic, message, { qos }, (error) => {
        if (!error) {
          console.log(`Publish message to topic ${topic} successfully!`);
          alert(`Published message ${message} to topic ${topic}`);
        } else {
          console.log(`Publish message to topic ${topic} failed: `, error);
        }
      });
    },


    beforeUpload(file) {
      const fileType = file.type
      const allowedTypes = ['text/plain']
      const isValidType = allowedTypes.includes(fileType)
      if (!isValidType) {
        this.$message.error('只能上传txt文件')
        return false
      }
      return true
    },
    handleFileChange(file) {
      this.fileList = []
      const fileName = file.name;
      const fileType = fileName.substring(fileName.lastIndexOf('.'));
      const reader = new FileReader()
      reader.onload = () => {
        if (fileType == '.txt') {
          this.Content = reader.result.replace(/\n/g, '');
          this.fileContent = reader.result.replace(/,/g, '\n')
          this.stringContent = JSON.stringify(this.Content);
          /* this.publishMessage(this.selectedTopic, this.Content) */
          this.publishMessage(this.selectedTopic, this.stringContent)
        } else {
          this.fileContent = ''
        }
      }
      reader.readAsText(file.raw)
    },
    /* publishData(topic, data) {
      if (!this.mqttClient) {
        this.mqttClient = mqtt.connect('http://100.78.169.243:1883') // 替换为实际的MQTT代理地址
      }

      this.mqttClient.publish(topic, data)
    }, */
    handleScroll(event) {
    const element = event.target;
    if (element.scrollHeight - element.scrollTop === element.clientHeight) {
      this.loadMoreContent();
    }
  },
  },

}
</script>

<style scoped>
.sub_wrapper {
  margin-left: 5%;
  line-height: 3.5vh;
}
.custom-tip {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>   
