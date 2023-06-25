<template>
    <div class="container mx-auto xl:px-20 lg:px-10 px-2">
        <p class="text-3xl text-center pt-20 font-bold">Reach The Alumni Association</p>
        <div class="p-10">
            <div class="grid grid-cols-2 gap-8">
                <div>
                    <label class="input-label">Name</label>
                    <input class="input-text" type="text">
                </div>
                <div>
                    <label class="input-label">Email</label>
                    <input class="input-text" type="email">
                </div>
            </div>
            <div class="grid grid-cols-2 gap-8 pt-10">
                <div>
                    <label class="input-label">Phone</label>
                    <input class="input-text" type="text">
                </div>
                <div>
                    <label class="input-label">Class Year and Degree</label>
                    <input class="input-text" type="email" />
                </div>
            </div>
            <div class="grid grid-cols-1 gap-8 pt-10">
                <div>
                    <label class="input-label">Message</label>
                    <textarea class="input-text" type="text" />
                </div>
            </div>
            <div class="grid grid-cols-1 gap-8 pt-10">
                <TwButton class="w-36">Submit</TwButton>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style></style>