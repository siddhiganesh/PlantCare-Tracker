<script setup lang="ts">
import { ref, watch } from 'vue'

import type { Plant, PlantFormData } from '@/services/plants'

const props = defineProps<{
    plant?: Plant | null
}>()

const emit = defineEmits<{
    (e: 'submit', plant: PlantFormData): void
}>()

const name = ref('')
const species = ref('')
const location = ref('')
const wateringFrequency = ref(1)
const sunlightRequirement = ref('Medium')
const image = ref<File | null>(null)

watch(

    () => props.plant,

    (plant) => {

        if (!plant) {

            return

        }

        name.value = plant.name
        species.value = plant.species
        location.value = plant.location
        wateringFrequency.value = plant.wateringFrequency
        sunlightRequirement.value = plant.sunlightRequirement

    },

    {

        immediate: true

    }

)

function handleImage(event: Event) {

    const target = event.target as HTMLInputElement

    image.value = target.files?.item(0) ?? null

}

function submitForm() {

    emit(

        'submit',

        {

            name: name.value,

            species: species.value,

            location: location.value,

            wateringFrequency: wateringFrequency.value,

            sunlightRequirement: sunlightRequirement.value,

            image: image.value

        }

    )

}
</script>

<template>

<form @submit.prevent="submitForm">

    <div class="mb-3">

        <label class="form-label">

            Plant Name

        </label>

        <input

            v-model="name"

            class="form-control"

            required

        >

    </div>

    <div class="mb-3">

        <label class="form-label">

            Species

        </label>

        <input

            v-model="species"

            class="form-control"

            required

        >

    </div>

    <div class="mb-3">

        <label class="form-label">

            Location

        </label>

        <input

            v-model="location"

            class="form-control"

        >

    </div>

    <div class="mb-3">

        <label class="form-label">

            Water Every (Days)

        </label>

        <input

            v-model.number="wateringFrequency"

            type="number"

            min="1"

            class="form-control"

            required

        >

    </div>

    <div class="mb-3">

        <label class="form-label">

            Sunlight Requirement

        </label>

        <select

            v-model="sunlightRequirement"

            class="form-select"

        >

            <option value="Low">

                Low

            </option>

            <option value="Medium">

                Medium

            </option>

            <option value="High">

                High

            </option>

        </select>

    </div>

    <div class="mb-4">

        <label class="form-label">

            Plant Image

        </label>

        <input

            type="file"

            class="form-control"

            accept="image/*"

            @change="handleImage"

        >

    </div>

    <div class="d-grid">

        <button

            type="submit"

            class="btn btn-success"

        >

            Save Plant

        </button>

    </div>

</form>

</template>

<style scoped>
</style>