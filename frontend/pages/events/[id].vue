<template>
    <div>
        <GlobalBreadcrumb />
        <div class="container mx-auto xl:px-20 lg:px-10 px-2">
            <div class="grid lg:grid-cols-3 gap-10">
                <div class="col-span-1">
                    <img src="~/assets/images/event-banner.jpg" class="object-fill h-96 pb-10">
                    <div class="flex items-center pb-6">
                        <span class="mr-2 leading-relaxed w-10">
                            <Icon name="material-symbols:calendar-month" color="dodgerblue" size="35px" />
                        </span>
                        <p class="leading-relaxed">{{ $dayjs(eventDetail.event_date_start).format('dddd MMM YYYY') }}</p>
                    </div>

                    <div class="flex pb-6">
                        <div class="w-10 mr-2">
                            <Icon name="ion:ticket-sharp" color="red" size="35px" />
                        </div>
                        <div>
                            <p class="leading-relaxed font-bold">Ticket Detail:</p>
                            <div v-for="(tk, index) in eventDetail.ticket" :key="'tk-' + index">
                                <span>{{ tk.name }}: {{ tk.price }} BDT</span>
                            </div>
                            <TwButton class="leading-relaxed mt-2">Register Now</TwButton>
                        </div>
                    </div>

                    <div class="flex pb-6">
                        <span class="mr-2 leading-relaxed w-10">
                            <Icon name="ic:baseline-edit-location" class="mr-2" color="dodgerblue" size="35px" />
                        </span>
                        <p class="leading-relaxed">
                            Venue: {{ $trunc(eventDetail.venue) }}<br>
                            address: {{ eventDetail.street_address }}<br>
                            City: {{ eventDetail.city }}, state: {{ eventDetail.state }}
                        </p>
                    </div>
                    <div class="pl-12 pb-6">
                        <p class="leading-relaxed">Add To Calender</p>
                        <clientOnly>
                            <add-to-calendar-button :name="eventDetail.title" :description="eventDetail.description"
                                options="'Apple','Google','iCal','Outlook.com'" :location="eventDetail.venue"
                                :startDate="eventDetail.event_date_start" :end-date="eventDetail.event_date_end"
                                start-time="10:15" end-time="23:30" time-zone="Asia/Dhaka" buttonsList buttonStyle="text"
                                inline="True" hideTextLabelButton lightMode="light">
                            </add-to-calendar-button>
                        </clientOnly>
                    </div>
                    <div class="flex pb-6">
                        <div class="w-10 mr-2">
                            <Icon name="gridicons:multiple-users" color="dodgerblue" size="35px" />
                        </div>
                        <div>
                            <p class="leading-relaxed font-bold">This event is open to:</p>
                            <p v-for="(at, index) in eventDetail.audience_type" :key="'at-' + index"
                                class="inline-flex items-center rounded-md bg-gray-50 px-2 py-2 mr-2 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">
                                {{ at.name }}
                            </p>
                        </div>
                    </div>
                </div>

                <!-- right side content -->
                <div class="col-span-2 leading-relaxed">
                    <div class="bg-slate-300  px-4 py-8 rounded">
                        <p class="leading-relaxed font-light">{{ eventDetail.tags[0].name }}</p>
                        <h1 class="text-3xl font-bold">{{ eventDetail.title }}</h1>
                        <p class="leading-relaxed font-light pt-2">Sponsored by Main Sponsor name</p>
                    </div>
                    <div class="px-4 py-8">
                        <h2 class="text-3xl font-bold">Event Detail</h2>
                        <div v-html="eventDetail.description" class="pt-2"></div>
                        <p class="leading-relaxed pt-4">
                            <span v-for="(tag, index) in eventDetail.tags" :key="'tag-' + index"
                                class="inline-flex items-center rounded-md bg-gray-50 px-2 py-2 mr-2 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">
                                {{ tag.name }}
                            </span>
                        </p>
                    </div>
                    <!-- sponsor section -->
                    <div>
                        <p class="text-center">
                            Event Sponsored By (<TwButton types="link" @click="showRegister = true">Sponsor Now</TwButton>)
                        </p>
                        <div class="grid grid-cols-6 gap-5">
                            <template v-for="(sp, index) in eventDetail.sponsors">
                                <div :key="`sp-${index}`" v-if="sp">
                                    <img :src="sp.sponsor.logo" :alt="sp.sponsor.name">
                                    <div class="text-xs text-gray-800 text-center">{{ sp.sponsor.name }}</div>
                                </div>
                            </template>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <GlobalRegisterSponsor :eventDetail="eventDetail" v-if="showRegister" v-model='showRegister' />
    </div>
</template>

<script lang="ts" setup>
import 'add-to-calendar-button'

const route = useRoute()
const showRegister = ref<Boolean>(false)

let paramsValue = route.params.id
const id = (paramsValue as string).split('-')[0]

const { data: eventDetail } = await useFetch('http://localhost:8000/api/events/' + id)


</script>

<style scoped></style>