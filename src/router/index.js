import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ExploreView from '../views/ExploreView.vue'
import UserView from '../views/UserView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/explore',
      name: 'explore',
      component: ExploreView
    },
    {
      path: '/user/', 
      name: 'user',
      component: UserView
    },
    {
      path: '/registration',
      name: 'registration',
      component: () => import('../views/RegistrationView.vue')
    },
    {
      path: '/cars/new',
      name: 'new',
      component: () =>import('../views/NewPostView.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: () =>import('../views/LogoutView.vue')
    },
    {
      path: '/cars/details/:id',
      name: 'details',
      component: () =>import('../views/DetailsView.vue')
    }
  ]
})

export default router
