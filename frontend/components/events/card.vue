<template>
    <div class="flex p-8 w-3/4" v-if="!_isEmpty(eventDetail)">
        <div class="flex flex-col items-center justify-center pr-20"
             v-if="!_isEmpty(eventDetail.event_date_start_arr)"
        >
            <div class="text-xl text-center italic font-light">
                {{eventDetail.event_date_start_arr[0]}}
            </div>
            <div class="text-6xl font-bold text-center">
                {{eventDetail.event_date_start_arr[1]}}
            </div>
        </div>
        <div class="col-span-2 md:col-span-3 lg:col-span-5">
            <div class="text-2xl leading-relaxed font-bold">
                <nuxt-link
                        :to="{name:'events-id', params:{id:eventDetail.slug}}"
                >
                    {{eventDetail.title}}
                </nuxt-link>
            </div>
            <div class="leading-relaxed">{{$trunc($removeHtml(eventDetail.description), 150)}}</div>
            <div class="leading-relaxed flex">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                     stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5m-9-6h.008v.008H12v-.008zM12 15h.008v.008H12V15zm0 2.25h.008v.008H12v-.008zM9.75 15h.008v.008H9.75V15zm0 2.25h.008v.008H9.75v-.008zM7.5 15h.008v.008H7.5V15zm0 2.25h.008v.008H7.5v-.008zm6.75-4.5h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V15zm0 2.25h.008v.008h-.008v-.008zm2.25-4.5h.008v.008H16.5v-.008zm0 2.25h.008v.008H16.5V15z"/>
                </svg>
                <span class="pl-2">{{eventDetail.event_date_start}}</span>
            </div>
            <div class="leading-relaxed flex">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                     stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/>
                </svg>
                <span class="pl-2">{{ $trunc(eventDetail.venue, 50) }}</span>
            </div>
            <div class="leading-relaxed">

            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
    const props = defineProps({
        eventDetail: Object as PropType<eventDetail>
    })
    const {$trunc} = useNuxtApp()
    const {$removeHtml} = useNuxtApp()

</script>

<style scoped>

</style>