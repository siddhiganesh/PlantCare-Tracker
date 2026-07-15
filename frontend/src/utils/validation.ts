export function isValidEmail(email: string): boolean {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

    return regex.test(email)
}

export function isValidPassword(password: string): boolean {
    return password.length >= 6
}

export function passwordsMatch(
    password: string,
    confirmPassword: string
): boolean {
    return password === confirmPassword
}

export function isRequired(value: string): boolean {
    return value.trim().length > 0
}

export function isPositiveNumber(value: number): boolean {
    return value > 0
}

export function validatePlantName(name: string): boolean {
    return name.trim().length >= 2
}

export function validateSpecies(species: string): boolean {
    return species.trim().length >= 2
}

export function validateLocation(location: string): boolean {
    return location.trim().length >= 2
}

export function validateWateringFrequency(frequency: number): boolean {
    return Number.isInteger(frequency) && frequency > 0
}

export function validateImage(file: File | null): boolean {
    if (!file) {
        return true
    }

    const allowedTypes = [
        'image/jpeg',
        'image/jpg',
        'image/png',
        'image/webp'
    ]

    return allowedTypes.includes(file.type)
}