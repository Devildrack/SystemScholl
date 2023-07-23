<template>
    <div class="container">
      <div class="row">
        <div class="col-12 text-center">
          <h2>Lista de profesores</h2>
        </div>
        <div class="col-12 text-right">
          <button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#modalNuevoProfesor">
            Nuevo Profesor
          </button>
        </div>
      </div>
      <br>
      <div class="row">
        <div class="col-md-12">
          <div class="table-responsive">
            <table class="table table-hover">
              <thead>
                <tr>
                  <th scope="col">Nombre</th>
                  <th scope="col">Apellido</th>
                  <th scope="col">Fecha de nacimiento</th>
                  <th scope="col">Dirección</th>
                  <th scope="col">Teléfono</th>
                  <th scope="col">Correo electrónico</th>
                  <th scope="col"></th>
                  <th scope="col"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="profesor in profesores" :key="profesor.id">
                  <td>{{ profesor.nombre }}</td>
                  <td>{{ profesor.apellido }}</td>
                  <td>{{ profesor.fecha_nacimiento }}</td>
                  <td>{{ profesor.direccion }}</td>
                  <td>{{ profesor.telefono }}</td>
                  <td>{{ profesor.correo_electronico }}</td>
                  <td>
                    <button class="btn btn-primary btn-sm" @click="redirectToEdit(profesor.id)">
                      Editar
                    </button>
                  </td>
                  <td>
                    <button class="btn btn-danger btn-sm" @click="eliminarProfesor(profesor.id)">
                      Eliminar
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  
    <!-- Modal Nuevo Profesor -->
    <div class="modal fade" id="modalNuevoProfesor" tabindex="-1" aria-labelledby="modalNuevoProfesorLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalNuevoProfesorLabel">Agregar Nuevo Profesor</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm">
              <div class="mb-3">
                <label for="nombre" class="form-label">Nombre</label>
                <input type="text" id="nombre" v-model="nombre" class="form-control" required>
              </div>
              <div class="mb-3">
                <label for="apellido" class="form-label">Apellido</label>
                <input type="text" id="apellido" v-model="apellido" class="form-control" required>
              </div>
              <div class="mb-3">
                <label for="fechaNacimiento" class="form-label">Fecha de Nacimiento</label>
                <input type="date" id="fechaNacimiento" v-model="fecha_nacimiento" class="form-control" required>
              </div>
              <div class="mb-3">
                <label for="direccion" class="form-label">Dirección</label>
                <input type="text" id="direccion" v-model="direccion" class="form-control" required>
              </div>
              <div class="mb-3">
                <label for="telefono" class="form-label">Número Telefónico</label>
                <input type="number" id="telefono" v-model="telefono" class="form-control" max="9999999999" required>
              </div>
              <div class="mb-3">
                <label for="correo" class="form-label">Correo Electrónico</label>
                <input type="email" id="correo" v-model="correo_electronico" class="form-control" required>
              </div>
              <button type="submit" class="btn btn-primary">Guardar</button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        profesores: null,
        nombre: '',
        apellido: '',
        fecha_nacimiento: '',
        direccion: '',
        telefono: null,
        correo_electronico: ''
      };
    },
    mounted() {
      this.getProfesores()
    },
    methods: {
      submitForm() {
        const formData = {
          nombre: this.nombre,
          apellido: this.apellido,
          fecha_nacimiento: this.fecha_nacimiento,
          direccion: this.direccion,
          telefono: this.telefono,
          correo_electronico: this.correo_electronico
        };
  
        axios.post('http://127.0.0.1:8000/api/profesores/', formData)
          .then(response => {
            // Realizar acciones después de enviar los datos
            console.log(response.data);
          })
          .catch(error => {
            // Manejar errores en caso de que la solicitud falle
            console.error(error);
          });
      },
      eliminarProfesor(id) {
        if (confirm('¿Estás seguro de eliminar este profesor?')) {
          axios.delete(`http://127.0.0.1:8000/api/profesores/${id}`)
            .then(response => {
              // Realizar acciones después de eliminar el profesor
              console.log(response.data, 'Profesor eliminado');
              // Volver a cargar la lista de profesores
              this.getProfesores();
            })
            .catch(error => {
              console.error(error);
              // Manejar errores en caso de que la solicitud falle
            });
        }
      },
      redirectToEdit(id) {
        this.$router.push({ path: `/profesores/editar/${id}` });
      },
      getProfesores() {
        axios.get('http://127.0.0.1:8000/api/profesores/').then(
          (response) => {
            this.profesores = response.data;
          }
        ).catch(error => {
          console.error(error);
          // Maneja el error de acuerdo a tus necesidades
        });
      }
    },
  };
  </script>
  
  <style lang="css" scoped>
  .container {
    margin-top: 30px;
  }
  
  .table-responsive {
    margin-bottom: 20px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 10px;
  }
  
  th {
    background-color: #f8f9fa;
    border-bottom: 1px solid #dee2e6;
    text-align: center;
  }
  
  tr:nth-child(even) {
    background-color: #f8f9fa;
  }
  
  .btn-sm {
    margin-right: 5px;
  }
  </style>