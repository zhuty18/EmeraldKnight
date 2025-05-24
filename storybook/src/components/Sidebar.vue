<template>
    <div class="sidebar">
        <SideItem :itemTitle="'参数表'" :boxId="'para_box'" :checked="true"/>
        <SideItem :itemTitle="'代码表'" :boxId="'code_box'" />
        <SideItem :itemTitle="'角色表'" :boxId="'char_box'" />
        <SideItem :itemTitle="'章节表'" :boxId="'chap_box'" />
    </div>
</template>

<script setup lang="ts">
import SideItem from "./SideItem.vue"
</script>

<style scoped>
.sidebar {
    overflow-y: auto;
    -ms-overflow-style: none;
    scrollbar-width: none;
}
.sidebar::-webkit-scrollbar {
    display: none;
}
</style>
