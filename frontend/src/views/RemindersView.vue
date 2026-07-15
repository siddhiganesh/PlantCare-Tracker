<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

import LoadingSpinner from '@/components/LoadingSpinner.vue'
import ReminderCard from '@/components/ReminderCard.vue'

import {
    getReminders,
    completeReminder,
    deleteReminder
} from '@/services/reminders'

const loading = ref(false)

const reminders = ref<any[]>([])

const pendingReminders = computed(() =>

    reminders.value.filter(

        reminder => !reminder.completed

    )

)

const completedReminders = computed(() =>

    reminders.value.filter(

        reminder => reminder.completed

    )

)

async function loadReminders() {

    loading.value = true

    try {

        reminders.value = await getReminders()

    }

    catch (error) {

        console.error(error)

    }

    finally {

        loading.value = false

    }

}

async function markComplete(id: number) {

    try {

        await completeReminder(id)

        await loadReminders()

    }

    catch (error) {

        console.error(error)

    }

}

async function removeReminder(id: number) {

    if (!confirm('Delete this reminder?')) {

        return

    }

    try {

        await deleteReminder(id)

        await loadReminders()

    }

    catch (error) {

        console.error(error)

    }

}

function getStatus(reminder: any) {

    if (reminder.completed) {

        return {

            text: 'Completed',

            class: 'bg-success'

        }

    }

    const today = new Date()

    today.setHours(0, 0, 0, 0)

    const due = new Date(reminder.reminderDate)

    due.setHours(0, 0, 0, 0)

    const diff = Math.floor(

        (due.getTime() - today.getTime()) /

        (1000 * 60 * 60 * 24)

    )

    if (diff < 0) {

        return {

            text: `Overdue by ${Math.abs(diff)} day(s)`,

            class: 'bg-danger'

        }

    }

    if (diff === 0) {

        return {

            text: 'Due Today',

            class: 'bg-warning text-dark'

        }

    }

    if (diff === 1) {

        return {

            text: 'Tomorrow',

            class: 'bg-info'

        }

    }

    return {

        text: `In ${diff} day(s)`,

        class: 'bg-primary'

    }

}

onMounted(loadReminders)

</script>

<template>

<div class="container-fluid">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <h2>

            Automatic Watering Reminders

        </h2>

    </div>

    <LoadingSpinner
        v-if="loading"
    />

    <template v-else>

        <div class="mb-5">

            <h4 class="mb-3">

                Pending

            </h4>

            <div class="row g-4">

                <div

                    v-for="reminder in pendingReminders"

                    :key="reminder.id"

                    class="col-lg-4"

                >

                    <div class="mb-2">

                        <span

                            class="badge"

                            :class="getStatus(reminder).class"

                        >

                            {{ getStatus(reminder).text }}

                        </span>

                    </div>

                    <ReminderCard

                        :reminder="reminder"

                        @complete="markComplete"

                        @delete="removeReminder"

                    />

                </div>

            </div>

        </div>

        <div>

            <h4 class="mb-3">

                Completed

            </h4>

            <div class="row g-4">

                <div

                    v-for="reminder in completedReminders"

                    :key="reminder.id"

                    class="col-lg-4"

                >

                    <ReminderCard

                        :reminder="reminder"

                        @delete="removeReminder"

                    />

                </div>

            </div>

        </div>

        <div

            v-if="reminders.length===0"

            class="alert alert-info text-center mt-5"

        >

            No reminders available.

        </div>

    </template>

</div>

</template>

<style scoped>

h4{

    font-weight:700;

}

</style>