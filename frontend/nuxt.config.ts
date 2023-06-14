export default defineNuxtConfig({
    devtools: {enabled: true},
    runtimeConfig: {
        public: {
            baseURL: process.env.BASE_URL || 'https://api.example.com/',
        },
    },
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
    ssr: true
})
