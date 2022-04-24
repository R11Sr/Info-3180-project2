<template>
<div class="card d-card" style="width: 60%; min-height:100%">
  <div class = "car">
     <img :src="url" class="card-img-top" alt={{result.model}}>
  </div>
 
  
  <div class="card-body my-card">
    <div class = "title">
    <h5 class="card-title">{{result.year}} {{result.make}}</h5>
    <h6>{{result.model}}</h6>
    <p class="card-text">{{result.description}}</p>
    </div>
    <div class = "body-end">
        <div class = "be-left">
            <div class = "info">
            <label for="colour">Colour: </label>
            <p name = "colour">{{result.colour}}</p>
            </div>
            <div class = "info">
            <label for="price">Price: </label>
            <p name = "price">{{result.price}}</p>
            </div>
        </div>
        <div class = "be-right">
            <div class = "info">
            <label for="body-type">Body Type: </label>
            <p name = "body-type">{{result.car_type}}</p>
            </div>
            <div class = "info">
            <label for="transmission">Transmission: </label>
            <p name = "transmission">{{result.transmission}}</p>
            </div>

        </div>

    </div>
    <div class = "button-end">
    
    <a href="#" class="btn btn-primary">Contact Owner</a>
    <i></i>
    </div>
        
    </div>
    
  
</div>
    
</template>
<script>
const API = 'http://localhost:8080/api/uploads/';
  let fav = document.getElementsByTagName("i")[0]

  fav.addEventListener('click', function handleClick(event) {
    event.target.classList.add('press');
});


  
export default {
    
    data() {
      return{
        result: {},
        url:'',
        csrf_token:'',
        error:{}
      };
    },
    created(){
            fav.addEventListener('click', function handleClick(event) {
            event.target.classList.add('press');
            });
            let self = this;
            this.getCsrfToken();
            let id = this.$route.params.id
            fetch("/api/cars/"+id.toString(), {
            method: 'GET',
            headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
            return response.json();
            })
            .then(function (data) {
            // display a success message
            console.log(data);
            self.result = data;
            self.url = API+self.result.photo
            console.log(self.url);
            })
            .catch(function (error) {
            console.log(error);
            self.error = error.result;
           });
    },

    methods:{
      
            
            getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
            console.log(data);
            self.csrf_token = data.csrf_token;
            });
        }
    },


}
</script>
<style>
.my-card {
    display: flex;
    flex-direction: column;
    align-items: flex-start;}
.title{
  margin-bottom:1rem;
}
.details{
  min-width:100%;
  min-height:450px;
  }
.d-card {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: fit-content;
}
.car {
  display: flex;
  flex-flow: column;
  height: 100%;
  max-width: 60%;
  overflow: hidden;
  min-height:100%;
 
  border-bottom-left-radius: calc(0.25rem - 1px);

}
img{
  height:450px;
}
main{
  height:450px;
}

.card-title {
  font-weight: bold;
}

.body-end{
    display: flex;
    flex-direction: row;
}
.be-left,.be-right{
    display: flex;
    flex-direction: column;
    margin-right: 1rem;
}
.info>*{
  margin-bottom:1rem;
}
.info{
  margin-bottom: 10%;
}

i {
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

i:hover {
  color:#666;
}

i:before {
  font-family:fontawesome;
  content:'\f004';
  font-style:normal;
}



i.press {
  animation: size .4s;
  color:#e23b3b;
}


</style>