<script>
export default {
  name: 'user',
  methods: {
    changePage() {
      this.$router.push('/')
    }
  },
}
</script>

<template>
  <div>
    <p>用户名</p>
    <p>已订阅列表</p>
    <p>已发布列表</p>
    <el-button @click="changePage">返回首页</el-button>
  </div>
</template>