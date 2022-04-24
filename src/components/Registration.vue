<template>
    <div class="card" style="width: fit-content;">
        <div class="card-body">
            <form id = "regForm" method = 'POST' @submit.prevent="registrationForm" enctype="multipart/form-data">
                <div class = "sector">
                    <div class = "data">
                    <label for = "username">Username</label>
                    <input type = "text" name = "username" id = "username">
                    </div>
                    <div class = "data">
                    <label for = "password" >Password</label>   
                    <input type = "password" name = "password" id = "password">
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                    <label for = "fullname">Fullname</label>
                    <input type = "text" name = "fullname" id = "fullname" >
                    </div>
                    <div class = "data">
                    <label for = "email" >Email</label>   
                    <input type = "email" name = "email" id = "email">
                    </div>
                </div>

                <div class = "sector">
                    <div class = "data">
                    <label for = "location">Location</label>
                    <input type = "text" name = "location" id = "location">
                    </div>
                    <div class = "data">
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                    <label for = "biography">Biography</label>
                    <textarea id = "biography" name = "biography" rows = "4" cols = "53">
                    </textarea>
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                        <label for="photo">Image: </label>
                        <input type="file" id="photo" name="photo"><br><br>
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
export default{
   data() {
        return {
            message:'',
            errors:[],
            csrf_token:''
        }
    },
    methods: {
            
            registrationForm(){
            let regForm = document.getElementById('regForm');
            let form_data = new FormData(regForm);
            let self = this;
            fetch("/api/register", {
            method: 'POST',
            body:form_data,
            headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
            return response.json();
            })
            .then(function (data) {
            // display a success message
            console.log(data);
            self.message = data.message
            
            })
            .catch(function (error) {
            console.log(error);
            self.errors = error
            
        });
        },
            
            getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
            console.log(data);
            self.csrf_token = data.csrf_token;
            });
        }
    }
    ,
        created() {
            this.getCsrfToken();
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