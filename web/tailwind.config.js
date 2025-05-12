// tailwind.config.js
module.exports = {
  content: [
    "./index.html",
    "./script.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["emerald", "forest"],
    darkTheme: "forest"
  },
};