<template>
    <div @click.self="$emit('update:modelValue', false)" 
        class="fixed inset-0 flex items-center justify-center bg-gradient-to-b from-slate-950">
        <div class="relative">
            <div class="bg-slate-50 p-10 rounded">
                <!-- if not logged in  -->
                <div>
                    <p class="text-xl text-center">Request to Sponsor</p>
                    
                    <div class="grid grid-cols-1 gap-5 pt-4">
                        <div>
                            <label class="input-label">Company Name</label>
                            <input class="input-text" type="text">
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-5 pt-4">
                        <div>
                            <label class="input-label">email</label>
                            <input class="input-text" type="email">
                        </div>
                        <div>
                            <label class="input-label">Phone number</label>
                            <input class="input-text" type="text">
                        </div>
                    </div>

                    <div class="grid grid-cols-1 gap-5 pt-4">
                        <div>
                            <label class="input-label">Upload logo (200px X 200px)</label>
                            <input class="input-text" type="file">
                        </div>
                    </div>
                    <div class="mt-8">
                        <TwButton>Submit</TwButton>
                        <TwButton color="text" @click="$emit('update:modelValue', false)">Cancel</TwButton>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps(['eventDetail'])
const loginForm = ref<Boolean>(false)
</script>