/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.html", "./**/templates/**/*.html", "./**/templates/*.html"],
    darkMode: "media",
    theme: {
        extend: {},
    },
    plugins: [
        require('daisyui')
    ],
};
