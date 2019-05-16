import Vue from 'vue'
import App from './App.vue'
import router from './components/js/router'
import ElementUI from 'element-ui'
import axios from 'axios'
import Vuex from 'vuex'
import 'element-ui/lib/theme-chalk/index.css'
import { showMsg } from './components/js/message'

Vue.use(ElementUI)
Vue.use(Vuex)
Vue.prototype.$axios = axios
Vue.prototype.showMsg = showMsg
Vue.config.productionTip = false

new Vue({
  router,
  el: '#app',
  components: { App },
  render: h => h(App),
  test: /\.css$/,
  loaders: ['style', 'css']
}).$mount('#app')
