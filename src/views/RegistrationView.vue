<template>
    <div class = "form">
        <h2>Register New User</h2>
        <Registration />
    </div>   
</template>

<script>
import Registration from '@/components/Registration.vue'
export default {
    data() {
        return {}    
    },
    components: { Registration }
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