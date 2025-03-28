/** @type {import('tailwindcss').Config} */
const plugin = require('tailwindcss/plugin')

module.exports = {
    content: [
        './templates/**/*.html',
        './node_modules/flowbite/**/*.js'
    ],
    theme: {
        container: {
            center: true,
        },
        extend: {
            textShadow: {
                sm: '0 1px 2px var(--tw-shadow-color)',
                DEFAULT: '0 2px 4px var(--tw-shadow-color)',
                lg: '0 8px 16px var(--tw-shadow-color)',
            },
        },
    },
    plugins: [
        require('flowbite/plugin'),
        plugin(function ({matchUtilities, theme}) {
            matchUtilities(
                {
                    'text-shadow': (value) => ({
                        textShadow: value,
                    }),
                },
                {values: theme('textShadow')}
            )
        }),
        require('@tailwindcss/typography'),
    ],
}


