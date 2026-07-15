<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import LoadingSpinner from '@/components/LoadingSpinner.vue'
import WateringHistory from '@/components/WateringHistory.vue'

import plantPlaceholder from '@/assets/images/plant-placeholder.jpg'

import {
    getPlant,
    waterPlant
} from '@/services/plants'

const route = useRoute()
const router = useRouter()

const loading = ref(true)
const watering = ref(false)

const plant = ref<any>(null)
const history = ref<any[]>([])

const imageUrl = computed(() => {

    if (!plant.value?.image) {

        return plantPlaceholder

    }

    return `http://127.0.0.1:5000/uploads/${plant.value.image}`

})

const status = computed(() => {

    if (!plant.value) {

        return ''

    }

    const today = new Date()

    const next = new Date(
        plant.value.nextWatering
    )

    const diff = Math.ceil(

        (next.getTime() - today.getTime()) /

        (1000 * 60 * 60 * 24)

    )

    if (diff < 0) {

        return `Overdue by ${Math.abs(diff)} day(s)`

    }

    if (diff === 0) {

        return 'Water Today'

    }

    if (diff === 1) {

        return 'Tomorrow'

    }

    return `In ${diff} day(s)`

})

async function loadPlant() {

    try {

        loading.value = true

        plant.value = await getPlant(

            Number(route.params.id)

        )

    }

    catch (error) {

        console.error(error)

        router.push('/plants')

    }

    finally {

        loading.value = false

    }

}

async function water() {

    try {

        watering.value = true

        plant.value = await waterPlant(

            Number(route.params.id)

        )

    }

    catch (error) {

        console.error(error)

        alert('Unable to water plant.')

    }

    finally {

        watering.value = false

    }

}

function deleteHistory(id: number) {

    history.value = history.value.filter(

        item => item.id !== id

    )

}

onMounted(loadPlant)

</script>

<template>

<div class="container">

    <LoadingSpinner
        v-if="loading"
    />

    <div
        v-else-if="plant"
        class="row g-4"
    >

        <div class="col-lg-5">

            <div class="card shadow">

                <img

                    :src="imageUrl"

                    class="card-img-top"

                    style="height:360px;object-fit:cover;"

                >

                <div class="card-body">

                    <h2>

                        {{ plant.name }}

                    </h2>

                    <hr>

                    <p>

                        <strong>Species:</strong>

                        {{ plant.species }}

                    </p>

                    <p>

                        <strong>Location:</strong>

                        {{ plant.location }}

                    </p>

                    <p>

                        <strong>Water Every:</strong>

                        {{ plant.wateringFrequency }}

                        day(s)

                    </p>

                    <p>

                        <strong>Sunlight:</strong>

                        {{ plant.sunlightRequirement }}

                    </p>

                    <p>

                        <strong>Last Watered:</strong>

                        {{ new Date(plant.lastWatered).toLocaleDateString() }}

                    </p>

                    <p>

                        <strong>Next Watering:</strong>

                        {{ new Date(plant.nextWatering).toLocaleDateString() }}

                    </p>

                    <div
                        class="alert alert-success text-center mt-3"
                    >

                        <strong>

                            {{ status }}

                        </strong>

                    </div>

                    <div class="d-grid mt-3">

                        <button

                            class="btn btn-success btn-lg"

                            @click="water"

                            :disabled="watering"

                        >

                            {{ watering ? 'Watering...' : '💧 Water Plant' }}

                        </button>

                    </div>

                </div>

            </div>

        </div>

        <div class="col-lg-7">

            <WateringHistory

                :history="history"

                @delete="deleteHistory"

            />

        </div>

    </div>

</div>

</template>

<style scoped>
</style>