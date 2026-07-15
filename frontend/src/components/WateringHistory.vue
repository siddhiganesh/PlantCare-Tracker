<script setup lang="ts">

const props = defineProps<{

    history: {

        id: number

        wateredOn: string

        notes: string

    }[]

}>()

</script>

<template>

<div class="card shadow-sm">

    <div class="card-header">

        <h5 class="mb-0">

            💧 Watering History

        </h5>

    </div>

    <div class="card-body">

        <div
            v-if="history.length"
            class="timeline"
        >

            <div

                v-for="item in [...history].sort((a,b)=>
                    new Date(b.wateredOn).getTime()-
                    new Date(a.wateredOn).getTime()
                )"

                :key="item.id"

                class="timeline-item"

            >

                <div class="timeline-dot">

                    💧

                </div>

                <div class="timeline-content">

                    <div class="fw-bold">

                        {{ new Date(item.wateredOn).toLocaleString() }}

                    </div>

                    <div
                        class="text-muted mt-1"
                    >

                        {{ item.notes || "Plant watered." }}

                    </div>

                </div>

            </div>

        </div>

        <div
            v-else
            class="text-center py-5 text-muted"
        >

            No watering history available.

        </div>

    </div>

</div>

</template>

<style scoped>

.timeline{

    position:relative;

    margin-left:18px;

}

.timeline::before{

    content:"";

    position:absolute;

    left:11px;

    top:0;

    bottom:0;

    width:2px;

    background:#198754;

}

.timeline-item{

    display:flex;

    margin-bottom:24px;

    position:relative;

}

.timeline-dot{

    width:24px;

    height:24px;

    border-radius:50%;

    background:#198754;

    color:white;

    display:flex;

    justify-content:center;

    align-items:center;

    margin-right:18px;

    z-index:2;

    font-size:12px;

}

.timeline-content{

    flex:1;

    background:white;

    border-radius:14px;

    padding:14px 18px;

    box-shadow:0 4px 15px rgba(0,0,0,.08);

}

</style>