
<template>
    
<div class="container col-md-6">
    <div id="notification">
    </div>

    <div id="notificationFormError" >
        <ul v-for="(error,index) in notifyErrorArray" :key="index" >
            {{error}}
        </ul>
    </div>

  <div class="login-form container d-flex justify-content-center">
    <div class="container ">
    <h2>Login to your account</h2>

        <form action='' class="p-3 col-md-6 col-lg-6 col-xl-9 col-xxl-8 container-outlined" method="POST" id="loginForm" @submit.prevent='login'>

        <div class="form-group pb-3">
            <label for="Username">Username</label>
            <input type="text" name="username" class='form-control' id="Username"  placeholder="Enter your Username">
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

import router from '../router'

export default{
    data(){
        return {
            csrf_token:'',
            notifySuccess:'',
            notifyErrorArray:[]
        }        
    },
    created(){
        this.getCsrfToken();
    },
    methods:{
        login(){
            let loginForm = document.getElementById('loginForm');

            let loginInfo = new FormData(loginForm);
            let notification = document.getElementById('notification');
            let notificationFormError = document.getElementById('notificationFormError');

            //hide notifications
            notification.style.display = 'none';
            notificationFormError.style.display = 'none';
            notification.className = '';
            notificationFormError.className = '';

            fetch('/api/auth/login',{
                method:"POST",
                body: loginInfo,
                headers:{
                    'X-CSRFToken': this.csrf_token
                }              
            }).then(async (response) =>{
                let data = await response.json();
                let status = response.status;

                switch(status){
                    case 200:
                        this.notifySuccess = data.result;
                        //store user_id in localStorage
                        localStorage.setItem('userId',data.user_id);
                        notification.textContent = this.notifySuccess;
                        notification.style.display = 'block';
                        notification.classList.add('bg-success');
                        setTimeout( function(){
                            router.push({ path: '/' });
                            },4000);
                        break;
                    
                    case 400:
                        if (Array.isArray(data.error)){
                            this.notifyErrorArray = data.error;
                            notificationFormError.style.display = 'block';
                            notificationFormError.classList.add('bg-danger');

                        }
                        break;
                    default:
                        notification.textContent= this.data;
                        notification.style.display = 'block';
                        notification.classList.add('bg-danger');
                }
            })

            .catch((error)=>{
                console.log(error);
                this.notifySuccess = error;
                notification.textContent = this.notifySuccess;
                notification.style.display = 'block';
                notification.classList.add('bg-danger');

            })
        },
        getCsrfToken(){
            fetch('/api/csrf-token')
            .then(response => response.json())
            .then(responseData =>{
                this.csrf_token = responseData.csrf_token;
            })

        },

    }
}
</script>

<style>
.container-outlined{

     box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
</style>
