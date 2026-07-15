<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

import { register } from '@/services/auth'

const router = useRouter()

const username = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')

const loading = ref(false)
const error = ref('')
const success = ref('')

async function handleRegister() {

    error.value = ''
    success.value = ''

    if (
        username.value.trim() === '' ||
        email.value.trim() === '' ||
        password.value.trim() === ''
    ) {

        error.value = 'All fields are required.'

        return

    }

    if (password.value !== confirmPassword.value) {

        error.value = 'Passwords do not match.'

        return

    }

    try {

        loading.value = true

        await register({

            username: username.value,

            email: email.value,

            password: password.value

        })

        success.value = 'Registration successful.'

        setTimeout(() => {

            router.push('/login')

        }, 1000)

    }

    catch (err: any) {

        error.value =

            err.response?.data?.message ||

            'Registration failed.'

    }

    finally {

        loading.value = false

    }

}
</script>

<template>

    <div class="container vh-100 d-flex align-items-center justify-content-center">

        <div
            class="card shadow-lg p-4"
            style="width:420px;"
        >

            <h2 class="text-center text-success mb-4">

                🌱 Plant Care Tracker

            </h2>

            <form @submit.prevent="handleRegister">

                <div class="mb-3">

                    <label class="form-label">

                        Username

                    </label>

                    <input

                        v-model="username"

                        class="form-control"

                        required

                    >

                </div>

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

                <div class="mb-3">

                    <label class="form-label">

                        Confirm Password

                    </label>

                    <input

                        v-model="confirmPassword"

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

                <div
                    v-if="success"
                    class="alert alert-success"
                >

                    {{ success }}

                </div>

                <button

                    class="btn btn-success w-100"

                    :disabled="loading"

                >

                    {{ loading ? 'Registering...' : 'Register' }}

                </button>

            </form>

            <hr>

            <div class="text-center">

                Already have an account?

                <RouterLink to="/login">

                    Login

                </RouterLink>

            </div>

        </div>

    </div>

</template>

<style scoped>
</style>