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
            removeHtml: (val: string) => {
                
                return val.replace(/(<([^>]+)>)/ig,'')
                
            }
        }
    }
})

