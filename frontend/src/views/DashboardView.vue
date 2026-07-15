<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

import LoadingSpinner from '@/components/LoadingSpinner.vue'

import { getPlants } from '@/services/plants'
import { getReminders } from '@/services/reminders'
import { getProfile } from '@/services/auth'

const loading = ref(true)

const username = ref('')

const plants = ref<any[]>([])
const reminders = ref<any[]>([])

const totalPlants = computed(() => plants.value.length)

const pendingReminders = computed(() =>
    reminders.value.filter(r => !r.completed)
)

const completedReminders = computed(() =>
    reminders.value.filter(r => r.completed)
)

const dueToday = computed(() => {

    const today = new Date()

    today.setHours(0, 0, 0, 0)

    return pendingReminders.value.filter(reminder => {

        const due = new Date(reminder.reminderDate)

        due.setHours(0, 0, 0, 0)

        return due.getTime() === today.getTime()

    })

})

const overdue = computed(() => {

    const today = new Date()

    today.setHours(0, 0, 0, 0)

    return pendingReminders.value.filter(reminder => {

        const due = new Date(reminder.reminderDate)

        due.setHours(0, 0, 0, 0)

        return due < today

    })

})

const upcoming = computed(() => {

    const today = new Date()

    today.setHours(0, 0, 0, 0)

    return pendingReminders.value

        .filter(reminder => {

            const due = new Date(reminder.reminderDate)

            due.setHours(0, 0, 0, 0)

            return due >= today

        })

        .slice(0, 5)

})

const recentPlants = computed(() =>

    plants.value.slice(0, 5)

)

async function loadDashboard() {

    loading.value = true

    try {

        const [

            profile,

            plantData,

            reminderData

        ] = await Promise.all([

            getProfile(),

            getPlants(),

            getReminders()

        ])

        username.value = profile.username

        plants.value = plantData

        reminders.value = reminderData

    }

    catch (error) {

        console.error(error)

    }

    finally {

        loading.value = false

    }

}

onMounted(loadDashboard)

</script>

<template>

<div class="container-fluid">

    <LoadingSpinner
        v-if="loading"
    />

    <template v-else>

        <div class="mb-4">

            <h2>

                Welcome,

                {{ username }}

                🌿

            </h2>

            <p class="text-muted">

                Take care of your plants today.

            </p>

        </div>

        <div class="row g-4 mb-4">

            <div class="col-lg-3">

                <div class="card text-center">

                    <div class="card-body">

                        <h6>Total Plants</h6>

                        <h2 class="text-success">

                            {{ totalPlants }}

                        </h2>

                    </div>

                </div>

            </div>

            <div class="col-lg-3">

                <div class="card text-center">

                    <div class="card-body">

                        <h6>Due Today</h6>

                        <h2 class="text-warning">

                            {{ dueToday.length }}

                        </h2>

                    </div>

                </div>

            </div>

            <div class="col-lg-3">

                <div class="card text-center">

                    <div class="card-body">

                        <h6>Overdue</h6>

                        <h2 class="text-danger">

                            {{ overdue.length }}

                        </h2>

                    </div>

                </div>

            </div>

            <div class="col-lg-3">

                <div class="card text-center">

                    <div class="card-body">

                        <h6>Completed</h6>

                        <h2 class="text-primary">

                            {{ completedReminders.length }}

                        </h2>

                    </div>

                </div>

            </div>

        </div>

        <div class="row g-4">

            <div class="col-lg-6">

                <div class="card">

                    <div class="card-header">

                        🌿 Recent Plants

                    </div>

                    <div class="card-body">

                        <div

                            v-for="plant in recentPlants"

                            :key="plant.id"

                            class="mb-3"

                        >

                            <strong>

                                {{ plant.name }}

                            </strong>

                            <br>

                            <small class="text-muted">

                                {{ plant.species }}

                            </small>

                            <hr>

                        </div>

                        <div
                            v-if="recentPlants.length===0"
                        >

                            No plants added.

                        </div>

                    </div>

                </div>

            </div>

            <div class="col-lg-6">

                <div class="card">

                    <div class="card-header">

                        💧 Upcoming Watering

                    </div>

                    <div class="card-body">

                        <div

                            v-for="reminder in upcoming"

                            :key="reminder.id"

                            class="mb-3"

                        >

                            <strong>

                                {{ reminder.plantName }}

                            </strong>

                            <br>

                            <small>

                                {{ new Date(reminder.reminderDate).toLocaleDateString() }}

                            </small>

                            <hr>

                        </div>

                        <div
                            v-if="upcoming.length===0"
                        >

                            No upcoming watering tasks.

                        </div>

                    </div>

                </div>

            </div>

        </div>

        <div
            v-if="overdue.length"
            class="card mt-4 border-danger"
        >

            <div class="card-header bg-danger text-white">

                ⚠ Overdue Plants

            </div>

            <div class="card-body">

                <div

                    v-for="reminder in overdue"

                    :key="reminder.id"

                    class="mb-2"

                >

                    {{ reminder.plantName }}

                    —

                    {{ new Date(reminder.reminderDate).toLocaleDateString() }}

                </div>

            </div>

        </div>

    </template>

</div>

</template>

<style scoped>
.card{

    border-radius:18px;

}
</style>