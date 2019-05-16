<template>
  <el-dialog
    title="股票预测"
    :visible.sync="visible"
    width="50%"
    :before-close="Close">
      <span>
        <el-table
          :data="forecastData"
          border
          style="left:20%;width: 60%">
        <el-table-column
          prop="key"
          label="">
        </el-table-column>
        <el-table-column
          prop="value"
          label="">
        </el-table-column>
      </el-table>
      </span>
    <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="visible = false">确 定</el-button>
      </span>
  </el-dialog>
</template>

<script>
export default {
  data () {
    return {
      loading: false,
      forecastData: []
    }
  },
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    'forecast': Object
  },
  mounted () {
    this.getForecastData()
  },
  methods: {
    Close () {
      this.$emit('update:visible', false)
    },
    getForecastData () {
      this.forecastData = []
      this.forecastData.push({
        key: '涨幅',
        value: this.forecast.increaseRange
      }, {
        key: '上涨概率',
        value: this.forecast.increasePossibility
      }, {
        key: '下降概率',
        value: this.forecast.decreasePossibility
      }, {
        key: '平盘概率',
        value: this.forecast.equalPossibility
      })
    }
  }
}

</script>

<style scoped>
  @import "../css/table.css";
</style>
