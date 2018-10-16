Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token}}"
new Vue({
  el: '#login',
  delimiters: ['${','}'],
  data: {
    loading: false,
    message: null,
    credentials: {'username': null, 'password': null }
  },
  mounted: function () {

  },
  methods: {
    login: function() {
      this.loading = true;
      this.$http.post('/api/auth/token/login/', this.credentials)
          .then((response) => {
            this.loading = true;
          })
          .catch((err) => {
            this.loading = true;
             console.log(err);
            swal({
              title: "Error",
              text: "Wrong username or password",
              icon: "warning",
              buttons: false,
              dangerMode: true,
              timer: 1500,
            });
          })
    }
  }
})
