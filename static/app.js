new Vue({
    el: "#modules_app",
    data: {
        modules: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/modules')
        .then(function (response){
            vm.modules = response.data
        })
    }
}

)