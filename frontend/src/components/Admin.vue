<template>
  <div>
    <Navbar />
    <h1 class="text-2xl mb-4 text-center">Administradores</h1>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <div 
        v-for="admin in administradores" 
        :key="admin.id" 
        class="card bg-cream p-4 mb-4"
        @click="editAdmin(admin)"
      >
        <p class="truncate">{{ admin.nombre }}</p>
      </div>
    </div>
    <div v-if="editMode" class="card bg-cream p-4 mb-4">
      <p>Editar Administrador</p>
      <form @submit.prevent="updateAdmin">
        <input 
          id="edit-nombre" 
          name="edit-nombre" 
          v-model="currentAdmin.nombre" 
          placeholder="Nombre" 
          class="mb-2 p-2 border rounded"
        />
        <input 
          id="edit-password" 
          name="edit-password" 
          v-model="currentAdmin.password" 
          type="password" 
          placeholder="Password" 
          class="mb-2 p-2 border rounded"
        />
        <div class="flex space-x-2">
          <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Guardar</button>
          <button @click="cancelEdit" type="button" class="bg-blue-500 text-white px-4 py-2 rounded">Cancelar</button>
          <button @click="deleteAdmin(currentAdmin.id)" type="button" class="bg-red-500 text-white px-4 py-2 rounded">Eliminar</button>
        </div>
      </form>
    </div>
    <div class="flex justify-center">
      <div class="card bg-cream p-4 mb-4" style="width: 100%; max-width: 400px;">
        <p>Nuevo Administrador</p>
        <form @submit.prevent="createAdmin">
          <input 
            id="nombre" 
            name="nombre" 
            v-model="newAdmin.nombre" 
            placeholder="Nombre" 
            class="mb-2 p-2 border rounded w-full"
          />
          <input 
            id="password" 
            name="password" 
            v-model="newAdmin.password" 
            type="password" 
            placeholder="Password" 
            class="mb-2 p-2 border rounded w-full"
          />
          <div class="flex space-x-2">
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Crear</button>
            <button type="button" @click="cancelCreate" class="bg-blue-500 text-white px-4 py-2 rounded">Cancelar</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted } from 'vue'
import Navbar from './Navbar.vue'

export default {
  name: 'Admin',
  components: {
    Navbar,
  },
  setup() {
    const administradores = ref([])
    const newAdmin = ref({ nombre: '', password: '' })
    const editMode = ref(false)
    const currentAdmin = ref({})

    const fetchAdministradores = async () => {
      try {
        const response = await fetch('http://localhost:8000/administradores')
        if (!response.ok) throw new Error('Failed to fetch')
        administradores.value = await response.json()
        resetNewAdmin()  // Resetear los campos al obtener la lista de administradores
      } catch (error) {
        console.error('Error:', error)
        alert('Error al conectar con el servidor')
      }
    }

    const createAdmin = async () => {
      try {
        const response = await fetch('http://localhost:8000/administradores', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(newAdmin.value)
        })
        if (!response.ok) {
          const data = await response.json()
          alert(`Error al crear el administrador: ${data.detail}`)
        } else {
          fetchAdministradores()
          resetNewAdmin()  // Limpiar los campos de entrada después de crear un administrador
        }
      } catch (error) {
        console.error('Error:', error)
        alert('Error al conectar con el servidor')
      }
    }

    const editAdmin = (admin) => {
      currentAdmin.value = { ...admin }
      editMode.value = true
    }

    const updateAdmin = async () => {
      try {
        const response = await fetch(`http://localhost:8000/administradores/${currentAdmin.value.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(currentAdmin.value)
        })
        if (!response.ok) {
          const data = await response.json()
          alert(`Error al actualizar el administrador: ${data.detail}`)
        } else {
          fetchAdministradores()
          cancelEdit()
        }
      } catch (error) {
        console.error('Error:', error)
        alert('Error al conectar con el servidor')
      }
    }

    const deleteAdmin = async (id) => {
      try {
        const response = await fetch(`http://localhost:8000/administradores/${id}`, {
          method: 'DELETE'
        })
        if (!response.ok) {
          const data = await response.json()
          alert(`Error al eliminar el administrador: ${data.detail}`)
        } else {
          fetchAdministradores()
        }
      } catch (error) {
        console.error('Error:', error)
        alert('Error al conectar con el servidor')
      }
    }

    const cancelEdit = () => {
      editMode.value = false
      currentAdmin.value = {}
    }

    const cancelCreate = () => {
      resetNewAdmin()
    }

    const resetNewAdmin = () => {
      newAdmin.value = { nombre: '', password: '' }
    }

    onMounted(() => {
      resetNewAdmin()
    })

    watch(() => [newAdmin.value.nombre, newAdmin.value.password], () => {
      if (newAdmin.value.nombre !== '' || newAdmin.value.password !== '') {
        resetNewAdmin()
      }
    })

    fetchAdministradores()

    return {
      administradores,
      newAdmin,
      editMode,
      currentAdmin,
      createAdmin,
      editAdmin,
      updateAdmin,
      deleteAdmin,
      cancelEdit,
      cancelCreate,
    }
  },
}
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px 0;
  border-radius: 5px;
  background-color: #f5f5dc; /* Fondo crema */
  cursor: pointer;
}

.card p {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

form {
  display: flex;
  flex-direction: column;
}

button {
  margin-top: 10px;
}

.grid {
  display: grid;
  gap: 10px;
}
</style>