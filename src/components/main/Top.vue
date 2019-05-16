<template>
  <el-row>
    <!--
    <div style="position:absolute;left: 0%;top:0%;width:12%;height:100%;text-align: center">
      <div style="background-color:#373d41;text-color:#fff;">
        <el-button type="text" icon="el-icon-menu" style="font-size: 18px;" @click="ToHomepage">
          ShareMarket
          <p></p>
        </el-button>
      </div>
    </div>
    --->
    <div style="position:absolute;left: 8%;top:0%;width:92%;height:100%;">
      <el-menu
        mode="horizontal"
        background-color="#373d41"
        text-color="#fff"
        active-text-color="#ffd04b"
        :router="true">
        <el-menu-item style="font-size: 20px;" @click="showToday ">股市行情</el-menu-item>
        <el-menu-item style="font-size: 20px;" @click="showRemark">股市分析</el-menu-item>
        <el-submenu index="3">
          <template slot="title" >财经新闻</template>
          <el-menu-item @click="showEvents('global')">要闻</el-menu-item>
          <el-menu-item @click="showEvents('a-stock')">A股</el-menu-item>
          <el-menu-item @click="showEvents('us-stock')">美股</el-menu-item>
          <el-menu-item @click="showEvents('forex')">外汇</el-menu-item>
          <el-menu-item @click="showEvents('commodity')">商品</el-menu-item>
          <el-menu-item @click="showEvents('blockchain')">区块链</el-menu-item>
        </el-submenu>
      </el-menu>
    </div>
  </el-row>
</template>

<script>
export default {
  name: 'Top',
  data () {
    return {
    }
  },
  mounted: function () {
  },
  methods: {
    ToHomepage () {
      this.$router.push({ path: '/' })
    },
    showToday () {
      this.$router.push({ path: '/' })
    },
    showRemark () {
      this.$router.push({ path: '/showRemark' })
    },
    showEvents (type) {
      this.$router.push({ path: '/showEvents', query: { type: type } })
    }
  }
}
</script>

<style scoped>
  @import "../css/el.css";
</style>
