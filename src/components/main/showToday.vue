<template>
  <div>
    <el-table
      :data="itemList"
      height="70%"
      style="position: absolute;top:10%;left: 10%;width: 80%;"
      :default-sort = "{prop: 'date', order: 'descending'}">
      <template slot="empty">
        暂时未能获取相关数据，请重试
      </template>
      <el-table-column
        prop="code"
        label="代码"
        align='center'>
      </el-table-column>
      <el-table-column
        prop="close"
        label="昨日收盘"
        align='center'>
      </el-table-column>
      <el-table-column
        prop="open"
        label="今日开盘"
        align='center'>
      </el-table-column>
      <el-table-column
        prop="high"
        label="最高"
        align='center'>
      </el-table-column>
      <el-table-column
        prop="low"
        label="最低"
        align='center'>
      </el-table-column>
      <el-table-column
        prop="volume"
        label="成交量"
        align='center'>
      </el-table-column>
      <el-table-column
        prop="date"
        label="日期"
        align='center'
        sortable>
        <template slot-scope="scope">
          {{changeDateFormat(scope.row.date)}}
        </template>
      </el-table-column>
      <!--
      <el-table-column
        prop="ratio"
        label="比率"
        align='center'>
        <template slot-scope="scope">
          <a v-if="scope.row.ratio > 0" style="color: green">+{{float2(scope.row.ratio)}}%</a>
          <a v-else-if="scope.row.ratio < 0" style="color: red">-{{float2(scope.row.ratio)}}%</a>
          <a v-else-if="scope.row.ratio = 0" style="color: yellow">{{zero}}%</a>
        </template>
      </el-table-column>
      --->
      <el-table-column
        prop=""
        label="其他操作"
        align='center'>
        <template slot-scope="scope">
          <el-button @click="getDetail(scope.$index)" type="text" size="small">K线走势</el-button>
          <el-button @click="getForecast(scope.$index)" type="text" size="small">股票预测</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-row style="position: absolute;top:85%;left: 40%;width: 20%;height: 10%;">
      <span>页数:</span>
      <el-input v-model="page" @blur="getPage()" type="text" style="width:25%"></el-input>
      <span>/</span>
      <el-input v-model="totalPage" type="text" style="width:25%" :disabled="true" readonly="readonly"></el-input>
      <el-button type="primary" @click="getPage()" class="submitBtn" style="width:25%">转到</el-button>
    </el-row>
    <m-forecast v-bind:forecast="forecast" v-if="forecastVisible" :visible.sync = "forecastVisible"></m-forecast>
  </div>
</template>

<script>
import Forecast from '../main/forecast'
import { formatDate } from '../js/format.js'
import { isPostiveInteger } from '../js/validate.js'
export default {
  name: 'showToday',
  data () {
    return {
      title: '应该有个标题',
      itemList: [],
      page: 1,
      totalPage: 1,
      perPage: 20,
      totalNum: 1,
      forecastVisible: false,
      zero: 0.00
    }
  },
  components: {
    'm-forecast': Forecast
  },
  mounted: function () {
    this.getTotalPage()
    this.getPage()
  },
  methods: {
    getTotalPage () {
      let _this = this
      _this.$axios({
        method: 'post',
        url: '/get_codes_count'
      }).then(function (response) {
        console.log(response)
        _this.totalNum = response.data
        _this.totalPage = _this.totalNum / _this.perPage + 1
      }).catch(function (res) {
      })
    },
    getPage () {
      let page = this.page
      let perPage = this.perPage
      let _this = this
      if (!isPostiveInteger(_this.page)) {
        _this.showMsg(_this, true, '页数不是合法数字，请输入一个正整数', 'error')
      } else if (page > _this.totalPage) {
        _this.showMsg(_this, true, '页数超出范围，请重新输入', 'error')
      } else {
        let time = formatDate(new Date())
        let date = time.substring(0, 10)
        _this.$axios({
          method: 'post',
          url: '/get_stock_list',
          data: {
            date: date,
            once: perPage,
            page: page
          }
        }).then(function (response) {
          console.log(response)
          _this.itemList = response.data
        }).catch(function (res) {
        })
      }
    },
    getDetail (index) {
      let stockId = this.itemList[index].stockId
      this.$router.push({ path: '/StockDetails', query: { stockId: stockId } })
    },
    getForecast (index) {
      let stockId = this.itemList[index].stockId
      //获取相关数据
      this.forecastVisible = true
    },
    changeDateFormat (date) {
      let time = new Date(date)
      return formatDate(time)
    },
    float2 (num) {
      return parseFloat(num).toFixed(2)
    }
  }
}
</script>

<style scoped>

</style>
