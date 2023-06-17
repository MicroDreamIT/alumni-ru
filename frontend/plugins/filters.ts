export default defineNuxtPlugin((nuxtApp) => {
    return {
        provide: {
            trunc: (value: string, len?: number) => {
                return len ? _truncate(
                    value,
                    {
                        'length': len,
                        omission: '...'
                    }
                ) : _truncate(value)
            },
            dateFullTextFormat: (val: string) => {
                return ''
                // const date = new Date(val)
                // .toLocaleString("en-US",
                //     {
                //         weekday: 'long',
                //         month: 'short',
                //         year: 'numeric',
                //         timeZone: 'Asia/Dhaka',
                //     })
                // date.getMonth()
                // date.getDay()
                // date.getFullYear()
            }
        },
    }
})

