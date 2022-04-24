<template>

<div class="container col-md-6 col-lg-6 col-xl-9 col-xxl-8 mx-auto">
        <h2 style="text-align: center;">Add New Car</h2>
    <div id="notification" class=""  style="text-align: center;"></div>

    <div id="notificationFormError" >
      <ul style="text-align: center;" v-for="(error, index) in notifyErrorArray" :key="index">
        {{
          error
        }}
      </ul>
    </div>

  <div class="pt-3 d-flex justify-content-center" >

  <div class="card " style="width: fit-content">
      
    <div class="card-body">
      <form
        id="npForm"
        method="POST"
        @submit.prevent="newPostForm"
        enctype="multipart/form-data"
      >
        <div class="sector">
          <div class="data">
            <label for="make">Make</label>
            <input type="text" name="make" class="form-control" id="make" />
          </div>
          <div class="data">
            <label for="model">Model</label>
            <input type="text" name="model" class="form-control" id="model" />
          </div>
        </div>
        <div class="sector">
          <div class="data">
            <label for="color">Colour</label>
            <input type="text" name="color" class="form-control" id="colour" />
          </div>
          <div class="data">
            <label for="year">Year</label>
            <input type="text" name="year" class="form-control" id="year" />
          </div>
        </div>

        <div class="sector">
          <div class="data">
            <label for="price">Price</label>
            <input type="text" name="price" class="form-control" id="price" />
          </div>
          <div class="data">
            <label for="Car_Type">Car Type</label>
            <select name="Car_Type" id="Car_Type">
              <option value="SUV">SUV</option>
              <option value="COUP">COUP</option>
              <option value="HATCH BACK">HATCH BACK</option>
              <option value="SEDAN">SEDAN</option>
              <option value="STATION WAGON">STATION WAGON</option>
            </select>
          </div>
        </div>
        <div class="sector">
          <div class="data">
            <label for="transmission">Transmission</label>
            <select name="transmission" id="transmission">
              <option value="MANUAL">MANUAL</option>
              <option value="AUTOMATIC">AUTOMATIC</option>
            </select>
          </div>
        </div>
        <div class="sector">
          <div class="data">
            <label for="description">Description</label>
            <textarea
              name="description"
              rows="4"
              cols="53"
              class="form-control"
              id="description"
            >
            </textarea>
          </div>
        </div>
        <div class="sector">
          <div class="data">
            <label for="photo">Upload Photo </label>
            <input type="file" id="photo" name="photo" /><br /><br />
          </div>
        </div>
        <div class="sector">
          <div class="data">
            <input type="submit" value="Save" class="btn btn-primary" />
          </div>
        </div>
      </form>
    </div>
  </div>
  </div>
</div>
</template>

<script>
import router from '../router'

export default {
  data() {
    return {
      message: "",
      notifySuccess:'',
      notifyErrorArray: [],
      csrf_token: "",
    };
  },
  methods: {
    newPostForm() {
      let npForm = document.getElementById("npForm");
      let notification = document.getElementById('notification');
      let notificationFormError = document.getElementById('notificationFormError');

      //hide notifications
      notification.style.display = 'none';
      notificationFormError.style.display = 'none';
      notification.className = '';
      notificationFormError.className = '';      

      let form_data = new FormData(npForm);
      let self = this;
      fetch("/api/cars", {
        method: "POST",
        body: form_data,
        headers: { "X-CSRFToken": this.csrf_token },
      })
        .then(async (response)=> {
          let data = await response.json();
          let status = response.status;

          switch(status){
              case 200:
                this.notifySuccess = data.message;
                notification.textContent = this.notifySuccess;
                notification.style.display = 'block';
                notification.classList.add('bg-success');
                npForm.reset()
                setTimeout( function(){
                   router.push({ path: '/explore' });
                    },3000);
                break;

                case 400:
                    if (Array.isArray(data.error)){
                        this.notifyErrorArray = data.error;
                        notificationFormError.style.display = 'block';
                        notificationFormError.classList.add('bg-danger');
                    }
                    break;
                default:
                    notification.textContent= this.data;
                    notification.style.display = 'block';
                    notification.classList.add('bg-danger');                
          }
        })
      
        .catch(function (error) {
            console.log(error);
            this.notifySuccess = error;
             notificationFormError.textContent = this.notifySuccess;
             notificationFormError.style.display = 'block';
             notificationFormError.classList.add('bg-danger');          
        });
    },

    getCsrfToken() {
      let self = this;
      fetch("/api/csrf-token")
        .then((response) => response.json())
        .then((data) => {
          self.csrf_token = data.csrf_token;
        });
    },
  },
  created() {
    this.getCsrfToken();
  },
};
</script>

<style>
.card {
  display: flex;
  flex-direction: column;
}
.data {
  display: flex;
  flex-direction: column;
  margin: 1rem;
}
.sector {
  display: flex;
  flex-direction: row;
}
</style>