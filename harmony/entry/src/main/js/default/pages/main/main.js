export default {
    data: {
        loading: true
    },
    onLoadStart() {
        this.loading = true;
    },
    onLoadComplete() {
        this.loading = false;
    }
};