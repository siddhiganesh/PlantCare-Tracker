import api from './api'

export interface RegisterRequest {
    username: string
    email: string
    password: string
}

export interface LoginRequest {
    email: string
    password: string
}

export interface User {
    id: number
    username: string
    email: string
    profileImage: string | null
    createdAt: string
    totalPlants?: number
    totalReminders?: number
    completedReminders?: number
}

export interface LoginResponse {
    token: string
    user: User
}

export async function register(
    data: RegisterRequest
) {

    const response = await api.post(
        '/auth/register',
        data
    )

    return response.data

}

export async function login(
    data: LoginRequest
): Promise<LoginResponse> {

    const response = await api.post(
        '/auth/login',
        data
    )

    return response.data

}

export async function getProfile(): Promise<User> {

    const response = await api.get(
        '/auth/profile'
    )

    return response.data

}

export async function uploadProfileImage(
    image: File
): Promise<User> {

    const formData = new FormData()

    formData.append(
        'image',
        image
    )

    const response = await api.put(

        '/auth/profile/image',

        formData,

        {

            headers: {

                'Content-Type':
                    'multipart/form-data'

            }

        }

    )

    return response.data

}

export async function logout() {

    const response = await api.post(
        '/auth/logout'
    )

    return response.data

}