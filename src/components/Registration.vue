<template>
    <div class="card" style="width: fit-content;">
        <div class="card-body">
            <form>
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
                        <label for="image">Image: </label>
                        <input type="file" id="image" name="image"><br><br>
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
    setup() {
        
    },
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