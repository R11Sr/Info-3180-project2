<template>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
    integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
    crossorigin="anonymous"
    referrerpolicy="no-referrer"
  />
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid d-flex justify-content-between">
        <div>

        <a class="navbar-brand" href="/"> <span><i class="fa fa-car" aria-hidden="true"></i></span> Unites Auto Sales</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        </div>

        <div>
          <ul class="navbar-nav">
            <li class="nav-item">
          <RouterLink to="/explore" class="nav-link">Explore</RouterLink>
            </li>

             <li class="nav-item">
         <RouterLink to="/cars/new" class="nav-link">Add Car</RouterLink>
            </li>
            

            <li class="nav-item">
          <RouterLink to="/user" class="nav-link">My Profile</RouterLink>
            </li>

            <li class="nav-item">
          <RouterLink to="/logout" class="nav-link">Logout</RouterLink>
            </li>
          </ul>
        </div>

        <div class="collapse " id="navbarSupportedContent" style="">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";
export default{
  data(){
    let id = localStorage.getItem('userId');
  }
}
</script>

<style>
/* Add any component specific styles here */
#navbarSupportedContent{
  display: inline-block;

}
</style>