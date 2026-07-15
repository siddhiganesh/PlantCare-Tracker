<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'

import LoadingSpinner from '@/components/LoadingSpinner.vue'

import {
    getProfile,
    uploadProfileImage
} from '@/services/auth'

import {
    getPlants
} from '@/services/plants'

import {
    getReminders
} from '@/services/reminders'

import profilePlaceholder from '@/assets/images/profile-placeholder.png'

const loading = ref(true)

const uploading = ref(false)

const profile = ref<any>({})

const imageFile = ref<File | null>(null)

const totalPlants = ref(0)

const totalReminders = ref(0)

const completedReminders = ref(0)

const dueToday = ref(0)

const overdue = ref(0)

const profileImage = computed(() => {

    if (profile.value.profileImage) {

        return `http://127.0.0.1:5000/uploads/${profile.value.profileImage}`

    }

    return profilePlaceholder

})

async function loadProfile() {

    loading.value = true

    try {

        const [

            user,

            plants,

            reminders

        ] = await Promise.all([

            getProfile(),

            getPlants(),

            getReminders()

        ])

        profile.value = user

        totalPlants.value = plants.length

        totalReminders.value = reminders.length

        completedReminders.value = reminders.filter(

            (r:any)=>r.completed

        ).length

        const today = new Date()

        today.setHours(

            0,

            0,

            0,

            0

        )

        dueToday.value = reminders.filter((r:any)=>{

            if(r.completed){

                return false

            }

            const d = new Date(

                r.reminderDate

            )

            d.setHours(

                0,

                0,

                0,

                0

            )

            return d.getTime()===today.getTime()

        }).length

        overdue.value = reminders.filter((r:any)=>{

            if(r.completed){

                return false

            }

            const d = new Date(

                r.reminderDate

            )

            d.setHours(

                0,

                0,

                0,

                0

            )

            return d<today

        }).length

    }

    catch(error){

        console.error(error)

    }

    finally{

        loading.value=false

    }

}

function chooseImage(event:Event){

    const target=event.target as HTMLInputElement

    imageFile.value=

        target.files?.item(0)??null

}

async function uploadImage(){

    if(!imageFile.value){

        return

    }

    try{

        uploading.value=true

        profile.value=

            await uploadProfileImage(

                imageFile.value

            )

    }

    catch(error){

        console.error(error)

        alert(

            'Failed to upload image.'

        )

    }

    finally{

        uploading.value=false

    }

}

onMounted(

    loadProfile

)

</script>

<template>

<div class="container">

<LoadingSpinner

v-if="loading"

/>

<div

v-else

class="row justify-content-center"

>

<div class="col-xl-10">

<div class="card shadow">

<div class="card-body text-center">

<img

:src="profileImage"

class="rounded-circle border shadow mb-3"

width="190"

height="190"

style="object-fit:cover"

/>

<h2>

{{ profile.username }}

</h2>

<p class="text-muted">

{{ profile.email }}

</p>

<div class="mt-3">

<input

class="form-control mb-3"

type="file"

accept="image/*"

@change="chooseImage"

/>

<button

class="btn btn-success"

@click="uploadImage"

:disabled="!imageFile||uploading"

>

{{ uploading ? 'Uploading...' : 'Change Photo' }}

</button>

</div>

</div>

</div>

<div class="row mt-4 g-3">

<div class="col-lg-3">

<div class="card">

<div class="card-body text-center">

<h5>

🌿 Plants

</h5>

<h2 class="text-success">

{{ totalPlants }}

</h2>

</div>

</div>

</div>

<div class="col-lg-3">

<div class="card">

<div class="card-body text-center">

<h5>

💧 Due Today

</h5>

<h2 class="text-warning">

{{ dueToday }}

</h2>

</div>

</div>

</div>
<div class="col-lg-3">

<div class="card">

<div class="card-body text-center">

<h5>

⚠ Overdue

</h5>

<h2 class="text-danger">

{{ overdue }}

</h2>

</div>

</div>

</div>

<div class="col-lg-3">

<div class="card">

<div class="card-body text-center">

<h5>

✅ Completed

</h5>

<h2 class="text-primary">

{{ completedReminders }}

</h2>

</div>

</div>

</div>

</div>

<div class="card shadow mt-4">

<div class="card-header">

<h4 class="mb-0">

Account Information

</h4>

</div>

<div class="card-body">

<table class="table align-middle">

<tbody>

<tr>

<th width="220">

User ID

</th>

<td>

{{ profile.id }}

</td>

</tr>

<tr>

<th>

Username

</th>

<td>

{{ profile.username }}

</td>

</tr>

<tr>

<th>

Email

</th>

<td>

{{ profile.email }}

</td>

</tr>

<tr>

<th>

Joined

</th>

<td>

{{ new Date(profile.createdAt).toLocaleDateString() }}

</td>

</tr>

<tr>

<th>

Plants

</th>

<td>

{{ totalPlants }}

</td>

</tr>

<tr>

<th>

Pending Reminders

</th>

<td>

{{ totalReminders-completedReminders }}

</td>

</tr>

<tr>

<th>

Completed Reminders

</th>

<td>

{{ completedReminders }}

</td>

</tr>

<tr>

<th>

Due Today

</th>

<td>

{{ dueToday }}

</td>

</tr>

<tr>

<th>

Overdue

</th>

<td>

<span
class="text-danger fw-bold"
v-if="overdue"
>

{{ overdue }}

</span>

<span
v-else
class="text-success fw-bold"
>

0

</span>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

</template>

<style scoped>

img{

border:5px solid white;

}

.card{

border:none;

border-radius:20px;

}

.card-body{

padding:24px;

}

.card-header{

font-weight:700;

font-size:1.1rem;

}

.table th{

width:220px;

font-weight:600;

}

.table td{

font-weight:500;

}

</style>