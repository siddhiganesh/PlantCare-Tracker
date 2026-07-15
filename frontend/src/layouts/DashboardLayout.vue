<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'

import Navbar from '@/components/Navbar.vue'
import Sidebar from '@/components/Sidebar.vue'
import Footer from '@/components/Footer.vue'

import dashboardBg from '@/assets/images/login-bg.jpg'
import plantsBg from '@/assets/images/default-plant.jpg'
import addPlantBg from '@/assets/images/1.png'
import detailsBg from '@/assets/images/plant-placeholder.jpg'
import remindersBg from '@/assets/images/register-bg.jpg'
import profileBg from '@/assets/images/default-plant.jpg'

const route = useRoute()

const backgroundImage = computed(() => {

    const path = route.path

    if (path.startsWith('/plants/add')) {

        return addPlantBg

    }

    if (path.startsWith('/plants/edit')) {

        return addPlantBg

    }

    if (
        path.startsWith('/plants/') &&
        !path.startsWith('/plants/edit')
    ) {

        return detailsBg

    }

    if (path.startsWith('/plants')) {

        return plantsBg

    }

    if (path.startsWith('/reminders')) {

        return remindersBg

    }

    if (path.startsWith('/profile')) {

        return profileBg

    }

    return dashboardBg

})

</script>

<template>

<div
    class="dashboard-layout"
    :style="{
        backgroundImage: `url(${backgroundImage})`
    }"
>

    <div class="background-overlay"></div>

    <Navbar />

    <div class="dashboard-body">

        <Sidebar />

        <main class="dashboard-content">

            <RouterView />

        </main>

    </div>

    <Footer />

</div>

</template>

<style scoped>

.dashboard-layout{

    min-height:100vh;

    display:flex;

    flex-direction:column;

    background-position:center;

    background-repeat:no-repeat;

    background-size:cover;

    background-attachment:fixed;

    position:relative;

}

.background-overlay{

    position:fixed;

    inset:0;

    background:rgba(20,35,20,0.28);

    backdrop-filter:blur(5px);

    z-index:0;

}

.dashboard-body{

    display:flex;

    flex:1;

    position:relative;

    z-index:1;

}

.dashboard-content{

    flex:1;

    padding:30px;

    overflow-y:auto;

}

</style>