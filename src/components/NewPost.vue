<template>
    <div class="card" style="width: fit-content;">
        <div class="card-body">
            <form>
                <div class = "sector">
                    <div class = "data">
                    <label for = "make">Make</label>
                    <input type = "text" name = "make" class="form-control">
                    </div>
                    <div class = "data">
                    <label for = "model" >Model</label>   
                    <input type = "text" name = "model" class="form-control">
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                    <label for = "colour">Colour</label>
                    <input type = "text" name = "colour" class="form-control">
                    </div>
                    <div class = "data">
                    <label for = "year" >Year</label>   
                    <input type = "text" name = "year" class="form-control">
                    </div>
                </div>

                <div class = "sector">
                    <div class = "data">
                        <label for = "price">Price</label>
                        <input type = "text" name = "price" class="form-control">
                    </div>
                    <div class = "data">
                        <label for = "car-type">Car Type</label>
                        <select name = "car-type">
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
                        <select name = "transmission">
                            <option value = "MANUAL">MANUAL</option>
                            <option value = "AUTOMATIC">AUTOMATIC</option>
                        </select>
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                    <label for = "description">Description</label>
                    <textarea name = "description" rows = "4" cols = "53" class="form-control">
                    </textarea>
                    </div>
                </div>
                <div class = "sector">
                    <div class = "data">
                        <label for="image">Upload Photo </label>
                        <input type="file" id="image" name="image"><br><br>
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