<template>
    <div class="form-group row">
        <div class="col-sm-11">
            <input
                type="text"
                class="form-control"
                placeholder="請輸入您想總結的網址"
                v-model="value"
            />
        </div>
        <label class="col-sm-1 col-form-label" style="padding: 0px;">
            <button
                type="button"
                class="btn btn-primary"
                @click="send"
                :disabled="disabled"
            >送出</button>
        </label>
    </div>
</template>

<script type="text/javascript">
module.exports = {
    // ---- (設置元件名稱) ----
    name: 'words-input',
    props: {
        // v-model用屬性
        modelValue: {
            type: String,
            default: '',
        },
        // 欄位名稱屬性
        columnName: {
            type: String,
            default: '',
        },
        // ---- (以下可放客製化元件屬性) ----
        placeholder: {
            type: String,
            default: '',
        },
        disabled: {
            type: Boolean,
            default: false,
        },
    },
    computed: {
        // v-model用變數
        value: {
            get() {
                return this.modelValue
            },
            set(value) {
                this.$emit('update:modelValue', value)
            }
        },
    },
    methods: {
        send() {
            this.$emit('send');
        },
    }
}
</script>