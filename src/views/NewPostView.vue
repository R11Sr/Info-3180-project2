<template>
    <div class = "form ">
        <NewPost />
    </div>   
</template>

<script>
import NewPost from '@/components/NewPost.vue'
export default {
    data() {
        return {}    
    },
    components: { NewPost }
    };
</script>

<style>
.form{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
</style>