
<template>
    
<div class="container col-md-6">

  <div class="login-form center-block text-white">
    <h2>Login to your account</h2>
    <form action="##to do ##" class="pb-3 col-6" method="POST">

      <div class="form-group pb-3">
          <label for="email">Email:</label>
          <input type="text" name="email" class='form-control' id="email"  placeholder="Enter your email">
      </div>

      <div class="form-group pb-3">
          <label for="password">Password:</label>
          <input type="password" name="password" class='form-control' id="password" >

      </div>
      <button type="submit" name="submit" class="btn btn-primary btn-block" style="width:100%">Log in</button>
    </form>
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
