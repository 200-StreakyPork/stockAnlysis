<template>
  <div>
    K线图
  </div>
</template>

<script>
import { formatDate } from '../js/format.js'
export default {
  name: 'StockDetails',
  data () {
    return {
      stockId: '',
      gap: 'gap值只能为5,15,30,60,d,m,y',
      KData: []
    }
  },
  mounted: function () {
    this.getParams()
    this.getData(this.stockId)
  },
  methods: {
    getParams () {
      this.stockId = this.$route.query.stockId
    },
    getK () {
      let stockId = this.stockId
      let time = formatDate(new Date())
      let date = time.substring(0, 10)
      let gap = this.gap
      let _this = this
      _this.$axios({
        method: 'post',
        url: '/fetch_k',
        data: {
          code: stockId,
          time_start: date,
          gap: gap
        }
      }).then(function (response) {
        console.log(response)
        this.KData = []
        for (let i = 0; i < response.data.length; i++) {
          this.KData.push(response.data[i])
        }
      }.bind(this)).catch(function (res) {
      })
    },
    changeDateFormat (date) {
      let time = new Date(date)
      return formatDate(time)
    }
  }
}
</script>

<style scoped>

</style>
