
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './mock'
import * as echarts from 'echarts' // 导入 ECharts
import vueParticles from 'vue-particles'
import countTo from 'vue3-count-to';

const app = createApp(App)

app.use(vueParticles)
app.use(router)
app.use(ElementPlus)
app.config.globalProperties.$echarts = echarts // 将 ECharts 添加到 Vue 实例中
app.use(countTo)

app.mount('#app')
