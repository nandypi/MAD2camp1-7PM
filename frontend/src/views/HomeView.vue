<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="home-container">
    <h1>Welcome to Our App</h1>

    <p>
      Want to know more about us?
      <RouterLink to="/about">Click here</RouterLink>
    </p>

    <div class="buttons">
      <RouterLink to="/login" class="btn">Login</RouterLink>

      <RouterLink to="/register" class="btn secondary">
        Register
      </RouterLink>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  text-align: center;
  margin-top: 100px;
  font-family: Arial, sans-serif;
}

h1 {
  color: #2c3e50;
  margin-bottom: 15px;
}

p {
  margin-bottom: 30px;
  font-size: 18px;
}

.buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
}

.btn {
  text-decoration: none;
  background-color: #42b883;
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  transition: 0.3s;
}

.btn:hover {
  background-color: #369f6e;
}

.secondary {
  background-color: #35495e;
}

.secondary:hover {
  background-color: #2c3e50;
}
</style>