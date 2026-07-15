<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>

<aside class="sidebar">

    <RouterLink
        to="/dashboard"
        class="sidebar-link"
    >
        <i class="bi bi-speedometer2"></i>

        <span>Dashboard</span>
    </RouterLink>

    <RouterLink
        to="/plants"
        class="sidebar-link"
    >
        <i class="bi bi-flower1"></i>

        <span>My Plants</span>
    </RouterLink>

    <RouterLink
        to="/plants/add"
        class="sidebar-link"
    >
        <i class="bi bi-plus-circle"></i>

        <span>Add Plant</span>
    </RouterLink>

    <RouterLink
        to="/reminders"
        class="sidebar-link"
    >
        <i class="bi bi-alarm"></i>

        <span>Reminders</span>
    </RouterLink>

    <RouterLink
        to="/profile"
        class="sidebar-link"
    >
        <i class="bi bi-person-circle"></i>

        <span>Profile</span>
    </RouterLink>

</aside>

</template>

<style scoped>

.sidebar{

    width:260px;

    min-height:calc(100vh - 78px);

    padding:25px 18px;

    display:flex;

    flex-direction:column;

    gap:12px;

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(18px);

    -webkit-backdrop-filter:blur(18px);

    border-right:1px solid rgba(255,255,255,.25);

    box-shadow:8px 0 30px rgba(0,0,0,.08);

}

.sidebar-link{

    display:flex;

    align-items:center;

    gap:15px;

    padding:15px 18px;

    border-radius:16px;

    color:#ffffff;

    font-size:1rem;

    font-weight:600;

    text-decoration:none;

    transition:.25s;

}

.sidebar-link i{

    font-size:1.25rem;

    width:24px;

    text-align:center;

}

.sidebar-link:hover{

    background:rgba(255,255,255,.22);

    transform:translateX(6px);

    color:white;

}

.router-link-active{

    background:rgba(255,255,255,.30);

    color:white;

    box-shadow:0 8px 20px rgba(0,0,0,.12);

}

@media(max-width:992px){

    .sidebar{

        width:90px;

        align-items:center;

    }

    .sidebar-link{

        justify-content:center;

    }

    .sidebar-link span{

        display:none;

    }

}

@media(max-width:768px){

    .sidebar{

        display:none;

    }

}

</style>