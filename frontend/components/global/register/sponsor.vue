<template>
    <div @click.self="$emit('update:modelValue', false)" 
        class="fixed inset-0 flex items-center justify-center bg-gradient-to-b from-slate-950">
        <div class="relative">
            <TwButton color="text" class="absolute right-0 -mr-10" @click="$emit('update:modelValue', false)">
                <Icon name="majesticons:close" color="grey" size="25px" />
            </TwButton>
            <div class="bg-slate-50 p-10 rounded">

                <ul class="flex flex-wrap justify-center mb-4">
                    <li class="mr-2">
                        <a @click="loginForm = false"
                            :class="`cursor-pointer inline-block p-4 border-b-2 border-transparent rounded-t-lg ${!loginForm ? 'text-blue-600 border-b-2 border-blue-600 rounded-t-lg active dark:text-blue-500 dark:border-blue-500' : 'hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'}`">
                            Register
                        </a>
                    </li>
                    <li class="mr-2">
                        <a @click="loginForm = true"
                            :class="`cursor-pointer inline-block p-4 ${loginForm ? 'text-blue-600 border-b-2 border-blue-600 rounded-t-lg active dark:text-blue-500 dark:border-blue-500' : 'hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 border-b-2 border-transparent rounded-t-lg'}`"
                            aria-current="page">
                            Login
                        </a>
                    </li>
                </ul>


                <!-- if not logged in  -->
                <div v-if="!loginForm">
                    <p class="text-xl text-center">Sponsor Registration</p>
                    <div class="grid grid-cols-2 gap-4 mt-8">
                        <div>
                            <label class="input-label">First Name</label>
                            <input class="input-text" type="text">
                        </div>
                        <div>
                            <label class="input-label">last Name</label>
                            <input class="input-text" type="text">
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-5 pt-4">
                        <div>
                            <label class="input-label">Username</label>
                            <input class="input-text" type="text">
                        </div>
                        <div>
                            <label class="input-label">Company Name</label>
                            <input class="input-text" type="text">
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-5 pt-4">
                        <div>
                            <label class="input-label">Password</label>
                            <input class="input-text" type="password">
                        </div>
                        <div>
                            <label class="input-label">Password Confirmation</label>
                            <input class="input-text" type="password">
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

                <!-- login form  -->

                <div v-else>
                    <p class="text-xl text-center">Sponsor Login</p>
                    <div class="grid grid-cols-1 gap-5 mt-8">
                        <div>
                            <label class="input-label">Username</label>
                            <input class="input-text" type="text">
                        </div>
                    </div>
                    <div class="grid grid-cols-1 gap-5 pt-4">
                        <div>
                            <label class="input-label">Password</label>
                            <input class="input-text" type="password">
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