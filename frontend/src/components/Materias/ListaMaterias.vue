<template>
    <div class="container">
      <div class="row">
        <div class="col-12 text-center">
          <h2>Lista de cursos</h2>
        </div>
        <div class="col-12 text-right">
          <button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#modalNuevoCurso">
            Nuevo Curso
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
                  <th scope="col">Descripción</th>
                  <th scope="col">Profesor</th>
                  <th scope="col"></th>
                  <th scope="col"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="curso in cursos" :key="curso.id">
                  <td>{{ curso.nombre }}</td>
                  <td>{{ curso.descripcion }}</td>
                  <td>{{ getNombreCompletoProfesor(curso.profesor) }}</td>
                  <td>
                    <button class="btn btn-primary btn-sm" @click="redirectToEdit(curso.id)">
                      Editar
                    </button>
                  </td>
                  <td>
                    <button class="btn btn-danger btn-sm" @click="eliminarCurso(curso.id)">
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
  
    <!-- Modal Nuevo Curso -->
    <div class="modal fade" id="modalNuevoCurso" tabindex="-1" aria-labelledby="modalNuevoCursoLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalNuevoCursoLabel">Agregar Nuevo Curso</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm">
              <div class="mb-3">
                <label for="nombre" class="form-label">Nombre</label>
                <input type="text" id="nombre" v-model="nombre" class="form-control" required>
              </div>
              <div class="mb-3">
                <label for="descripcion" class="form-label">Descripción</label>
                <input type="text" id="descripcion" v-model="descripcion" class="form-control" required>
              </div>
              <div class="mb-3">
                <label for="profesor" class="form-label">Profesor</label>
                <select id="profesor" v-model="profesor" class="form-select" required>
                  <option value="" disabled selected>Seleccionar</option>
                  <option v-for="profesor in profesores" :value="profesor.id" :key="profesor.id">{{ getNombreCompletoProfesor(profesor.id) }}</option>
                </select>
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
        cursos: null,
        profesores: [],
        nombre: '',
        descripcion: '',
        profesor: ''
      };
    },
    mounted() {
      this.getCursos();
      this.getProfesores();
    },
    methods: {
      submitForm() {
        const formData = {
          nombre: this.nombre,
          descripcion: this.descripcion,
          profesor: this.profesor
        };
  
        axios.post('http://127.0.0.1:8000/api/cursos/', formData)
          .then(response => {
            // Realizar acciones después de enviar los datos
            console.log(response.data);
          })
          .catch(error => {
            // Manejar errores en caso de que la solicitud falle
            console.error(error);
          });
      },
      eliminarCurso(id) {
        if (confirm('¿Estás seguro de eliminar este curso?')) {
          axios.delete(`http://127.0.0.1:8000/api/cursos/${id}`)
            .then(response => {
              // Realizar acciones después de eliminar el curso
              console.log(response.data, 'Curso eliminado');
              // Volver a cargar la lista de cursos
              this.getCursos();
            })
            .catch(error => {
              console.error(error);
              // Manejar errores en caso de que la solicitud falle
            });
        }
      },
      redirectToEdit(id) {
        this.$router.push({ path: `/cursos/editar/${id}` });
      },
      getCursos() {
        axios.get('http://127.0.0.1:8000/api/cursos/').then(
          (response) => {
            this.cursos = response.data;
          }
        ).catch(error => {
          console.error(error);
          // Maneja el error de acuerdo a tus necesidades
        });
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
      },
      getNombreCompletoProfesor(profesorId) {
        const profesor = this.profesores.find(profesor => profesor.id === profesorId);
        if (profesor) {
          return `${profesor.nombre} ${profesor.apellido}`;
        }
        return '';
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