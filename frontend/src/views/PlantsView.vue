<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'

import PlantCard from '@/components/PlantCard.vue'
import SearchBar from '@/components/SearchBar.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'

import {
    getPlants,
    deletePlant
} from '@/services/plants'

import { usePlantStore } from '@/stores/plants'

const plantStore = usePlantStore()

const loading = ref(false)

const search = ref('')

const sortedPlants = computed(() => {

    return [...plantStore.plants].sort((a, b) => {

        const today = new Date()

        today.setHours(0, 0, 0, 0)

        const aDate = new Date(a.nextWatering)

        const bDate = new Date(b.nextWatering)

        aDate.setHours(0, 0, 0, 0)

        bDate.setHours(0, 0, 0, 0)

        return aDate.getTime() - bDate.getTime()

    })

})

const filteredPlants = computed(() => {

    let plants = sortedPlants.value

    if (search.value.trim()) {

        const query = search.value.toLowerCase()

        plants = plants.filter(plant =>

            plant.name.toLowerCase().includes(query)

            ||

            plant.species.toLowerCase().includes(query)

            ||

            plant.location.toLowerCase().includes(query)

        )

    }

    return plants

})

async function loadPlants() {

    loading.value = true

    try {

        const plants = await getPlants()

        plantStore.setPlants(plants)

    }

    catch (error) {

        console.error(error)

    }

    finally {

        loading.value = false

    }

}

async function removePlant(id: number) {

    if (!confirm('Delete this plant?')) {

        return

    }

    try {

        await deletePlant(id)

        plantStore.removePlant(id)

    }

    catch (error) {

        console.error(error)

    }

}

function updateSearch(value: string) {

    search.value = value

}

onMounted(loadPlants)

</script>

<template>

<div class="container-fluid">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <h2>

            🌿 My Plants

        </h2>

        <RouterLink

            to="/plants/add"

            class="btn btn-success"

        >

            + Add Plant

        </RouterLink>

    </div>

    <SearchBar

        placeholder="Search plants..."

        @search="updateSearch"

    />

    <LoadingSpinner

        v-if="loading"

    />

    <div

        v-else

        class="row g-4 mt-2"

    >

        <div

            v-for="plant in filteredPlants"

            :key="plant.id"

            class="col-xl-4 col-lg-6"

        >

            <PlantCard

                :plant="plant"

                @delete="removePlant"

            />

        </div>

        <div

            v-if="filteredPlants.length===0"

            class="col-12"

        >

            <div class="alert alert-info text-center">

                No plants found.

            </div>

        </div>

    </div>

</div>

</template>

<style scoped>
</style>