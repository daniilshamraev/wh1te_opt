import Vue from 'vue'
import Router from 'vue-router'
import main from '@/components/pages/main'
import registration from '../components/pages/registration'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: main
    },
    {
      path: '/registration',
      name: 'registration',
      component: registration
    }
  ]
})
