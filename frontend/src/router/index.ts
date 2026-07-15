import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'

import DashboardLayout from '@/layouts/DashboardLayout.vue'

import DashboardView from '@/views/DashboardView.vue'
import PlantsView from '@/views/PlantsView.vue'
import AddPlantView from '@/views/AddPlantView.vue'
import EditPlantView from '@/views/EditPlantView.vue'
import PlantDetailsView from '@/views/PlantDetailsView.vue'
import RemindersView from '@/views/RemindersView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const router = createRouter({
    history: createWebHistory(),

    routes: [
        {
            path: '/',
            redirect: '/dashboard'
        },

        {
            path: '/login',
            component: LoginView,
            meta: {
                guest: true
            }
        },

        {
            path: '/register',
            component: RegisterView,
            meta: {
                guest: true
            }
        },

        {
            path: '/',
            component: DashboardLayout,
            meta: {
                requiresAuth: true
            },

            children: [
                {
                    path: 'dashboard',
                    component: DashboardView
                },

                {
                    path: 'plants',
                    component: PlantsView
                },

                {
                    path: 'plants/add',
                    component: AddPlantView
                },

                {
                    path: 'plants/edit/:id',
                    component: EditPlantView,
                    props: true
                },

                {
                    path: 'plants/:id',
                    component: PlantDetailsView,
                    props: true
                },

                {
                    path: 'reminders',
                    component: RemindersView
                },

                {
                    path: 'profile',
                    component: ProfileView
                }
            ]
        },

        {
            path: '/:pathMatch(.*)*',
            component: NotFoundView
        }
    ]
})

router.beforeEach((to, from, next) => {

    const token = localStorage.getItem('token')

    if (to.meta.requiresAuth && !token) {
        next('/login')
        return
    }

    if (to.meta.guest && token) {
        next('/dashboard')
        return
    }

    next()
})

export default router