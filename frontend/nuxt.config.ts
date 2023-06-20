export default defineNuxtConfig({
    devtools: { enabled: true },
    runtimeConfig: {
        public: {
            baseURL: process.env.BASE_URL || 'https://api.example.com/',
        },
    },
    css: [
        '@/assets/styles/app.scss'
    ],
    vue: {
        compilerOptions: {
            // treat all tags starting with "add-" as custom elements, added this for add-to-calendar
            isCustomElement: (tag) => tag.startsWith('add-'),
        },
    },
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
    extractCSS: true,
    ssr: true,
    noExternal: ['dayjs', 'add-to-calendar-button'],
    modules: [
        "nuxt-lodash",
        "nuxt-icon",
        'dayjs-nuxt'
    ],
    dayjs: {
        locales: ['en'],
        plugins: ['relativeTime', 'utc', 'timezone'],
        defaultLocale: 'en',
        defaultTimezone: 'Asia/Dhaka',
    },
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
    components: [
        {
            path: '~/components',
        },
      ],
})
