import api from './api'

export interface Plant {
    id: number
    name: string
    species: string
    location: string
    image: string | null
    wateringFrequency: number
    sunlightRequirement: string
    lastWatered: string
    nextWatering: string
    createdAt: string
    userId: number
}

export interface PlantFormData {
    name: string
    species: string
    location: string
    wateringFrequency: number
    sunlightRequirement: string
    image: File | null
}

export async function getPlants(): Promise<Plant[]> {

    const response = await api.get('/plants')

    return response.data

}

export async function getPlant(
    id: number
): Promise<Plant> {

    const response = await api.get(
        `/plants/${id}`
    )

    return response.data

}

export async function createPlant(
    data: PlantFormData
): Promise<Plant> {

    const formData = new FormData()

    formData.append(
        'name',
        data.name
    )

    formData.append(
        'species',
        data.species
    )

    formData.append(
        'location',
        data.location
    )

    formData.append(
        'wateringFrequency',
        data.wateringFrequency.toString()
    )

    formData.append(
        'sunlightRequirement',
        data.sunlightRequirement
    )

    if (data.image) {

        formData.append(
            'image',
            data.image
        )

    }

    const response = await api.post(

        '/plants',

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

export async function updatePlant(

    id: number,

    data: PlantFormData

): Promise<Plant> {

    const formData = new FormData()

    formData.append(
        'name',
        data.name
    )

    formData.append(
        'species',
        data.species
    )

    formData.append(
        'location',
        data.location
    )

    formData.append(
        'wateringFrequency',
        data.wateringFrequency.toString()
    )

    formData.append(
        'sunlightRequirement',
        data.sunlightRequirement
    )

    if (data.image) {

        formData.append(
            'image',
            data.image
        )

    }

    const response = await api.put(

        `/plants/${id}`,

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

export async function waterPlant(

    id: number,

    notes = ''

): Promise<Plant> {

    const response = await api.post(

        `/plants/${id}/water`,

        {

            notes

        }

    )

    return response.data

}

export async function deletePlant(
    id: number
) {

    const response = await api.delete(
        `/plants/${id}`
    )

    return response.data

}