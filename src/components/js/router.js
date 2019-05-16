import Vue from 'vue'
import Router from 'vue-router'
import Homepage from '../main/Homepage'
import Page1 from '../main/Page'
import Top from '../main/Top'
import Left from '../main/Left'
import showToday from '../main/showToday'
import showRemark from '../main/showRemark'
import showEvents from '../main/showEvents'
import StockDetails from '../main/StockDetails'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage,
      children: [
        {
          path: '',
          components: {
            topNav: Top,
            leftNav: Left,
            main: showToday
          }
        }
      ]
    },
    {
      path: '/showRemark',
      name: 'showRemark',
      component: Page1,
      children: [
        {
          path: '',
          components: {
            topNav: Top,
            leftNav: Left,
            main: showRemark
          }
        }
      ]
    },
    {
      path: '/showEvents',
      name: 'showEvents',
      component: Page1,
      children: [
        {
          path: '',
          components: {
            topNav: Top,
            leftNav: Left,
            main: showEvents
          }
        }
      ]
    },
    {
      path: '/StockDetails',
      name: 'StockDetails',
      component: Page1,
      children: [
        {
          path: '',
          components: {
            topNav: Top,
            leftNav: Left,
            main: StockDetails
          }
        }
      ]
    }
  ]
})

export default router
