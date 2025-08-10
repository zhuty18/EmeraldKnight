<template>
    <div class="bg-base-100 text-base-content flex flex-vert">
        <div style="width: 25vw; height: 100vh">
            <Sidebar />
        </div>
        <div style="width: 75vw; height: 100vh">
            <VueFlow
                :nodes="nodes"
                :edges="edges"
                @nodes-initialized="layoutGraph()"
            >
                <Background patternColor="var(--color-base-300)" />
                <MiniMap />
                <Controls />
                <Panel :position="'top-right'">
                    <details class="dropdown">
                        <summary class="btn btn-sm btn-soft btn-primary">
                            章节
                        </summary>
                        <ul
                            class="menu dropdown-content bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
                        >
                            <li v-for="item in getChapters()">
                                <button @click="switchChapter(item)">
                                    第{{ item }}章
                                </button>
                            </li>
                        </ul>
                    </details>
                    <details class="dropdown">
                        <summary class="btn btn-sm btn-soft btn-neutral">
                            配置
                        </summary>
                        <ul
                            class="menu dropdown-content bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
                        >
                            <li>
                                <button @click="loadConfig()">导入配置</button>
                            </li>
                            <li><button>导出配置</button></li>
                        </ul>
                    </details>
                    <details class="dropdown">
                        <summary class="btn btn-sm btn-soft btn-secondary">
                            节点
                        </summary>
                        <ul
                            class="menu dropdown-content bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
                        >
                            <li><button>添加节点</button></li>
                            <li><button>删除节点</button></li>
                        </ul>
                    </details>
                    <details class="dropdown">
                        <summary class="btn btn-sm btn-soft btn-secondary">
                            选项
                        </summary>
                        <ul
                            class="menu dropdown-content bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
                        >
                            <li><button>添加选项</button></li>
                            <li><button>删除选项</button></li>
                        </ul>
                    </details>
                    <details class="dropdown">
                        <summary class="btn btn-sm btn-soft btn-accent">
                            参数
                        </summary>
                        <ul
                            class="menu dropdown-content bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
                        >
                            <li><button>导入配置</button></li>
                            <li><button>导出配置</button></li>
                        </ul>
                    </details>
                </Panel>
            </VueFlow>
        </div>
    </div>
</template>

<script setup>
import { nextTick, ref, Suspense } from "vue"
import { Background } from "@vue-flow/background"
import { Controls } from "@vue-flow/controls"
import { MiniMap } from "@vue-flow/minimap"
import { VueFlow, Panel, useVueFlow } from "@vue-flow/core"
import Sidebar from "./components/Sidebar.vue"

import { initialNodes, initialEdges } from "./init.js"
import { useLayout } from "./useLayout"

import { loadChapter, loadConfig, getChapters } from "./story.js"

let data = loadChapter("2")
let nodes = ref(data.node)
let edges = ref(data.edge)

async function switchChapter(chapId) {
    let new_data = loadChapter(chapId)
    nodes = ref(new_data.node)
    edges = ref(new_data.edge)
    await layoutGraph()
}

const { layout } = useLayout()

const { fitView } = useVueFlow()

async function layoutGraph(direction) {
    nodes.value = layout(nodes.value, edges.value, direction)

    nextTick(() => {
        fitView()
    })
}
</script>
