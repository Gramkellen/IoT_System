<script>
import { User,Bell,UploadFilled,Help, } from '@element-plus/icons-vue';
import { RouterLink, RouterView } from 'vue-router'

export default {
  name: 'about',
  components:{
    User,
    Bell,
    UploadFilled,
    Help,
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
    <el-row>
      <el-col :span="4">
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
        >
          <el-menu-item index="1">
            <RouterLink to="/about/user">
              <el-icon><User /></el-icon>
              <span>个人信息</span>
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
</style>
