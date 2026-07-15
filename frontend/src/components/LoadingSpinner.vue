<script setup lang="ts">
defineProps({

    text: {

        type: String,

        default: 'Loading...'

    }

})
</script>

<template>

<div class="d-flex flex-column justify-content-center align-items-center py-5">

    <div
        class="spinner-border text-success"
        role="status"
        style="width:3rem;height:3rem;"
    >

        <span class="visually-hidden">

            Loading

        </span>

    </div>

    <p class="mt-3 text-muted">

        {{ text }}

    </p>

</div>

</template>

<style scoped>

.spinner-border{

    border-width:0.3rem;

}

p{

    font-size:1rem;

    margin-bottom:0;

}

</style>