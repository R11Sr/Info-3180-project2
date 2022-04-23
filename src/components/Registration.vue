<template>
    <div class="card" style="width: fit-content;">
        <div class="card-body">
            <form method="POST" enctype="multipart/form-data" id="registerForm" @submit.prevent="register" >
                <div class = "sector">
                    <div class = "data">
                    <label for = "username">Username</label>
                    <input type = "text" name = "username">
                    </div>
                    <div class = "data">
                    <label for = "password" >Password</label>   
                    <input type = "password" name = "password">
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                    <label for = "fullname">Fullname</label>
                    <input type = "text" name = "fullname">
                    </div>
                    <div class = "data">
                    <label for = "email" >Email</label>   
                    <input type = "email" name = "email">
                    </div>
                </div>

                <div class = "sector">
                    <div class = "data">
                    <label for = "location">Location</label>
                    <input type = "text" name = "location">
                    </div>
                    <div class = "data">
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                    <label for = "biography">Biography</label>
                    <textarea name = "biography" rows = "4" cols = "53">
                    </textarea>
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                        <label for="photo">Image: </label>
                        <input type="file" id="image" name="photo"><br><br>
                    </div>
                </div>
                <div class = "sector">
                <div class = "data">
                    <input type="submit" value="Register" class = "btn btn-primary">
                </div>
                </div>
            </form>
    
  </div>
</div>
    
</template>
<script>
export default {
    data() {
        return {
            csrf_token: ''
        }
    },
    created(){
         this.getCsrfToken();
    },
    methods:{
        register(){
            let registerForm = document.getElementById('registerForm');
            let formInfo = new FormData(registerForm);

            fetch('/api/register',{
                method:'POST',
                body: formInfo,
                headers:{
                    'X-CSRFToken': this.csrf_token
                }
            }).then((data)=>{
                return JSON.stringify(data);
            })
            .then((data2)=>{
                console.log(data2);
            })
            .catch((error)=>{
                console.log(error);
            })

        },
        getCsrfToken(){
            let self =this;
            fetch('/api/csrf-token')
          .then(response=>
              response.json())          
          .then(data=>{
            self.csrf_token = data.csrf_token;
          })
        }
    }

}
</script>

<style>
.card{
    display: flex;
    flex-direction: column;

}

.data{
    display: flex;
    flex-direction: column;
    margin: 1rem;
}

.sector{
    display: flex;
    flex-direction: row;
}


</style>