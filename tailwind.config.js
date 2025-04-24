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
    themes: ["light", "dark", "emerald"], // 可根据需要添加更多主题
  },
};