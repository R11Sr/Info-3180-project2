<template>
    <div class="container col-md-6 col-lg-6 col-xl-9 col-xxl-8">
        <div class="title">
            <h2>Explore</h2>
        </div>

        <div class="">
            <form action="##to do ##" method="GET" class="d-flex p-2 align-items-end">
                <div class="form-group pe-3">
                    <label for="make">Make</label>
                    <input type="text" name="make" class='form-control' id="make">
                </div>

                <div class="form-group pe-3">
                    <label for="model">Model</label>
                    <input type="text" name="model" class='form-control' id="model">
                </div>

              <button type="submit" name="submit" class="btn btn-success" >Search</button>

            </form>
        </div>

    </div>
</template>

<style>
button{
    width: 10em;
    height:2.5em;
}
</style>