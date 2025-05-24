<template>
    <div
        class="collapse collapse-arrow bg-base-100 rounded-xl"
        style="margin-bottom: 0.2em"
    >
        <input type="radio" name="my-accordion" :checked="checked" />
        <div class="collapse-title font-semibold bg-accent text-accent-content">
            {{ itemTitle }}
        </div>
        <div class="collapse-content text-sm bg-base-200 text-base-content">
            <div :id="boxId" class="p-4">{{ itemTitle }}内容</div>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from "vue"

const props = defineProps({
    itemTitle: { type: String },
    boxId: { type: String },
    checked: { type: Boolean, default: false },
})
</script>
