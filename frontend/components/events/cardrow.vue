<template>
  <div v-if="!_isEmpty(eventDetail)" class="p-5 bg-slate-100">
    <div v-if="!_isEmpty(eventDetail.event_date_start_arr)" class="pb-3">
      <p class="text-xl">{{ eventDetail.event_date_start_arr[0] }}</p>
      <p class="text-6xl font-bold">{{ eventDetail.event_date_start_arr[1] }}</p>
    </div>
    <nuxt-link class="font-bold text-3xl" :to="{ name: 'events-id', params: { id: eventDetail.slug } }">
      {{ eventDetail.title }}
    </nuxt-link>
    <div class="flex pt-4">
      <span class="leading-relaxed w-10">
        <Icon name="material-symbols:calendar-month" color="dodgerblue" size="25px" />
      </span>
      <p class="leading-relaxed">{{ $dayjs(eventDetail.event_date_start).format('dddd MMM YYYY') }}</p>
    </div>
    <div class="flex">
      <span class="leading-relaxed w-10">
        <Icon name="ic:baseline-edit-location" class="mr-2" color="dodgerblue" size="25px" />
      </span>
      {{ $trunc(eventDetail.venue, 50) }}
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  eventDetail: Object as PropType<eventDetail>
})
const { $trunc } = useNuxtApp()
const { $removeHtml } = useNuxtApp()
</script>

<style></style>