<template>
    <div class="container mx-auto xl:px-20 lg:px-10 px-2">
        <div class="grid grid-cols-12 gap-10">
            <div class="col-span-4 gap-y-3">
                <img src="~/assets/images/event-banner.jpg"
                     class="object-fill h-96 pb-10"
                >
                <div class="grid grid-cols-12 gap-2 pb-2">
                    <div class="col-span-1">
                        <Icon name="material-symbols:calendar-month" class="mr-2 leading-relaxed" color="red"
                              size="40px"/>
                    </div>
                    <div class="col-span-11 grid items-center">
                        <p class="leading-relaxed">
                            Venue: {{$trunc(eventDetail.venue)}}<br>
                            address: {{eventDetail.street_address}}<br>
                            City: {{eventDetail.city}}, state: {{eventDetail.state}}
                        </p>
                    </div>
                </div>
                <div class="grid grid-cols-12 gap-2 pt-2">
                    <div class="col-span-1">
                        <Icon name="ic:baseline-edit-location" class="mr-2" color="red" size="40px"/>
                    </div>
                    <div class="col-span-11 grid items-center">
                        <p class="leading-relaxed">{{$dayjs(eventDetail.event_date_start).format('dddd MMM YYYY')}}</p>
                    </div>
                </div>
                <div class="flex flex-col">
                    <div class="pl-11 pt-2">
                        <p class="leading-relaxed">Add To Calender</p>
                        <clientOnly>
                            <add-to-calendar-button
                                    :name="eventDetail.title"
                                    :description="eventDetail.description"
                                    options="'Apple','Google','iCal','Outlook.com'"
                                    :location="eventDetail.venue"
                                    :startDate="eventDetail.event_date_start"
                                    :end-date="eventDetail.event_date_end"
                                    start-time="10:15"
                                    end-time="23:30"
                                    time-zone="Asia/Dhaka"
                                    buttonsList
                                    buttonStyle="text"
                                    inline="True"
                                    hideTextLabelButton
                                    lightMode="light"
                            ></add-to-calendar-button>
                        </clientOnly>
                        <p></p>
                    </div>
                </div>
            </div>
            <div class="col-span-8">
                <h1>{{eventDetail.title}}</h1>
                <h2>Event Detail</h2>
                <p>{{eventDetail.description}}</p>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
    import 'add-to-calendar-button'

    const route = useRoute();
    const id = (route.params.id).split('-')[0];
    const {data: eventDetail} = await useFetch('http://localhost:8000/api/events/' + id)

</script>

<style scoped>

</style>