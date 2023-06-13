export default defineNuxtConfig({
    devtools: {enabled: true},
    css: [
        '@/assets/styles/app.scss',
    ],
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
    extractCSS: true,
    ssr: false
})
