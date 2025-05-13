<template>
    <div class="choose-area">
        <ul>
            <li
                v-for="item in tabs"
                :key="item"
                :class="{ active: item === selectedTab }"
                @click="emit('updateTab', item)"
            >
                {{ item }}
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from "vue";

const tabs = ["首页", "关于我们", "服务", "联系我们"];
const props = defineProps<{
    selectedTab: string;
}>();

const emit = defineEmits<{
    (e: "updateTab", tab: string): void;
}>();
</script>

<style scoped>
.choose-area {
    padding: 1rem;
    background-color: #2c3e50;
    color: white;
}

.choose-area ul {
    list-style: none;
    padding: 0;
}
.choose-area li {
    margin: 1rem 0;
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 4px;
}
.choose-area li:hover,
.choose-area li.active {
    background-color: #1abc9c;
}
</style>
