<template>
  <div class="sub_wrapper">
    <el-row style="margin-top: 2%;">
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
        <div slot="tip" class="el-upload__tip el-icon-warning-outline" style="margin-left: 10px; color: #0a22ac">只能上传txt文件</div>
      </el-upload>
    </el-row>
      <el-row style="margin-top: 2%;">
  <el-row>文件内容：</el-row>
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
      selectedTopic: '',
      uploadUrl: 'https://jsonplaceholder.typicode.com/posts/',
      fileList: [],
      fileContent: '',
      mqttClient: null,
    }
  },
  methods: {
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
      const fileName = file.name;
      const fileType = fileName.substring(fileName.lastIndexOf('.'));
      const reader = new FileReader()
      reader.onload = () => {
        if (fileType == '.txt') {
          this.fileContent = reader.result.replace(/,/g, '\n')
          this.publishData(this.selectedTopic, this.fileContent)
        } else {
          this.fileContent = ''
        }
      }
      reader.readAsText(file.raw)
    },
    publishData(topic, data) {
      if (!this.mqttClient) {
        this.mqttClient = mqtt.connect('mqtt://mqtt-broker-url') // 替换为实际的MQTT代理地址
      }

      this.mqttClient.publish(topic, data)
    },
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