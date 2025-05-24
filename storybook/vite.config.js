import { defineConfig } from "vite"
import tailwindcss from "@tailwindcss/vite"
import vue from "@vitejs/plugin-vue"

export default defineConfig({
  base: "EmeraldKnight/storybook/",
  plugins: [tailwindcss(), vue()],
})
