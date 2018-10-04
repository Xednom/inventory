Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}"
new Vue({
  el: '#inventory',
  delimiters: ['${','}'],
  data: {
    items: [],
    loading: true,
    currentItem: {},
    message: null,
    newItem: {'category_items': null, 'brand_name': null, 'size': null, 'price': null},
    search_term: ''
  },
  mounted: function () {
    this.getItems();
  },
  methods: {
    getItems: function() {
      let api_url = '/api/v1/item/';
      if(this.search_term!==''||this.search_term!==null) {
        api_url = `/api/v1/item/?search=${this.search_term}`
      }
      this.loading = false;
      this.$http.get(api_url)
          .then((response) => {
            this.items = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getItem: function(id) {
      this.loading = true;
      this.$http.get(`/api/v1/item/${id}/`)
          .then((response) => {
            this.currentItem = response.data;
            $("#editItemModal").modal('show');
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    addItem: function() {
      this.loading = true;
      this.$http.post('/api/v1/item/', this.newItem)
          .then((response) => {
            this.loading = true;
            $("#addItemModal").modal('hide');
            $('.modal-backdrop').remove();
            this.newItem.category_items = null;
            this.newItem.brand_name = null;
            this.newItem.size = null;
            this.price = null;
            swal("Inventory System", "Added successfully", "success");
            this.getItems();
          })
          .catch((err) => {
            this.loading =true;
            console.log(err);
          })
    },
    updateItem: function() {
      this.loading = true;
      this.$http.put(`/api/v1/item/${this.currentItem.item_id}/`, this.currentItem)
          .then((response) => {
            this.loading = false;
            this.currentItem = response.data;
            // after updating, thide the modal
            $("#editItemModal").modal('hide');
            $('.modal-backdrop').remove();
            swal("Inventory System", "Successfully updated the record", "success");
            this.getItems();
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    deleteItem: function(id) {
      swal({
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover this imaginary file!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          this.loading = true;
          this.$http.delete(`/api/v1/item/${id}/`)
              .then((response) => {
                this.loading = false;
                this.getItems();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
          swal("Poof! Your data file has been deleted!", {
            icon: "success",
          });
        } else {
          swal("Your data is safe!");
        }
      });

    }
  }
});
