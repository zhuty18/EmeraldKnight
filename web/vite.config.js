import { defineConfig } from "vite";
import { viteStaticCopy } from "vite-plugin-static-copy";

export default defineConfig({
    base: "/EmeraldKnight/web/",
    plugins: [
        viteStaticCopy({
            targets: [
                {
                    src: "data/*", // 你项目里的 data 文件夹
                    dest: "./", // 输出到 dist/
                },
            ],
        }),
    ],
});
