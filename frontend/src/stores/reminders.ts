import { defineStore } from 'pinia'
import { ref } from 'vue'

import type { Reminder } from '@/services/reminders'

export const useReminderStore = defineStore('reminders', () => {

    const reminders = ref<Reminder[]>([])

    const selectedReminder = ref<Reminder | null>(null)

    const loading = ref(false)

    function setReminders(data: Reminder[]) {

        reminders.value = data

    }

    function addReminder(reminder: Reminder) {

        reminders.value.unshift(reminder)

    }

    function updateReminder(updatedReminder: Reminder) {

        const index = reminders.value.findIndex(

            reminder => reminder.id === updatedReminder.id

        )

        if (index !== -1) {

            reminders.value[index] = updatedReminder

        }

        if (

            selectedReminder.value &&

            selectedReminder.value.id === updatedReminder.id

        ) {

            selectedReminder.value = updatedReminder

        }

    }

    function removeReminder(id: number) {

        reminders.value = reminders.value.filter(

            reminder => reminder.id !== id

        )

        if (

            selectedReminder.value &&

            selectedReminder.value.id === id

        ) {

            selectedReminder.value = null

        }

    }

    function setSelectedReminder(

        reminder: Reminder | null

    ) {

        selectedReminder.value = reminder

    }

    function setLoading(value: boolean) {

        loading.value = value

    }

    function clearStore() {

        reminders.value = []

        selectedReminder.value = null

        loading.value = false

    }

    return {

        reminders,

        selectedReminder,

        loading,

        setReminders,

        addReminder,

        updateReminder,

        removeReminder,

        setSelectedReminder,

        setLoading,

        clearStore

    }

})