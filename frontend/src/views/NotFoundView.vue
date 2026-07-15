<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>

<div class="container vh-100 d-flex justify-content-center align-items-center">

    <div class="text-center">

        <h1
            class="display-1 fw-bold text-success"
        >

            404

        </h1>

        <h3 class="mb-3">

            Page Not Found

        </h3>

        <p class="text-muted mb-4">

            The page you are looking for does not exist.

        </p>

        <RouterLink
            to="/dashboard"
            class="btn btn-success"
        >

            Go to Dashboard

        </RouterLink>

    </div>

</div>

</template>

<style scoped>

.display-1{

    font-size:7rem;

}

</style>