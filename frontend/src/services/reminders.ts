import api from './api'

export interface Reminder {
    id: number
    plantId: number
    plantName: string
    title: string
    reminderDate: string
    completed: boolean
    createdAt: string
}

export async function getReminders(): Promise<Reminder[]> {

    const response = await api.get(
        '/reminders'
    )

    return response.data

}

export async function getReminder(
    id: number
): Promise<Reminder> {

    const response = await api.get(
        `/reminders/${id}`
    )

    return response.data

}

export async function completeReminder(
    id: number
): Promise<Reminder> {

    const response = await api.patch(
        `/reminders/${id}`
    )

    return response.data

}

export async function deleteReminder(
    id: number
) {

    const response = await api.delete(
        `/reminders/${id}`
    )

    return response.data

}
export interface ReminderFormData {
    plantId: number
    title: string
    reminderDate: string
    completed: boolean
}