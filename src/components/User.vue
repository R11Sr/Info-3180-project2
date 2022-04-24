<template>
<div class="d-flex justify-content-center ">
    <div class=" col-9  col-md-6 col-lg-6 col-xl-9 col-xxl-8">
    <div class="container container-outlined d-flex justify-content-start mb-5 ">
      <div class="wrapper pt-1 pe-5 pb-3 ">
        <div class="row d-flex">
          <div class="col-3">
            <img
              :src="message.image"
              :alt="message.fullname"
              id="profilePhoto"
              class="d-inline-block"
            />
          </div>
          <div class="col-9 text-start">
            <div class="container">
              <h1>{{ message.fullname }}</h1>
              <h3 class="text-muted pb-3">@{{ message.username }}</h3>

              <article class="col-10">
                <p class="text-muted">
                  {{ message.biography }}
                </p>
              </article>

              <article>
                <div class="row">
                  <div class="col-2 userInfo text-muted text-start">
                    Email <br />
                    Location <br />
                    Joined
                  </div>

                  <div class="col userInfo text-start">
                    {{ message.email }} <br />
                    {{ message.location }} <br />
                    {{ message.date_joined }}
                  </div>
                </div>
              </article>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Display of  the favorites  -->
    <div class="container row p-0">
        <h1>Cars Favourited</h1>
      <div class="col">
        <div class="card h-100">
          <img
            src="http://placehold.jp/150x150.png"
            class="card-img-top"
            alt="place-holder"
          />
          <div class="card-body">
            <h6 class="card-title d-flex m-0">
              <div class="me-auto">Card title</div>
              <div class="">
                <p class="price">
                  <span><i class="fa fa-tag" aria-hidden="true"></i> </span>
                  $400,000
                </p>
              </div>
            </h6>
            <p class="card-text text-muted pb-5">Model</p>
            <a href="#" class="btn btn-primary">View more details</a>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="card h-100">
          <img
            src=""
            class="card-img-top"
            alt="place-holder"
          />
          <div class="card-body">
            <h6 class="card-title d-flex m-0">
              <div class="me-auto">Card title</div>
              <div class="">
                <p class="price">
                  <span><i class="fa fa-tag" aria-hidden="true"></i> </span>
                  $400,000
                </p>
              </div>
            </h6>
            <p class="card-text text-muted pb-5">Model</p>
            <a href="#" class="btn btn-primary">View more details</a>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="card h-100">
          <img
            src="http://placehold.jp/150x150.png"
            class="card-img-top"
            alt="place-holder"
          />
          <div class="card-body">
            <h6 class="card-title d-flex m-0 m-0">
              <div class="me-auto">Card title</div>
              <div class="">
                <p class="price">
                  <span><i class="fa fa-tag" aria-hidden="true"></i> </span>
                  $400,000
                </p>
              </div>
            </h6>
            <p class="card-text text-muted pb-5">Model</p>
            <a href="#" class="btn btn-primary">View more details</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
  
</template>

<script>
const API = 'http://localhost:8080/api/uploads/';
export default {
  data() {
    return {
      message:{},
    };
  },
  created(){
      fetch(`/api/users/${localStorage.getItem('userId')}`,{
      method:"GET",
     }).then(response =>{
        return response.json();
     }).then(data =>{
       this.message = data;
       this.message['image'] = API + this.message.photo;
     })
  },
  methods:{
    userInfo(){

    }
  }
};
</script>


<style>
.container-outlined {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

#profilePhoto {
  border-radius: 50%;
  width: 12rem;
  height: 12rem;
}

.userInfo {
  line-height: 2;
}
</style>