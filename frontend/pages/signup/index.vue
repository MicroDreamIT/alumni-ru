<template>
    <div class="container mx-auto xl:px-20 lg:px-10 px-2">
        <p class="text-3xl font-bold text-center pt-10">Apply to be a part of Alumni Association</p>



        <Form @submit="postForm" :validation-schema="schema" v-slot="{ errors }">

            <div class="grid grid-cols-2 gap-10 pt-10">
                <div>
                    <label class="input-label" for="first_name">First Name</label>
                    <Field name="first_name" class="input-text" type="text" id="first_name" v-model="form.first_name"
                        rules="required" />
                    <ErrorMessage class="text-red-500" name="first_name" />
                </div>
                <div>
                    <label class="input-label" for="last_name">Last Name</label>
                    <Field name="last_name" class="input-text" type="text" id="last_name" v-model="form.last_name" />
                    <ErrorMessage class="text-red-500" name="last_name" />
                </div>
                <div>
                    <label class="input-label" for="phone_number">Phone Number</label>
                    <Field name="phone_number" class="input-text" id="phone_number" type="text"
                        v-model="form.phone_number" />
                    <ErrorMessage class="text-red-500" name="phone_number" />
                </div>
                <div>
                    <label class="input-label" for="gender">Gender</label>
                    <select name="gender" class="input-text" id="gender" v-model="form.gender">
                        <option v-for="(value, key) in gender" :value="value" :key="`gen ${value}`">{{ key }}</option>
                    </select>
                    <ErrorMessage class="text-red-500" name="gender" />
                </div>
                <div>
                    <label class="input-label" for="subject">Subject</label>
                    <input name="subject" class="input-text" type="text" id="subject" v-model="form.subject">
                    <ErrorMessage class="text-red-500" name="subject" />
                </div>
                <div>
                    <label class="input-label" for="batch_no">Batch No.</label>
                    <input name="batch_no" class="input-text" type="text" id="batch_no" v-model="form.batch_no">
                    <ErrorMessage class="text-red-500" name="batch_no" />
                </div>
                <div>
                    <label class="input-label" for="enroll_year">Enroll Year</label>
                    <input name="enroll_year" class="input-text" type="number" id="enroll_year" v-model="form.enroll_year"
                        maxlength="4" pattern="[1-9][0-9]{3}" required>
                    <ErrorMessage class="text-red-500" name="enroll_year" />
                </div>
                <div>
                    <label class="input-label" for="graduation_year">Graduation Year</label>
                    <input name="graduation_year" class="input-text" type="text" id="graduation_year"
                        v-model="form.graduation_year">
                    <ErrorMessage class="text-red-500" name="graduation_year" />
                </div>
                <div>
                    <label class="input-label" for="street_address">Street Address</label>
                    <input name="street_address" class="input-text" type="text" id="street_address"
                        v-model="form.street_address">
                    <ErrorMessage class="text-red-500" name="street_address" />
                </div>
                <div>
                    <label class="input-label" for="state">State</label>
                    <input name="state" class="input-text" type="text" id="state" v-model="form.state">
                    <ErrorMessage class="text-red-500" name="state" />
                </div>
                <div>
                    <label class="input-label" for="city">City</label>
                    <input name="city" class="input-text" type="text" id="city" v-model="form.city">
                    <ErrorMessage class="text-red-500" name="city" />
                </div>
                <div>
                    <label class="input-label" for="postal_code">Postal Code</label>
                    <input name="postal_code" class="input-text" type="text" id="postal_code" v-model="form.postal_code">
                    <ErrorMessage class="text-red-500" name="postal_code" />
                </div>
            </div>

            <p class="text-xl pt-10 text-center">Login Detail</p>
            <div class="grid grid-cols-2 gap-10 mt-4">
                <div class="col-span-2">
                    <label class="input-label" for="username">Username</label>
                    <input name="username" class="input-text" type="text" id="username" v-model="form.username">
                    <ErrorMessage class="text-red-500" name="username" />
                </div>
                <div>
                    <label class="input-label" for="password">Password</label>
                    <input name="password" class="input-text" type="password" id="password" v-model="form.password">
                    <ErrorMessage class="text-red-500" name="password" />
                </div>
                <div>
                    <label class="input-label" for="confirmation">Password Confirmation</label>
                    <input name="confirmation" class="input-text" type="password" id="confirmation"
                        v-model="form.confirmation">
                    <ErrorMessage class="text-red-500" name="confirmation" />
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
    // phone_number: 'required',
    // gender: 'required',
    // subject: 'required',
    // batch_no: 'required',
    // enroll_year: 'required',
    // graduation_year: 'required',
    // street_address: 'required',
    // state: 'required',
    // city: 'required',
    // postal_code: 'required',
    // email: 'required|email',
    // username: 'required',
    // password: 'required',
    // confirmation: 'required|confirmed:@password'
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
    confirmation: ''
})
// function postForm(val:String) {
//     console.log('hello world', val)
// }
const postForm = async () => {
    const { data, error } = await useFetch('http://localhost:8000/api/accounts/register', {
        method: 'post',
        body: form
    })

    console.log(data);
    console.log(error.value.data);
    // Might be interesting as well:
    console.log(error.value.name, error.value.message);
}

// try {

//     const { data, error } = await useFetch(constants.imageUploadApiUrl, {
//         headers: { "Content-type": "multipart/form-data" },
//         method: 'POST',
//         body: form
//     })
//     console.log("data from server", data.value)
// } catch (error) {
//     console.log(error)
// }


// async function postForm() {
//     console.log('hello')
//     const { data: response } = await useFetch('http://localhost:8000/api/accounts/register', {
//         method: 'post',
//         body: {
//             data: form
//         }
//     })
//     if (response) {
//         console.log(response.value)
//     }
// }
</script>
<style lang="scss" scoped></style>