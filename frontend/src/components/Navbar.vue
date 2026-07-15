<script setup lang="ts">
import { useRouter } from 'vue-router'

import { logout } from '@/services/auth'
import { useAuthStore } from '@/stores/auth'

import logo from '@/assets/images/logo.png'

const router = useRouter()

const authStore = useAuthStore()

async function handleLogout() {

    try {

        await logout()

    }

    catch (error) {

        console.error(error)

    }

    authStore.logout()

    router.push('/login')

}
</script>

<template>

<nav class="navbar navbar-expand-lg navbar-dark app-navbar">

    <div class="container-fluid">

        <RouterLink
            to="/dashboard"
            class="navbar-brand d-flex align-items-center"
        >

            <img
                :src="logo"
                class="logo me-3"
            >

            <span>

                Plant Care Tracker

            </span>

        </RouterLink>

        <button

            class="btn btn-light logout-btn"

            @click="handleLogout"

        >

            Logout

        </button>

    </div>

</nav>

</template>

<style scoped>

.app-navbar{

    position:sticky;

    top:0;

    z-index:1000;

    background:rgba(25,135,84,.45);

    backdrop-filter:blur(18px);

    -webkit-backdrop-filter:blur(18px);

    border-bottom:1px solid rgba(255,255,255,.20);

    padding:14px 24px;

}

.logo{

    width:48px;

    height:48px;

    border-radius:50%;

    object-fit:cover;

    background:white;

    padding:4px;

    box-shadow:0 5px 15px rgba(0,0,0,.15);

}

.navbar-brand{

    font-size:1.45rem;

    font-weight:700;

    color:white !important;

}

.logout-btn{

    border-radius:14px;

    padding:8px 22px;

    font-weight:600;

    transition:.25s;

}

.logout-btn:hover{

    transform:translateY(-2px);

}

</style>