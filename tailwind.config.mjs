/** @type {import('tailwindcss').Config} */
export default {
    content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
    theme: {
        extend: {
            colors: {
                bgDeep: '#020202',
                bgCenter: '#0a0f0d',
                amber: {
                    DEFAULT: '#ffb347',
                    glow: '#ffcc00'
                },
                emerald: {
                    DEFAULT: '#10b981',
                    glow: '#00ffcc'
                }
            },
            fontFamily: {
                sans: ['Outfit', 'sans-serif'],
                serif: ['Merriweather', 'serif'],
            }
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
    ],
}
