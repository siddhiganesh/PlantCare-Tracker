export function formatDate(date: string | Date): string {
    return new Date(date).toLocaleDateString('en-IN', {
        day: '2-digit',
        month: 'long',
        year: 'numeric'
    })
}

export function formatDateTime(date: string | Date): string {
    return new Date(date).toLocaleString('en-IN', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    })
}

export function getTodayDate(): string {
    return new Date().toISOString().split('T')[0]!
}

export function calculateNextWatering(
    lastWatered: string | Date,
    frequency: number
): string {
    const nextDate = new Date(lastWatered)
    nextDate.setDate(nextDate.getDate() + frequency)

    return nextDate.toISOString().split('T')[0]!
}

export function daysUntil(date: string | Date): number {
    const today = new Date()
    const target = new Date(date)

    today.setHours(0, 0, 0, 0)
    target.setHours(0, 0, 0, 0)

    const diff = target.getTime() - today.getTime()

    return Math.ceil(diff / (1000 * 60 * 60 * 24))
}

export function isOverdue(date: string | Date): boolean {
    return daysUntil(date) < 0
}

export function isToday(date: string | Date): boolean {
    return daysUntil(date) === 0
}

export function isTomorrow(date: string | Date): boolean {
    return daysUntil(date) === 1
}

export function relativeDate(date: string | Date): string {
    const days = daysUntil(date)

    if (days < 0) {
        return `${Math.abs(days)} day(s) overdue`
    }

    if (days === 0) {
        return 'Today'
    }

    if (days === 1) {
        return 'Tomorrow'
    }

    return `In ${days} days`
}