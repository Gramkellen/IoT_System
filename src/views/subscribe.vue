<script>
export default {
  name: 'subscribe',
  methods: {
    changePage() {
      this.$router.push('/about/details')
    }
  },
}
</script>

<template>
  <div>
    <p>订阅</p>
    <p>订阅主题输入框</p>
    <p>订阅情况</p>
    <el-button @click="changePage">跳转详情页</el-button>
  </div>
</template>