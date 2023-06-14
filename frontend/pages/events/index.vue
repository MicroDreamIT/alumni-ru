<template>
    <div>
        <div class="responsive-bg h-48 flex flex-col items-center justify-center">
            <h1 class="text-4xl mb-6 text-white text-stroke text-stroke-black">
                Events
            </h1>
            <p class="text-6xl font-bold text-white capitalize text-stroke text-stroke-black">All together now</p>
        </div>
        <div class="mx-auto p-2 sm:p-4 lg:p-6 max-w-screen-xl">
            <div class="h-36 everything-center">
                <h2 class="text-4xl font-bold pb-4">
                    Alumni Association Events
                </h2>
                <h3>Browse upcoming events in the RU community</h3>
            </div>

            <div>
                <EventCard :event="event" v-for="event in events.results"></EventCard>
            </div>

        </div>
    </div>
</template>
<script lang="ts" setup>
    import EventCard from '~/components/events/EventCard.vue'
    const {data: events} = await useFetch('http://localhost:8000/api/events/');
</script>

<style lang="scss" scoped>
    .responsive-bg {
        background-image: url('~/assets/images/event-banner.jpg');
        background-size: cover;
        background-position: center;
        height: 450px;

        @media (min-width: 1920px) {
            background-size: 100% auto;
            height: auto;
            width: 1920px;
        }
    }
</style>
