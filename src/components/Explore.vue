<template>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
    integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
    crossorigin="anonymous"
    referrerpolicy="no-referrer"
  />
  <div class="container col-md-6 col-lg-6 col-xl-9 col-xxl-8">
    <div class="title">
      <h2>Explore</h2>
    </div>

    <div class="container-outlined">
      <form
        action="##to do ##"
        method="GET"
        class="d-flex mt-5 mb-5 pt-4 pe-5 pb-5 ps-5 align-items-end"
      >
        <div class="form-group pe-3">
          <label for="make">Make</label>
          <input type="text" name="make" class="form-control" id="make" />
        </div>

        <div class="form-group pe-3">
          <label for="model">Model</label>
          <input type="text" name="model" class="form-control" id="model" />
        </div>

        <button type="submit" name="submit" class="btn btn-success">
          Search
        </button>
      </form>
    </div>

    <!-- Display of  the results  -->
    <div class="container row p-0">

      <div class="col">
        <div class="card h-100" >
          <img
            src="http://placehold.jp/150x150.png"
            class="card-img-top "
            alt="place-holder"
          />
          <div class="card-body">
            <h6 class="card-title d-flex m-0">
              <div class="me-auto">Card title</div>
              <div class="">
                <p class="price">
                  <span><i class="fa fa-tag" aria-hidden="true"></i> </span
                  >  $400,000
                </p>
              </div>
            </h6>
            <p class="card-text text-muted pb-5">Model</p>
            <a href="#" class="btn btn-primary">View more details</a>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="card h-100" >
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
                  <span><i class="fa fa-tag" aria-hidden="true"></i> </span
                  >  $400,000
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
                  <span><i class="fa fa-tag" aria-hidden="true"></i> </span
                  >  $400,000
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
</template>

<style>
button {
  width: 10em;
  height: 2.5em;
}

.container-outlined {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.price{
    border-radius: 15px;
    height: 25px;
    padding-top: 4px;
    padding-bottom: 4px;
    padding-left: 8px;
    padding-right: 8px;
    background: #1fb989;
    color: white;

}

.card-body{
    line-height: 80%;
}

</style>