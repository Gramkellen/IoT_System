<template>
    <div class="container">
        <el-button @click="changePage">返回首页</el-button>
      <el-col :span="8">
        <el-row><div class="row">第一列 - 第一行</div></el-row>
        <el-row><div class="row">第一列 - 第二行</div></el-row>
        <el-row><div class="row">第一列 - 第三行</div></el-row>
      </el-col>
      <el-col :span="8"></el-col>
      <el-col :span="8">
        <el-row><div class="row">第三列 - 第一行</div></el-row>
        <el-row><div class="row">第三列 - 第二行</div></el-row>
        <el-row><div class="row">第三列 - 第三行</div></el-row>
      </el-col>
    </div>
  </template>
  
  <script>
  export default {
    name: 'dataview',
    methods: {
    changePage() {
      this.$router.push('/')
    }
  },
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
  }
  
  .row {
    border: 1px solid blue;
    padding: 10px;
  }
  </style>