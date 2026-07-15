import { defineStore } from 'pinia'
import { ref } from 'vue'

import type { Plant } from '@/services/plants'

export const usePlantStore = defineStore('plants', () => {

    const plants = ref<Plant[]>([])

    const selectedPlant = ref<Plant | null>(null)

    const loading = ref(false)

    function setPlants(data: Plant[]) {

        plants.value = data

    }

    function addPlant(plant: Plant) {

        plants.value.unshift(plant)

    }

    function updatePlant(updatedPlant: Plant) {

        const index = plants.value.findIndex(

            plant => plant.id === updatedPlant.id

        )

        if (index !== -1) {

            plants.value[index] = updatedPlant

        }

        if (

            selectedPlant.value &&

            selectedPlant.value.id === updatedPlant.id

        ) {

            selectedPlant.value = updatedPlant

        }

    }

    function removePlant(id: number) {

        plants.value = plants.value.filter(

            plant => plant.id !== id

        )

        if (

            selectedPlant.value &&

            selectedPlant.value.id === id

        ) {

            selectedPlant.value = null

        }

    }

    function setSelectedPlant(

        plant: Plant | null

    ) {

        selectedPlant.value = plant

    }

    function setLoading(value: boolean) {

        loading.value = value

    }

    function clearStore() {

        plants.value = []

        selectedPlant.value = null

        loading.value = false

    }

    return {

        plants,

        selectedPlant,

        loading,

        setPlants,

        addPlant,

        updatePlant,

        removePlant,

        setSelectedPlant,

        setLoading,

        clearStore

    }

})