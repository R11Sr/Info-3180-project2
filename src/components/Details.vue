<template>
<div class="card" style="width: 18rem;">
  <img src="https://static.cargurus.com/images/article/2017/01/19/13/31/2018_tesla_model_3_preview_overview-pic-5194843292684011956-1600x1200.jpeg" class="card-img-top" alt="2018 tesla">
  <div class="card-body">
    <h5 class="card-title">2018 Tesla</h5>
    <h6>Model S</h6>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <div class = "body-end">
        <div class = "be-left">
            <div class = "info">
            <label for="colour">Colour: </label>
            <p name = "colour">Red</p>
            </div>
            <div class = "info">
            <label for="price">Price: </label>
            <p name = "price">$62,288</p>
            </div>
        </div>
        <div class = "be-right">
            <div class = "info">
            <label for="body-type">Body Type: </label>
            <p name = "body-type">Sedan</p>
            </div>
            <div class = "info">
            <label for="transmission">Transmission: </label>
            <p name = "transmission">Automatic</p>
            </div>

        </div>
        
    </div>
    <div class = "card-footer">
    <a href="#" class="btn btn-primary">Contact Owner</a>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
    </svg>
    </div>
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
.card {
  flex-direction: row;
  align-items: center;
  width: fit-content;
}
.card img {
  width: 30%;
  border-top-right-radius: 0;
  border-bottom-left-radius: calc(0.25rem - 1px);
}

.card-title {
  font-weight: bold;
}

.body-end{
    display: flex;
    flex-direction: row;
}
.be-left,.be-right{
    display: flex;
    flex-direction: column;
    margin-right: 1rem;
}

</style>