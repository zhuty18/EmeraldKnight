<template>
    <div
        class="app bg-base-100 text-base-content min-h-screen flex flex-vert justify-center"
    >
        <div class="flex w-full">
            <div class="bg-base-200 h-full" style="width: 25vw">
                <Sidebar style="height: 100vh" />
            </div>
            <div class="divider divider-horizontal"></div>
            <div class="bg-base-100 h-full" style="width: 70vw; height: 100vh">
                <VueFlow
                    v-model:nodes="nodes"
                    v-model:edges="edges"
                    fit-view-on-init
                    class="vue-flow-basic-example"
                    :default-zoom="1.5"
                    :min-zoom="0.2"
                    :max-zoom="4"
                >
                    <Background pattern-color="#aaa" :gap="8" />

                    <MiniMap />

                    <Controls />

                    <template #node-custom="nodeProps">
                        <SpecialNode v-bind="nodeProps" />
                    </template>

                    <template #edge-custom="edgeProps">
                        <SpecialEdge v-bind="edgeProps" />
                    </template>
                </VueFlow>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref } from "vue"
import { Background } from "@vue-flow/background"
import { Controls } from "@vue-flow/controls"
import { MiniMap } from "@vue-flow/minimap"
import { VueFlow, useVueFlow, type Node, type Edge } from "@vue-flow/core"
import SpecialNode from "./components/SpecialNode.vue"
import SpecialEdge from "./components/SpecialEdge.vue"
import Sidebar from "./components/Sidebar.vue"

const { onConnect, addEdges } = useVueFlow()

const nodes = ref<Node[]>([
    { id: "1", type: "input", label: "Node 1", position: { x: 250, y: 5 } },
    { id: "2", type: "output", label: "Node 2", position: { x: 100, y: 100 } },
    { id: "3", type: "custom", label: "Node 3", position: { x: 400, y: 100 } },
])

const edges = ref<Edge[]>([
    { id: "e1-2", source: "1", target: "2", type: "custom" },
    { id: "e1-3", source: "1", target: "3", animated: true },
])

onConnect((params) => {
    addEdges([params])
})
</script>

<style scoped>
.app {
    height: 100vh;
    display: flex;
    background-color: var(--color-base-100);
}

.main-content {
    flex: 1;
}
</style>
