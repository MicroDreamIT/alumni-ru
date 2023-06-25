<template>
    <div class="container mx-auto xl:px-20 lg:px-10 px-2">
        <p class="text-3xl font-bold text-center pt-10">Apply to be a part of Alumni Association</p>

        <Form @submit="postForm" :validation-schema="schema" v-slot="{ errors }">

            <div class="grid grid-cols-2 gap-10 pt-10">
                <div>
                    <label class="input-label" for="first_name">First Name</label>
                    <Field name="first_name" class="input-text" type="text" id="first_name" v-model="form.first_name" rules="required" />
                    <ErrorMessage class="text-red-500" name="first_name" />
                </div>
                <div>
                    <label class="input-label" for="last_name">Last Name</label>
                    <Field name="last_name" class="input-text" type="text" id="last_name" v-model="form.last_name" />
                    <ErrorMessage class="text-red-500" name="last_name" />
                </div>
                <div>
                    <label class="input-label" for="phone_number">Phone Number</label>
                    <Field name="phone_number" class="input-text" id="phone_number" type="text" v-model="form.phone_number" />
                </div>
                <div>
                    <label class="input-label" for="gender">Gender</label>
                    <select class="input-text" id="gender" v-model="form.gender">
                        <option v-for="(value, key) in gender" :value="value" :key="`gen ${value}`">{{ key }}</option>
                    </select>
                </div>
                <div>
                    <label class="input-label" for="subject">Subject</label>
                    <input class="input-text" type="text" id="subject" v-model="form.subject">
                </div>
                <div>
                    <label class="input-label" for="batch_no">Batch No.</label>
                    <input class="input-text" type="text" id="batch_no" v-model="form.batch_no">
                </div>
                <div>
                    <label class="input-label" for="enroll_year">Enroll Year</label>
                    <input class="input-text" type="number" id="enroll_year" v-model="form.enroll_year" maxlength="4"
                        pattern="[1-9][0-9]{3}" required>
                </div>
                <div>
                    <label class="input-label" for="graduation_year">Graduation Year</label>
                    <input class="input-text" type="text" id="graduation_year" v-model="form.graduation_year">
                </div>
                <div>
                    <label class="input-label" for="street_address">Street Address</label>
                    <input class="input-text" type="text" id="street_address" v-model="form.street_address">
                </div>
                <div>
                    <label class="input-label" for="state">State</label>
                    <input class="input-text" type="text" id="state" v-model="form.state">
                </div>
                <div>
                    <label class="input-label" for="city">City</label>
                    <input class="input-text" type="text" id="city" v-model="form.city">
                </div>
                <div>
                    <label class="input-label" for="postal_code">Postal Code</label>
                    <input class="input-text" type="text" id="postal_code" v-model="form.postal_code">
                </div>
            </div>

            <p class="text-xl pt-10 text-center">Login Detail</p>
            <div class="grid grid-cols-2 gap-10 mt-4">
                <div class="col-span-2">
                    <label class="input-label" for="username">Username</label>
                    <input class="input-text" type="text" id="username" v-model="form.username">
                </div>
                <div>
                    <label class="input-label" for="password">Password</label>
                    <input class="input-text" type="password" id="password" v-model="form.password">
                </div>
                <div>
                    <label class="input-label" for="password_confirmation">Password Confirmation</label>
                    <input class="input-text" type="password" id="password_confirmation"
                        v-model="form.password_confirmation">
                </div>
                <TwButton class="w-36" type="submit">Submit</TwButton>

            </div>
        </Form>

    </div>
</template>

<script lang="ts" setup>
import { Form, Field, ErrorMessage } from 'vee-validate';

const schema = {
    first_name: 'required',
    last_name: 'required',
    phone_number:'required',
    email: 'required|email',
}

const gender = ref<Object>({
    MALE: 'M',
    FEMALE: 'F',
    OTHER: 'O'
})
const form = ref<Object>({
    first_name: '',
    last_name: '',
    phone_number: '',
    subject: '',
    batch_no: '',
    enroll_year: '',
    graduation_year: '',
    street_address: '',
    state: '',
    city: '',
    postal_code: '',
    username: '',
    password: '',
    password_confirmation: ''
})

function postForm() {
    console.log(form)
}
</script>
<style lang="scss" scoped>

</style>