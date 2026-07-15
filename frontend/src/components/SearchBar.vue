<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps({

    placeholder: {

        type: String,

        default: 'Search...'

    }

})

const emit = defineEmits<{

    (e: 'search', value: string): void

}>()

const query = ref('')

watch(query, (value) => {

    emit('search', value)

})
</script>

<template>

<div class="input-group mb-4">

    <span class="input-group-text">

        🔍

    </span>

    <input

        v-model="query"

        type="text"

        class="form-control"

        :placeholder="placeholder"

    >

    <button

        v-if="query"

        class="btn btn-outline-secondary"

        @click="query = ''"

    >

        Clear

    </button>

</div>

</template>

<style scoped>

.input-group{

    max-width:500px;

}

.form-control{

    height:45px;

}

.input-group-text{

    background:#198754;

    color:white;

    border-color:#198754;

}

</style>