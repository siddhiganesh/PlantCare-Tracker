<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import PlantForm from '@/components/PlantForm.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'

import {
    getPlant,
    updatePlant,
    type Plant,
    type PlantFormData
} from '@/services/plants'

const route = useRoute()
const router = useRouter()

const loading = ref(true)

const plant = ref<Plant | null>(null)

async function loadPlant() {

    try {

        loading.value = true

        plant.value = await getPlant(
            Number(route.params.id)
        )

    }

    catch (error) {

        console.error(error)

        alert('Plant not found.')

        router.push('/plants')

    }

    finally {

        loading.value = false

    }

}

async function savePlant(data: PlantFormData) {

    try {

        await updatePlant(

            Number(route.params.id),

            data

        )

        router.push('/plants')

    }

    catch (error) {

        console.error(error)

        alert('Failed to update plant.')

    }

}

onMounted(() => {

    loadPlant()

})
</script>

<template>

<div class="container">

    <LoadingSpinner
        v-if="loading"
    />

    <div
        v-else
        class="row justify-content-center"
    >

        <div class="col-lg-8">

            <div class="card shadow-sm mt-4">

                <div class="card-header">

                    <h3>

                        Edit Plant

                    </h3>

                </div>

                <div class="card-body">

                    <PlantForm

                        v-if="plant"

                        :plant="plant"

                        @submit="savePlant"

                    />

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<style scoped>
</style>