<template>
  <div>
    <el-table
      :data="eventList"
      height="60%"
      style="position: absolute;top:10%;left: 10%;width: 80%;"
      :row-style="rowStyle"
      title=""
      stripe
      :default-sort = "{prop: 'date', order: 'descending'}">
      <template slot="empty">
        暂时未能获取相关评论，请重试
      </template>
      <el-table-column
        prop="date"
        label=""
        sortable>
        <template slot-scope="scope">
          <div>
            <a class="titleE">
              <a v-if="scope.row.title !== '' && scope.row.link !== '' " @click="linkTo(scope.row.link)" class="link">{{scope.row.title}}</a>
              <a v-else-if="scope.row.link === '' ">{{scope.row.title}}</a>
              <a v-else-if="scope.row.title === '' " @click="linkTo(scope.row.link)" class="link">查看详情</a>
            </a>
            <a class="contentE">{{scope.row.brief}}</a>
            <a class="timeE">{{scope.row.time}}</a>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <el-row style="position: absolute;top:85%;left: 42%;width: 16%;height: 10%;">
      <span>页数:</span>
      <el-input v-model="page" @blur="getPage()" type="text" style="width:25%"></el-input>
      <span>/</span>
      <el-input v-model="totalPage" type="text" style="width:25%" :disabled="true" readonly="readonly"></el-input>
      <el-button type="primary" @click="getPage()" class="submitBtn" style="width:25%">转到</el-button>
    </el-row>
  </div>
</template>

<script>
import { formatDate } from '../js/format.js'
import { isPostiveInteger } from '../js/validate.js'
export default {
  name: 'showEvents',
  data () {
    return {
      eventList: [],
      page: 1,
      totalPage: 25,
      perPage: 20,
      type: 'global',
      rowStyle: {
        height: '150px'
      }
    }
  },
  mounted: function () {
    this.getParams()
    this.getPage()
  },
  methods: {
    getParams () {
      this.type = this.$route.query.type
    },
    getPage () {
      let page = this.page
      let type = this.type
      let _this = this
      if (!isPostiveInteger(_this.page)) {
        _this.showMsg(_this, true, '页数不是合法数字，请输入一个正整数', 'error')
      } else if (page > _this.totalPage) {
        _this.showMsg(_this, true, '页数超出范围，请重新输入', 'error')
      } else {
        _this.$axios({
          method: 'post',
          url: '/get_events',
          data: {
            layout: type
          }
        }).then(function (response) {
          console.log(response)
          _this.eventList = response.data
        }).catch(function (res) {
        })
      }
    },
    changeDateFormat (date) {
      let time = new Date(date)
      return formatDate(time)
    },
    linkTo (link) {
      window.open(link)
    }
  }
}
</script>

<style scoped>
  @import "../css/time.css";
</style>
