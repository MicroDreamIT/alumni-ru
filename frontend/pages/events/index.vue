<template>
    <div>
        I am events data:
        <pre>
            {{events}}
        </pre>
    </div>
</template>

<script lang="ts" setup>
    const {data: events} = await useFetch('http://localhost:8000/api/events/')
</script>
