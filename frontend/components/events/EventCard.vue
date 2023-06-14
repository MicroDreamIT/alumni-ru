<template>
    <div>
        <div>date</div>
        <div>
            {{event.title}}
        </div>
    </div>
</template>

<script lang="ts" setup>

    const props = defineProps({
     event: {
         type: Object,
         required: true,
         default: {}
     },
})

</script>

<style scoped>

</style>