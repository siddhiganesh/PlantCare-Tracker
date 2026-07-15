<script setup lang="ts">
</script>

<template>

<footer class="app-footer">

    <div class="container-fluid">

        <div class="footer-content">

            <span>

                🌿 Plant Care Tracker

            </span>

            <span>

                © {{ new Date().getFullYear() }}

            </span>

        </div>

    </div>

</footer>

</template>

<style scoped>

.app-footer{

    background:rgba(255,255,255,.16);

    backdrop-filter:blur(16px);

    -webkit-backdrop-filter:blur(16px);

    border-top:1px solid rgba(255,255,255,.20);

    color:white;

    padding:14px 30px;

    position:relative;

    z-index:2;

}

.footer-content{

    display:flex;

    justify-content:space-between;

    align-items:center;

    font-size:.95rem;

    font-weight:500;

}

@media(max-width:768px){

    .footer-content{

        flex-direction:column;

        gap:8px;

        text-align:center;

    }

}

</style>