<template>
    <div class="card" style="width: fit-content;">
        <div class="card-body">
            <form id = "npForm" method = 'POST' @submit.prevent="newPostForm" enctype="multipart/form-data">
                <div class = "sector">
                    <div class = "data">
                    <label for = "make">Make</label>
                    <input type = "text" name = "make" class="form-control" id = "make">
                    </div>
                    <div class = "data">
                    <label for = "model" >Model</label>   
                    <input type = "text" name = "model" class="form-control" id = "model">
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                    <label for = "colour">Colour</label>
                    <input type = "text" name = "colour" class="form-control" id = "colour">
                    </div>
                    <div class = "data">
                    <label for = "year" >Year</label>   
                    <input type = "text" name = "year" class="form-control" id = "year">
                    </div>
                </div>

                <div class = "sector">
                    <div class = "data">
                        <label for = "price">Price</label>
                        <input type = "text" name = "price" class="form-control" id = "price">
                    </div>
                    <div class = "data">
                        <label for = "Car_Type">Car Type</label>
                        <select name = "Car_Type" id = "Car_Type">
                            <option value = "SUV">SUV</option>
                            <option value = "COUP">COUP</option>
                            <option value = "HATCH BACK">HATCH BACK</option>
                            <option value = "SEDAN">SEDAN</option>
                            <option value = "STATION WAGON">STATION WAGON</option>
                        </select>
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                        <label for = "transmission">Transmission</label>
                        <select name = "transmission" id = "transmission">
                            <option value = "MANUAL">MANUAL</option>
                            <option value = "AUTOMATIC">AUTOMATIC</option>
                        </select>
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                    <label for = "description">Description</label>
                    <textarea name = "description" rows = "4" cols = "53" class="form-control" id = "description">
                    </textarea>
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                        <label for="photo">Upload Photo </label>
                        <input type="file" id="photo" name="photo"><br><br>
                    </div>
                </div>
                <div class = "sector">
                <div class = "data">
                    <input type="submit" value="Save" class = "btn btn-primary">
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
            message:'',
            errors:[],
            csrf_token:''
        }
    },
    methods: {
            
            newPostForm(){
            let npForm = document.getElementById('npForm');
            let form_data = new FormData(npForm);
            let self = this;
            fetch("/api/cars", {
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