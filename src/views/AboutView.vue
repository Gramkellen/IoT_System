<script>
import { User,Bell,UploadFilled,Help, } from '@element-plus/icons-vue';
import { RouterLink, RouterView } from 'vue-router'
import Particles from '@/components/particles/index.vue'
export default {
  name: 'about',
  components:{
    User,
    Bell,
    UploadFilled,
    Help,
    "particles":Particles
  },
  methods: {
    changePage() {
      this.$router.push('/')
    }
  },
}
</script>

<template>
  <div class="about">
    <div class="layer">
    <el-row>
      <el-col :span="4">
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
        >
          <el-menu-item index="1">
            <RouterLink to="/about/dataview">
              <el-icon><User /></el-icon>
              <span>数据展示</span>
            </RouterLink>
          </el-menu-item>
          <el-menu-item index="2">
            <RouterLink to="/about/subscribe">
              <el-icon><Bell /></el-icon>
              <span>订阅</span>
            </RouterLink>
          </el-menu-item>
          <el-menu-item index="3">
            <RouterLink to="/about/publish">
              <el-icon><UploadFilled /></el-icon>
              <span>发布</span>
            </RouterLink>
          </el-menu-item>
          <el-menu-item index="4">
            <RouterLink to="/about/help">
              <el-icon><Help /></el-icon>
              <span>Navigator</span>
            </RouterLink>
          </el-menu-item>
      </el-menu>
      </el-col>
      <el-col :span="16">
        <RouterView />
      </el-col>
    </el-row>
    
  </div>
  <particles></particles>
  </div>
  
</template>

<style>
.router-link-active {
  text-decoration: none;
  color: #45a2ff;
}
a{
  text-decoration: none;
  color: rgb(73, 73, 73);
  font-size: 1.8vh;
}
.about {
  .layer {
  position: absolute;
  height: 100%;
  width: 100%;
  z-index: 1001;
  }
  #particles-js {
  
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  }
}
</style>
