<template>
  <nav class="bg-blue-500 p-4">
    <ul class="flex space-x-4">
      <li><router-link to="/" class="text-white">Reservas</router-link></li>
      <li><router-link to="/administradores" class="text-white">Administradores</router-link></li>
      <li><a href="#" class="text-white">Socios</a></li>
      <li><a href="#" class="text-white">Pistas</a></li>
      <li><a href="#" class="text-white">Mis Reservas</a></li>
      <li><a href="#" class="text-white">Register</a></li>
      <li><a href="#" class="text-white">Login</a></li>
      <li><a href="#" class="text-white">Logout</a></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>