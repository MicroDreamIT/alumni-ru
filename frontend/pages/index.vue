<template>
    <div>
        <!-- banner -->
        <div class="banner-image bg-cover overflow-hidden bg-no-repeat relative ">
            <div class="flex flex-wrap flex-col justify-center items-center py-28">
                <h1 class="text-3xl mb-7 text-white text-center font-serif">
                    Rajshahi University Alumni
                </h1>
                <p class="text-6xl mb-7 text-center text-white font-bold">
                    Welcome Home
                </p>
                <p class="text-2xl mb-7 text-white font-serif text-center">
                    Rajshahi University Alumni Association helps you keep close wherever you are.
                </p>
            </div>
        </div>

        <!-- featured event  -->
        <div class="container mx-auto xl:px-20 lg:px-10 px-2">
            <p class="text-center text-3xl pt-10">
                Featured Events
            </p>
            <p class="subheading text-center pt-3">Peek at some alumni events happening just around the corner.</p>
            <div class="grid grid-cols-3 gap-10">
                <template v-for="eventDetail in eventsArr?.results">
                    <EventsCardrow></EventsCardrow>
                </template>
            </div>

        </div>

    </div>
</template>

<script lang="ts" setup>
const { data: events } = await useFetch('http://localhost:8000/api/events/?limit=3')

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
                { timeZone: 'Asia/Dhaka', month: 'short', day: '2-digit', year: 'numeric' })
            .replace(',', '')
            .split(' ')
    })
    return events.value
})
</script>

<style scoped lang="scss">
.banner-image {
    background-image: linear-gradient(to bottom, rgba(250, 250, 250, 0.267), rgba(0, 0, 0, 0.73)), url('~/assets/images/banner.jpg');
}
</style>