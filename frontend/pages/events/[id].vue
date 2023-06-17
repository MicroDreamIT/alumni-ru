<template>
    <div class="container mx-auto">
        <div class="grid grid-cols-12 gap-1">
            <div class="col-span-4">
                <div class="flex flex-col">
                    <div class="flex">
                        <Icon name="et:alarmclock" class="mr-2" color="red" size="24px"/>
                        <p>{{$dayjs(eventDetail.event_date_start).format('dddd MMM YYYY')}}</p>
                    </div>
                </div>
            </div>
            <div class="col-span-8">

            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
    const route = useRoute();
    const id = (route.params.id).split('-')[0];
    const {data: eventDetail} = await useFetch('http://localhost:8000/api/events/' + id)
</script>

<style scoped>

</style>