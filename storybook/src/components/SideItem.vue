<template>
    <div class="collapse collapse-arrow bg-base-100 border border-base-300">
        <input type="radio" name="my-accordion" :checked="checked" />
        <div class="collapse-title font-semibold">
            {{ itemTitle }}
        </div>
        <div :id="boxId" class="collapse-content text-sm">
            {{ itemTitle }}内容
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue"

const props = defineProps({
    itemTitle: { type: String },
    boxId: { type: String },
    checked: { type: Boolean, default: false },
})
</script>

<style scoped></style>
