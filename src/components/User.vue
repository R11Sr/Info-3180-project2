<template>
<div class="d-flex justify-content-center ">
    <div class=" col-9  col-md-6 col-lg-6 col-xl-9 col-xxl-8">
    <div class="container container-outlined d-flex justify-content-start mb-5 ">
      <div class="wrapper pt-1 pe-5 pb-3 ">
        <div class="row d-flex">
          <div class="col-3">
            <img
              src="@/assets/jessica-felicio-_cvwXhGqG-o-unsplash.jpg"
              alt=""
              id="profilePhoto"
              class="d-inline-block"
            />
          </div>
          <div class="col-9 text-start">
            <div class="container">
              <h1>{{ message.firstname }} {{ message.lastname }}</h1>
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
                    {{ message.Joined }}
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
export default {
  data() {
    return {
      message: {
        firstname: "Danica",
        lastname: "Patrick",
        username: "dparick",
        biography:
          "United Auto Sales provides the  fastest, easiest and most user friendly way to buy or sell cars online. Find a great price on the vehicle you want.",
        email: "email@xampl.com",
        location: "Wisconsin, USA",
        Joined: "April 8, 2022",
        image: "jessica-felicio-_cvwXhGqG-o-unsplash.jpg",
      },
    };
  },
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