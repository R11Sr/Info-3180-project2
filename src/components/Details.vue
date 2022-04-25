<template>
  <div class="container col-md-8 container-outlined">
    <div class="wrapper">
      <div class="row">
        <div class="col-4">
          <img
            :src="url"
            class="h-100 w-100 d-inline-block"
            alt="result.model"
          />
        </div>
        <div class="col-8">
          <div class="container p-2">
            <div class="h3">{{ result.year }} {{ result.make }}</div>
            <div>
              <h5 class="text-muted">{{ result.model }}</h5>
            </div>

            <div class="pb-3 text-muted">
              {{ result.description }}
            </div>
            <article>
              <div class="row mb-5 pb-5">
                <div class="col-4 text-start">
                  Color {{ result.colour }} <br />
                  Price {{ result.price }}
                </div>

                <div class="col-8 text-start">
                  Body Type {{ result.car_type }} <br />
                  Transmission {{ result.transmission }}
                </div>
              </div>
            </article>

            <div class="d-flex">
              <div class=" w-100">
                <button class="btn btn-primary">Contact Owner</button>
              </div>
              <div class="flex-shrink-1"><i @click="highlight" id="fav"></i></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>

const API = "http://localhost:8080/api/uploads/";

let fav = document.getElementsByTagName("i")[0];
fav.addEventListener("click", function handleClick(event) {
  event.target.classList.add("press");
});

export default {
  data() {
    return {
      result: {},
      url: "",
      csrf_token: "",
      error: {},
    };
  },
  created() {

    let self = this;
    this.getCsrfToken();
    let id = this.$route.params.id;
    fetch("/api/cars/" + id.toString(), {
      method: "GET",
      headers: { "X-CSRFToken": this.csrf_token },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        // display a success message
        console.log(data);
        self.result = data;
        self.url = API + self.result.photo;
        console.log(self.url);
      })
      .catch(function (error) {
        console.log(error);
        self.error = error.result;
      });
  },
  methods: {
    getCsrfToken() {
      let self = this;
      fetch("/api/csrf-token")
        .then((response) => response.json())
        .then((data) => {
          self.csrf_token = data.csrf_token;
        });
    },
    highlight(event){
         event.target.classList.add("press");
        let id =  JSON.parse(JSON.stringify(this.result)).id
        console.log(id)
         fetch(`/api/cars/${id}/favourite`,{
            method: "POST",
            headers:{"Content-Type": "application/json; charset=UTF-8"},
            body:JSON.stringify({car_fav:`${id}`}),
            headers: { "X-CSRFToken": this.csrf_token },
         }).then(async (response)=>{
             let data = await response.json();
            let status = response.status;

            console.log(data);

         })
    },
  },
};
</script>

<style >
.container-outlined {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}


#fav {
  cursor:pointer;
  padding:10px 12px 8px;
  background:#fff;
  border-radius:50%;
  display:inline-block;
  margin:0 0 15px;
  color:#aaa;
  transition:.2s;
  margin-top: 1rem;
}
#fav:hover {
  color:#666;
}
#fav:before {
  font-family:fontawesome;
  content:'\f004';
  font-style:normal;
}
#fav.press {
  animation: size .4s;
  color:#e23b3b;
}
</style>