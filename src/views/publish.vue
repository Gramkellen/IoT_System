<script>
export default {
  name: 'publish',
  methods: {
    changePage() {
      this.$router.push('/about/details')
    }
  },
}
</script>

<template>
<div>
    <p>发布</p>
    <p>发布主题</p>
    <p>发布内容</p>
    <p>成功后<el-button @click="changePage">跳转详情页</el-button></p>
</div>
</template>