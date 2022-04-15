
<template>
    
<div class="container col-md-6">

  <div class="login-form container d-flex justify-content-center">
    <div class="container ">
    <h2>Login to your account</h2>

        <form action="##to do ##" class="p-3 col-md-6 col-lg-6 col-xl-9 col-xxl-8 container-outlined" method="POST">

        <div class="form-group pb-3">
            <label for="Username">Username</label>
            <input type="text" name="Username" class='form-control' id="Username"  placeholder="Enter your Username">
        </div>

        <div class="form-group pb-3">
            <label for="password">Password</label>
            <input type="password" name="password" class='form-control' id="password" >

        </div>
        <button type="submit" name="submit" class="btn btn-success btn-block" style="width:100%">Login</button>
        </form>
    </div>
  </div>
</div>
</template>

<script>

export default{
    data(){
        return {
            csrf_token:''
        }
    },
    created(){
        this.getCsrfToken();
    },
    methods:{
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
.container-outlined{
    /* border-style: solid; */
    /* border-radius: 1em; */
    /* border-width: .15em; */
    /* border-color: gray; */
     box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
</style>
