/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        navy: '#12355b',
        saffron: '#e6811d',
        leaf: '#18794e',
        mist: '#f4f7fb'
      },
      boxShadow: { card: '0 6px 18px rgba(18, 53, 91, 0.10)' }
    }
  },
  plugins: []
}
