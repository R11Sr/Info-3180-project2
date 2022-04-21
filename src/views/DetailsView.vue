<template>
    <div class = "details">
        <Details />
    </div>   
</template>

<script>
import Details from '@/components/Details.vue'
export default {
    data() {
    return {}    
    },
    components: { Details }
    };
</script>

<style>
.details{
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>