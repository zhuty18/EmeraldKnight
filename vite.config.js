import { defineConfig } from 'vite'
import { viteStaticCopy } from 'vite-plugin-static-copy'

export default defineConfig({
    base: './',
    plugins: [
        viteStaticCopy({
            targets: [
                {
                    src: 'data/*',    // 你项目里的 data 文件夹
                    dest: 'data'      // 输出到 dist/data/
                }
            ]
        })
    ],
})
