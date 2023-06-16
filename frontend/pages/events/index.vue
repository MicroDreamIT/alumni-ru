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

            <div class="flex flex-col items-center">
                <EventCard
                        :event-detail="eventDetail"
                        v-if="!_isEmpty(eventDetail)"
                        v-for="eventDetail in eventsArr?.results"
                        :key="eventDetail.id"
                        class="border-b-2 border-gray-200"
                ></EventCard>
            </div>

        </div>
    </div>
</template>
<script lang="ts" setup>
    import EventCard from '~/components/events/EventCard.vue'

    const {data: events} = await useFetch('http://localhost:8000/api/events/')

    const eventDetail = {
        title: '',
        event_date_start: '',
        venue: '',
    };

    const eventsArr = computed<Object>(() => {
        // return events.value.results
        events.value?.results?.map(s => {
            // console.log(s)
            s.event_date_start_arr = new Date(s.event_date_start)
                .toLocaleString("en-US",
                    {timeZone: 'Asia/Dhaka', month: 'short', day: '2-digit', year: 'numeric'})
                .replace(',', '')
                .split(' ')
        })
        return events.value
    })

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
