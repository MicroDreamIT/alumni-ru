<template>
    <div class="bg-white p-4 flex items-center flex-wrap container mx-auto xl:px-20 lg:px-10 px-2">

        <ul class="flex items-center">
            <li class="inline-flex items-center">
                <a href="#" class="text-gray-600 hover:text-blue-500 text-sm">
                    <svg class="w-5 h-auto fill-current mx-2 text-gray-400" xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24" fill="#000000">
                        <path d="M0 0h24v24H0V0z" fill="none" />
                        <path
                            d="M10 19v-5h4v5c0 .55.45 1 1 1h3c.55 0 1-.45 1-1v-7h1.7c.46 0 .68-.57.33-.87L12.67 3.6c-.38-.34-.96-.34-1.34 0l-8.36 7.53c-.34.3-.13.87.33.87H5v7c0 .55.45 1 1 1h3c.55 0 1-.45 1-1z" />
                    </svg>
                </a>

                <span class="mx-4 h-auto text-gray-400 font-medium">/</span>
            </li>

            <li class="inline-flex items-center" v-for="(r, index) in routeLinks" key="'br'+index">
                <a href="#" class="text-gray-600 hover:text-blue-500 text-sm">
                    {{ r }}
                </a>

                <span class="mx-4 h-auto text-gray-400 font-medium" v-if="lastIndex !== index">/</span>
            </li>
        </ul>
    </div>
</template>
<script lang="ts" setup>
const route = useRoute()
let routeLinks = route.fullPath.split('/').slice(1)
const lastIndex = routeLinks.length - 1
</script>