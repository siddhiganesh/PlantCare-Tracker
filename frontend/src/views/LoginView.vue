<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

import { login } from '@/services/auth'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')

const loading = ref(false)
const error = ref('')

async function handleLogin() {

    error.value = ''

    try {

        loading.value = true

        const response = await login({

            email: email.value,

            password: password.value

        })

        authStore.login(

            response.token,

            response.user

        )

        router.push('/dashboard')

    }

    catch (err: any) {

        error.value =

            err.response?.data?.message ||

            'Invalid email or password.'

    }

    finally {

        loading.value = false

    }

}
</script>

<template>

    <div class="container vh-100 d-flex align-items-center justify-content-center">

        <div class="card shadow-lg p-4" style="width:420px;">

            <h2 class="text-center text-success mb-4">

                🌱 Plant Care Tracker

            </h2>

            <form @submit.prevent="handleLogin">

                <div class="mb-3">

                    <label class="form-label">

                        Email

                    </label>

                    <input

                        v-model="email"

                        type="email"

                        class="form-control"

                        required

                    >

                </div>

                <div class="mb-3">

                    <label class="form-label">

                        Password

                    </label>

                    <input

                        v-model="password"

                        type="password"

                        class="form-control"

                        required

                    >

                </div>

                <div
                    v-if="error"
                    class="alert alert-danger"
                >

                    {{ error }}

                </div>

                <button

                    class="btn btn-success w-100"

                    :disabled="loading"

                >

                    {{ loading ? 'Logging in...' : 'Login' }}

                </button>

            </form>

            <hr>

            <div class="text-center">

                Don't have an account?

                <RouterLink to="/register">

                    Register

                </RouterLink>

            </div>

        </div>

    </div>

</template>

<style scoped>
</style>