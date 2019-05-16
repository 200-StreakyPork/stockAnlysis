<template>
  <el-container class="container">
    <el-header class="userTop">
      <router-view name="topNav"></router-view>
    </el-header>
    <el-container>
      <el-aside class="userLeft">
        <router-view name="leftNav"></router-view>
      </el-aside>
      <el-main class="userMain">
        <router-view name="main"></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'Homepage'
}
</script>

<style scoped>
  @import "../css/sidebar.css";
</style>
