<template>
  <div class="about">
    <h1>FrontEnd</h1>

    <h2 id="message">...</h2>

    <button @click="greetUser()">Call Backend</button>
  </div>
</template>

<script setup>
async function greetUser() {
  let res = await fetch('http://127.0.0.1:5000/hello')
  const data = await res.json()
  let message = document.getElementById("message")
  message.innerText = data.message
}
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    max-height: 80vh;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: space-between;
  }
}
</style>
