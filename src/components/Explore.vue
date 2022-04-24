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
        action=""
        method="GET"
        class="d-flex mt-5 mb-5 pt-4 pe-5 pb-5 ps-5 align-items-end"
        id="searchForm"
        @submit.prevent = 'search'
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
    <div class="container d-flex flex-wrap row p-0" >

      
      <div class="col-4 pb-3" v-for="(vehicle,index) in vehicleList" :key="index">
        <div class="card h-100" >
          <img
            :src="vehicle.image"
            class="card-img-top "
            alt="place-holder"
          /> 
          <div class="card-body">
            <h6 class="card-title d-flex m-0">
              <div class="me-auto">{{vehicle.year}} {{vehicle.make.replace(/^\w/, (c) => c.toUpperCase())}}</div>
              <div class="">
                <p class="price">
                  <span><i class="fa fa-tag" aria-hidden="true"></i> </span
                  >  ${{vehicle.price}}
                </p>
              </div>
            </h6>
            <p class="card-text text-muted pb-5">{{vehicle.model.replace(/^\w/, (c) => c.toUpperCase())}}</p>
            <a href="#" class="btn btn-primary">View more details</a>
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
    return{
      vehicleList:[],
      csrf_token:''
    }
    
  },
  created(){
    this.getCsrfToken();
    fetch("/api/cars", {
        method: "GET",
      }).then(async(response)=>{
        let data = await response.json();
        let status = response.status;
        
        //  use Slice -3 to get the last 3 vehicles
        data = data.result.slice(-3);

        //set the full path of each image
        data.forEach(veh =>{
          veh['image'] = API + veh.photo;
        });

        switch (status){
          case 200:
              this.vehicleList = data;
            break;

          case 404:

            break;
          
          default:

        }
        

      }).catch(error =>{
        console.log(error);
      })
  },
  methods:{
    search(){
      let searchdata = new FormData(document.getElementById('searchForm'));
      
      fetch(`/api/search?make=${document.getElementById('make').value}&model=${document.getElementById('model').value}`,{
        method: "GET",
        headers:{
            'X-CSRFToken': this.csrf_token
        }        
      }).then( async (response)=>{
        let data = await response.json();
        data = data.result;
        console.log(data);

        //set the full path of each image
        data.forEach(veh =>{
          veh['image'] = API + veh.photo;
        });

        this.vehicleList = data;

      })
    },
        getCsrfToken(){
            fetch('/api/csrf-token')
            .then(response => response.json())
            .then(responseData =>{
                this.csrf_token = responseData.csrf_token;
            })

        }    
  }
}
</script>

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

img{
  width: 12rem;
  height: 10rem;
}

</style>