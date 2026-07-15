<script setup lang="ts">
import { computed } from 'vue'

import type { Reminder } from '@/services/reminders'

const props = defineProps<{
    reminder: Reminder
}>()

const emit = defineEmits<{
    (e: 'complete', id: number): void
    (e: 'delete', id: number): void
}>()

const formattedDate = computed(() => {

    return new Date(
        props.reminder.reminderDate
    ).toLocaleDateString()

})

const status = computed(() => {

    if (props.reminder.completed) {

        return {
            text: 'Completed',
            class: 'bg-success'
        }

    }

    const today = new Date()

    today.setHours(
        0,
        0,
        0,
        0
    )

    const due = new Date(
        props.reminder.reminderDate
    )

    due.setHours(
        0,
        0,
        0,
        0
    )

    const diff = Math.floor(

        (due.getTime() - today.getTime())

        /

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

})

function completeReminder() {

    emit(

        'complete',

        props.reminder.id

    )

}

function removeReminder() {

    emit(

        'delete',

        props.reminder.id

    )

}

</script>

<template>

<div class="card reminder-card h-100">

    <div class="card-body">

        <div
            class="d-flex justify-content-between align-items-start mb-3"
        >

            <h5 class="mb-0">

                {{ reminder.title }}

            </h5>

            <span
                class="badge"
                :class="status.class"
            >

                {{ status.text }}

            </span>

        </div>

        <hr>

        <div class="mb-3">

            <small class="text-muted">

                Plant

            </small>

            <div class="fw-semibold">

                🌿 {{ reminder.plantName }}

            </div>

        </div>

        <div>

            <small class="text-muted">

                Reminder Date

            </small>

            <div class="fw-semibold">

                📅 {{ formattedDate }}

            </div>

        </div>

    </div>

    <div class="card-footer">

        <div class="d-flex gap-2">

            <button

                v-if="!reminder.completed"

                class="btn btn-success flex-fill"

                @click="completeReminder"

            >

                💧 Water Plant

            </button>

            <button

                class="btn btn-outline-danger"

                @click="removeReminder"

            >

                Delete

            </button>

        </div>

    </div>

</div>

</template>

<style scoped>

.reminder-card{

    border:none;

    border-radius:18px;

}

.card-body{

    padding:22px;

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

h5{

    font-weight:700;

}

</style>