<template>
    <div>
        <DefaultHeader></DefaultHeader>
        <div>
            <slot/>
        </div>
        <DefaultFooter></DefaultFooter>
    </div>
</template>

<script lang="ts">
    import DefaultHeader from '~/components/layout/DefaultHeader.vue'
    import DefaultFooter from '~/components/layout/DefaultFooter.vue'

    export default defineComponent({
        components: {
            DefaultHeader,
            DefaultFooter
        }
    })
</script>

<style scoped>

</style>