<template>
<div class="page">

    <header class="header">
        <h2>Admin Dashboard</h2>
        <button class="logout" @click="LogOut">Logout</button>
    </header>

    <div class="form-card">
        <h3>Add Product</h3>

        <form @submit.prevent="CreateItem">
            <input v-model="newItem.name" placeholder="Product Name" required>
            <textarea v-model="newItem.description" placeholder="Description" ></textarea>
            <input v-model="newItem.image_url" placeholder="Image URL">

            <button class="add-btn">Add Product</button>
        </form>
    </div>

    <div class="products">

        <div class="card" v-for="item in items" :key="item.id">

            <img :src="item.image_url">

            <h3>{{ item.name }}</h3>

            <p>{{ item.description }}</p>

            <div class="actions">
                <button class="edit" @click="openEdit(item)">Edit</button>
                <button class="delete" @click="DeleteItem(item.id)">Delete</button>
            </div>

        </div>

    </div>

    <!-- Popup -->

    <div class="overlay" v-if="showEdit">

        <div class="popup">

            <h3>Edit Product</h3>

            <input v-model="editItem.name">

            <textarea v-model="editItem.description"></textarea>

            <input v-model="editItem.image_url">

            <div class="popup-buttons">
                <button class="edit" @click="UpdateItem">Save</button>
                <button @click="showEdit=false">Cancel</button>
            </div>

        </div>

    </div>

</div>
</template>

<script>
export default {

data(){
return{
items:[],

newItem:{
name:"",
description:"",
image_url:""
},

showEdit:false,

editItem:{
id:null,
name:"",
description:"",
image_url:""
}
}
},

methods:{

async loadItems(){

const res=await fetch("http://127.0.0.1:5000/items",{
headers:{
Authorization:`Bearer ${localStorage.getItem("token")}`
}
})

const data=await res.json()

if(res.ok)
this.items=data.items

},

async CreateItem(){

const res=await fetch("http://127.0.0.1:5000/items",{

method:"POST",

headers:{
"Content-Type":"application/json",
Authorization:`Bearer ${localStorage.getItem("token")}`
},

body:JSON.stringify(this.newItem)

})

if(res.ok){

this.newItem={name:"",description:"",image_url:""}

this.loadItems()

}

},

openEdit(item){

this.editItem={...item}

this.showEdit=true

},

async UpdateItem(){

const res=await fetch(`http://127.0.0.1:5000/items/${this.editItem.id}`,{

method:"PUT",

headers:{
"Content-Type":"application/json",
Authorization:`Bearer ${localStorage.getItem("token")}`
},

body:JSON.stringify(this.editItem)

})

if(res.ok){

this.showEdit=false

this.loadItems()

}

},

async DeleteItem(id){

if(!confirm("Delete this product?")) return

const res=await fetch(`http://127.0.0.1:5000/items/${id}`,{

method:"DELETE",

headers:{
Authorization:`Bearer ${localStorage.getItem("token")}`
}

})

if(res.ok)
this.loadItems()

},

LogOut(){

localStorage.clear()

this.$router.push("/login")

}

},

mounted(){

    const user = JSON.parse(localStorage.getItem('user'))
    if (user.role != 'admin') {
        alert("You do not have previlage to be here")
        if (user.role == 'user') {
            this.$router.push('/user')
        }
    }

    this.loadItems()

}

}
</script>

<style scoped>

body{
margin:0;
}

.page{
background:#f1f3f6;
min-height:100vh;
padding:30px;
font-family:Arial;
}

.header{
display:flex;
justify-content:space-between;
align-items:center;
background:#2874f0;
padding:18px 25px;
color:white;
border-radius:10px;
margin-bottom:25px;
}

.logout{
background:white;
color:#2874f0;
}

.form-card{
background:white;
padding:20px;
border-radius:10px;
box-shadow:0 3px 10px rgba(0,0,0,.1);
margin-bottom:30px;
}

form{
display:flex;
flex-direction:column;
gap:12px;
}

input,textarea{
padding:12px;
border:1px solid #ddd;
border-radius:8px;
font-size:15px;
}

button{
border:none;
padding:12px;
border-radius:8px;
cursor:pointer;
font-weight:bold;
transition:.3s;
}

.add-btn{
background:#2874f0;
color:white;
}

.add-btn:hover{
background:#1565c0;
}

.products{
display:grid;
grid-template-columns:repeat(auto-fill,minmax(250px,1fr));
gap:20px;
}

.card{
background:white;
padding:15px;
border-radius:12px;
box-shadow:0 4px 12px rgba(0,0,0,.08);
transition:.3s;
}

.card:hover{
transform:translateY(-5px);
}

.card img{
width:100%;
height:180px;
object-fit:cover;
border-radius:8px;
}

.actions{
display:flex;
justify-content:space-between;
margin-top:15px;
}

.edit{
background:#2874f0;
color:white;
}

.delete{
background:#e53935;
color:white;
}

.overlay{
position:fixed;
inset:0;
background:rgba(0,0,0,.5);
display:flex;
justify-content:center;
align-items:center;
}

.popup{
background:white;
padding:25px;
width:380px;
border-radius:12px;
display:flex;
flex-direction:column;
gap:10px;
}

.popup-buttons{
display:flex;
justify-content:flex-end;
gap:10px;
margin-top:10px;
}

</style>