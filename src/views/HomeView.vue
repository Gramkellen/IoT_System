<script>
export default {
  name: 'home',
  methods: {
    changePage() {
      this.$router.push('/about')
    }
  },
}
</script>

<template>
  <div>
    <p>首页(注册、登录)</p>
    <el-button @click="changePage">登录</el-button>
  </div>
</template>

<style>
</style>