<script setup lang="ts">
import { ref, watch } from 'vue'

import type { Plant } from '@/services/plants'
import type { ReminderFormData } from '@/services/reminders'

interface Reminder {
    id?: number
    plantId: number
    title: string
    reminderDate: string
    completed: boolean
}


const props = defineProps<{
    plants: Plant[]
    reminder?: Reminder | null
}>()

const emit = defineEmits<{
    (e: 'submit', reminder: ReminderFormData): void
}>()

const plantId = ref<number>(0)
const title = ref('')
const reminderDate = ref('')
const completed = ref(false)

watch(
    () => props.reminder,
    (value) => {

        if (!value) {

            return

        }

        plantId.value = value.plantId
        title.value = value.title
        reminderDate.value = value.reminderDate.slice(0, 16)
        completed.value = value.completed

    },
    {
        immediate: true
    }
)

function submitForm() {

    emit('submit', {

        plantId: plantId.value,

        title: title.value,

        reminderDate: reminderDate.value,

        completed: completed.value

    })

}
</script>

<template>

<form @submit.prevent="submitForm">

    <div class="mb-3">

        <label class="form-label">

            Plant

        </label>

        <select
            v-model.number="plantId"
            class="form-select"
            required
        >

            <option
                :value="0"
                disabled
            >

                Select Plant

            </option>

            <option
                v-for="plant in plants"
                :key="plant.id"
                :value="plant.id"
            >

                {{ plant.name }}

            </option>

        </select>

    </div>

    <div class="mb-3">

        <label class="form-label">

            Reminder Title

        </label>

        <input
            v-model="title"
            type="text"
            class="form-control"
            required
        >

    </div>

    <div class="mb-3">

        <label class="form-label">

            Reminder Date

        </label>

        <input
            v-model="reminderDate"
            type="datetime-local"
            class="form-control"
            required
        >

    </div>

    <div
        v-if="props.reminder"
        class="form-check mb-3"
    >

        <input
            v-model="completed"
            class="form-check-input"
            type="checkbox"
            id="completed"
        >

        <label
            class="form-check-label"
            for="completed"
        >

            Completed

        </label>

    </div>

    <div class="d-grid">

        <button
            type="submit"
            class="btn btn-success"
        >

            Save Reminder

        </button>

    </div>

</form>

</template>

<style scoped>
</style>