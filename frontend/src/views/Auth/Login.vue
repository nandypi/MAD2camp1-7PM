<template>
  <div class="login-container">
    <div class="login-card">
      <h1>Login to Continue</h1>

      <form @submit.prevent="LoginUser">
        <input
          v-model="email"
          required
          type="email"
          name="email"
          id="email"
          placeholder="Your email"
        />

        <input
          v-model="password"
          required
          type="password"
          name="password"
          id="password"
          placeholder="Password..."
        />

        <p :class="messageType">{{ message }}</p>

        <button type="submit">Login</button>
      </form>

      <p class="register-link">
        Don't have an account?
        <RouterLink to="/register">Register here</RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import router from '@/router'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

const email = ref('')
const password = ref('password')

const message = ref('Enter details to Submit')
const messageType = ref('info')

async function LoginUser() {
//   console.log(email.value, password.value)

  const res = await fetch('http://127.0.0.1:5000/login', {
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
    localStorage.setItem('user', JSON.stringify(data.user))
    localStorage.setItem('token', data.access_token)
    message.value += ", Redirecting to dashboard..."
    setTimeout(() => {
      if (data.user.role == "admin") {
        router.push('/admin')
      } else (
        router.push('/user')
      )
    }, 3000);
  } else {
    messageType.value = 'error'
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  margin-top: 80px;
  font-family: Arial, sans-serif;
}

.login-card {
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

.register-link {
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