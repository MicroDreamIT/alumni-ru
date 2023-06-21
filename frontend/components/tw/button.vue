<template>
    <button :type="types" :class="classes">
        <span :class="`uppercase ${classes}`">
            <slot />
        </span>
    </button>
</template>
<script lang="ts" setup>
const props = defineProps([
    'types', 'color'
])
let classes = "text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"

if (props.types === 'link') {
    classes = 'font-semibold text-gray-900 underline decoration-indigo-500'
}
if(props.color==='text'){
    classes = "text-gray-800 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 focus:outline-none"
}

</script>