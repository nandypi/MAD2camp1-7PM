<template>
  <div class="register-container">
    <div class="register-card">
      <h1>Create Account</h1>

      <form @submit.prevent="RegisterUser">
        <input
          v-model="email"
          type="email"
          placeholder="Your email"
        />

        <input
          v-model="password"
          type="password"
          placeholder="Password"
        />

        <p :class="messageType">{{ message }}</p>

        <button type="submit">Register</button>
      </form>

      <p class="login-link">
        Already have an account?
        <RouterLink to="/login">Login here</RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const email = ref('')
const password = ref('')

const message = ref('Enter your details to register')
const messageType = ref('info')

async function RegisterUser() {
  const res = await fetch('http://127.0.0.1:5000/register', {
    method: 'POST',
    body: JSON.stringify({
      email: email.value,
      password: password.value,
    }),
    headers: {
      'content-type': 'application/json',
    },
  })

  const data = await res.json()

  message.value = data.message

  if (res.ok) {
    messageType.value = 'success'
    email.value = ''
    password.value = ''
  } else {
    messageType.value = 'error'
  }
}
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  margin-top: 80px;
  font-family: Arial, sans-serif;
}

.register-card {
  width: 350px;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h1 {
  margin-bottom: 25px;
  color: #2c3e50;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

input {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 14px;
}

button {
  padding: 12px;
  border: none;
  border-radius: 8px;
  background: #42b883;
  color: white;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background: #369f6e;
}

.login-link {
  margin-top: 20px;
}

.info {
  color: #666;
}

.success {
  color: green;
}

.error {
  color: red;
}
</style>