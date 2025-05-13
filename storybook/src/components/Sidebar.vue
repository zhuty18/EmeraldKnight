<template>
    <div class="sidebar">
        <ChooseList
            :selectedTab="selectedTab"
            @updateTab="selectedTab = $event"
        />
        <div class="setting-display">
            <component :is="currentComponent" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import ChooseList from "./ChooseList.vue";
import About from "./About.vue";

const selectedTab = ref("首页");
const currentComponent = computed(() => {
    switch (selectedTab.value) {
        case "关于我们":
            return About;
        case "服务":
            return About;
        case "联系我们":
            return About;
        default:
            return About;
    }
});
</script>

<style scoped>
.sidebar {
    width: 30%;
    display: flex;
}
.setting-display {
    flex: 1;
}
</style>
