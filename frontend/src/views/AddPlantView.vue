<script setup lang="ts">
import { useRouter } from 'vue-router'

import PlantForm from '@/components/PlantForm.vue'

import {
    createPlant,
    type PlantFormData
} from '@/services/plants'

const router = useRouter()

async function savePlant(data: PlantFormData) {

    try {

        await createPlant(data)

        router.push('/plants')

    }

    catch (error) {

        console.error(error)

        alert('Failed to create plant.')

    }

}
</script>

<template>

<div class="container">

    <div class="row justify-content-center">

        <div class="col-lg-8">

            <div class="card shadow-sm mt-4">

                <div class="card-header">

                    <h3>

                        Add Plant

                    </h3>

                </div>

                <div class="card-body">

                    <PlantForm

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