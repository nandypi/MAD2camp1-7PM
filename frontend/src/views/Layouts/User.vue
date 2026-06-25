<template>
    <div style="display: flex; justify-content: space-between;">
        <h1>User Dashboard</h1>
        <button @click="LogOut">Logout</button>
    </div>
    

    <h2>Items Display</h2>

    <ul>
        <li v-for="item in items">
            <h3>{{item.name}}</h3>
            <p>{{item.description}}</p>
            <img :src="item.image_url" alt="">
        </li>
    </ul>

</template>


<script>

export default {
    data () {
        return {
            message: "hey welcome user",
            items: []
        }
    },
    methods: {
        async loadItems() {
            const res = await fetch('http://127.0.0.1:5000/items', {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            })
            const data = await res.json()
            console.log(res)
            if (res.ok) {
                console.log(data)
                this.items = data.items
            } else if ([401].includes(res.status)) {
                localStorage.removeItem('token')
                localStorage.removeItem('user')
                this.$router.push('/login')
            }
        },
        LogOut(){
            if (confirm("Are you sure about logging out?")) {
                localStorage.removeItem('token')
                localStorage.removeItem('user')
                this.$router.push('/login')
            }
        }
    },
    mounted() {
        this.loadItems()
    }
}
</script>