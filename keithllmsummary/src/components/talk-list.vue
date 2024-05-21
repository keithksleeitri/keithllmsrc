<template>
    <div class="chat-container">
        <div
            class="chat-item"
            v-for="(item, index) in talkContents"
            :key="index"
            :class="item.class"
        >
            <div class="person">{{ item.user }}: </div>
            <div class="content">{{ item.content }} </div>
        </div>
    </div>
</template>

<script type="text/javascript">
module.exports = {
    // ---- (設置元件名稱) ----
    name: 'talk-list',
    props: {
        // v-model用屬性
        talkContents: {
            type: Array,
            default: [],
        },
    },
}
</script>

<style scoped>
.chat-container {
    width: 100%;
    height: 75vh;
    border: 1px #333 solid;
    border-radius: 1rem;
    margin-bottom: 1rem;
    overflow-y: scroll;
    display: block;
}
.chat-container .chat-item {
    width: 100%;
    display: flex;
    margin-bottom: 0.25rem;
}

.chat-container .chat-item.user {
    background: #BBB;
    padding: 0.5rem 0.25rem;
}

.chat-container .chat-item.chatgpt {
    background: #DDD;
    padding: 0.5rem 0.25rem;
}

.person {
    width: 5rem;
    text-align: right;
}
.content {
    width: calc(100% - 5rem);
    padding-left: 0.75rem;
}
</style>