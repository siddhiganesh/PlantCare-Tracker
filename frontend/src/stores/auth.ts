import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

import type { User } from '@/services/auth'

export const useAuthStore = defineStore('auth', () => {

    const token = ref<string | null>(
        localStorage.getItem('token')
    )

    const user = ref<User | null>(

        JSON.parse(

            localStorage.getItem('user') || 'null'

        )

    )

    const isAuthenticated = computed(() => {

        return !!token.value

    })

    function login(

        jwtToken: string,

        userData: User

    ) {

        token.value = jwtToken

        user.value = userData

        localStorage.setItem(

            'token',

            jwtToken

        )

        localStorage.setItem(

            'user',

            JSON.stringify(userData)

        )

    }

    function updateUser(

        userData: User

    ) {

        user.value = userData

        localStorage.setItem(

            'user',

            JSON.stringify(userData)

        )

    }

    function logout() {

        token.value = null

        user.value = null

        localStorage.removeItem('token')

        localStorage.removeItem('user')

    }

    return {

        token,

        user,

        isAuthenticated,

        login,

        logout,

        updateUser

    }

})