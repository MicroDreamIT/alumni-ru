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
    ssr: true,
    modules: ["nuxt-lodash"],
    lodash: {
        prefix: "_",
        prefixSkip: ["string"],
        upperAfterPrefix: false,
        exclude: ["map"],
        alias: [
            ["camelCase", "stringToCamelCase"], // => stringToCamelCase
            ["kebabCase", "stringToKebab"], // => stringToKebab
            ["isDate", "isLodashDate"], // => _isLodashDate
        ],
    },
})
