<template>
    <div class="container">
      <div class="row">
        <div class="col-md-6 offset-md-3">
          <h2>Editar profesor</h2>
          <form @submit.prevent="actualizarProfesor">
            <div class="mb-3">
              <label for="nombre" class="form-label">Nombre</label>
              <input type="text" id="nombre" v-model="profesor.nombre" class="form-control" required>
            </div>
            <div class="mb-3">
              <label for="apellido" class="form-label">Apellido</label>
              <input type="text" id="apellido" v-model="profesor.apellido" class="form-control" required>
            </div>
            <div class="mb-3">
              <label for="fechaNacimiento" class="form-label">Fecha de Nacimiento</label>
              <input type="date" id="fechaNacimiento" v-model="profesor.fecha_nacimiento" class="form-control" required>
            </div>
            <div class="mb-3">
              <label for="direccion" class="form-label">Dirección</label>
              <input type="text" id="direccion" v-model="profesor.direccion" class="form-control" required>
            </div>
            <div class="mb-3">
              <label for="telefono" class="form-label">Número Telefónico</label>
              <input type="number" id="telefono" v-model="profesor.telefono" class="form-control" max="9999999999" required>
            </div>
            <div class="mb-3">
              <label for="correo" class="form-label">Correo Electrónico</label>
              <input type="email" id="correo" v-model="profesor.correo_electronico" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Guardar</button>
            <button @click="cancelarEdicion" class="btn btn-secondary">Cancelar</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        profesor: {
          nombre: '',
          apellido: '',
          fecha_nacimiento: '',
          direccion: '',
          telefono: null,
          correo_electronico: ''
        }
      };
    },
    mounted() {
      // Obtener el ID del profesor de la ruta
      const id = this.$route.params.id;
  
      // Realizar la solicitud para obtener los datos del profesor
      axios.get(`http://127.0.0.1:8000/api/profesores/${id}/`)
        .then(response => {
          // Asignar los datos del profesor al objeto profesor
          this.profesor = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    methods: {
      cancelarEdicion() {
        this.$router.push('/profesores/');
      },
      actualizarProfesor() {
        const id = this.$route.params.id;
  
        // Realizar la solicitud PUT para actualizar los datos del profesor
        axios.put(`http://127.0.0.1:8000/api/profesores/${id}/`, this.profesor)
          .then(response => {
            console.log(response.data);
            // Realizar acciones después de actualizar el profesor
          })
          .catch(error => {
            console.error(error);
            // Manejar errores en caso de que la solicitud falle
          });
      }
    }
  };
  </script>