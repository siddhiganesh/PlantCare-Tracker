<script setup lang="ts">
import { computed } from 'vue'
import { RouterLink } from 'vue-router'

import plantPlaceholder from '@/assets/images/plant-placeholder.jpg'

import type { Plant } from '@/services/plants'

const props = defineProps<{
    plant: Plant
}>()

const emit = defineEmits<{
    (e: 'delete', id: number): void
}>()

const imageUrl = computed(() => {

    if (!props.plant.image) {

        return plantPlaceholder

    }

    return `http://127.0.0.1:5000/uploads/${props.plant.image}`

})

const status = computed(() => {

    const today = new Date()

    today.setHours(0, 0, 0, 0)

    const next = new Date(props.plant.nextWatering)

    next.setHours(0, 0, 0, 0)

    const diff = Math.floor(

        (next.getTime() - today.getTime())

        /

        (1000 * 60 * 60 * 24)

    )

    if (diff < 0) {

        return {

            text: `Overdue by ${Math.abs(diff)} day(s)`,

            badge: 'bg-danger'

        }

    }

    if (diff === 0) {

        return {

            text: 'Water Today',

            badge: 'bg-warning text-dark'

        }

    }

    if (diff === 1) {

        return {

            text: 'Tomorrow',

            badge: 'bg-info'

        }

    }

    return {

        text: `In ${diff} day(s)`,

        badge: 'bg-success'

    }

})

function deletePlant() {

    emit(

        'delete',

        props.plant.id

    )

}

</script>

<template>

<div class="card h-100 shadow plant-card">

    <img

        :src="imageUrl"

        class="card-img-top"

        alt="Plant"

    >

    <div class="card-body">

        <div
            class="d-flex justify-content-between align-items-start mb-3"
        >

            <h5 class="mb-0">

                {{ plant.name }}

            </h5>

            <span

                class="badge"

                :class="status.badge"

            >

                {{ status.text }}

            </span>

        </div>

        <p>

            🌱

            <strong>Species:</strong>

            {{ plant.species }}

        </p>

        <p>

            📍

            <strong>Location:</strong>

            {{ plant.location }}

        </p>

        <p>

            💧

            <strong>Every:</strong>

            {{ plant.wateringFrequency }}

            day(s)

        </p>

        <p>

            ☀️

            <strong>Sunlight:</strong>

            {{ plant.sunlightRequirement }}

        </p>

        <p>

            📅

            <strong>Next:</strong>

            {{ new Date(plant.nextWatering).toLocaleDateString() }}

        </p>

    </div>

    <div class="card-footer">

        <div class="d-grid gap-2">

            <RouterLink

                :to="`/plants/${plant.id}`"

                class="btn btn-success"

            >

                View Details

            </RouterLink>

            <div class="d-flex gap-2">

                <RouterLink

                    :to="`/plants/edit/${plant.id}`"

                    class="btn btn-warning flex-fill"

                >

                    Edit

                </RouterLink>

                <button

                    class="btn btn-danger flex-fill"

                    @click="deletePlant"

                >

                    Delete

                </button>

            </div>

        </div>

    </div>

</div>

</template>

<style scoped>

.plant-card{

    border:none;

    border-radius:20px;

    overflow:hidden;

    transition:.25s;

}

.plant-card:hover{

    transform:translateY(-6px);

}

.card-img-top{

    height:240px;

    object-fit:cover;

}

.card-body{

    padding:22px;

}

.card-body p{

    margin-bottom:12px;

}

.card-title,

h5{

    font-weight:700;

}

.card-footer{

    background:transparent;

    border-top:none;

    padding:18px;

}

.badge{

    font-size:.8rem;

    padding:8px 12px;

}

</style>