<template>
  <div class="container">
    <div class="row">
      <div class="col-12 text-center">
        <h2>Lista de alumnos</h2>
      </div>
      <div class="col-12 text-right">
        <button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#modalNuevoEstudiante">
          Nuevo Alumno
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
                <th scope="col">Direccion</th>
                <th scope="col">Telefono</th>
                <th scope="col">Correo electrónico</th>
                <th scope="col"></th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="alumno in alumnos" :key="alumno.id">
                <td>{{ alumno.nombre }}</td>
                <td>{{ alumno.apellido }}</td>
                <td>{{ alumno.fecha_nacimiento }}</td>
                <td>{{ alumno.direccion }}</td>
                <td>{{ alumno.telefono }}</td>
                <td>{{ alumno.correo_electronico }}</td>
                <td>
                  <button class="btn btn-primary btn-sm" @click="redirectToEdit(alumno.id)">
                    Editar
                  </button>
                </td>
                <td>
                  <button class="btn btn-danger btn-sm" @click="eliminarAlumno(alumno.id)">
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
  
  <!-- Modal Nuevo Estudiante -->
  <div class="modal fade" id="modalNuevoEstudiante" tabindex="-1" aria-labelledby="modalNuevoEstudianteLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalNuevoEstudianteLabel">Agregar Nuevo Estudiante</h5>
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
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" >Cancelar</button>
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
      alumnos: null,
      nombre: '',
      apellido: '',
      fecha_nacimiento: '',
      direccion: '',
      telefono: null,
      correo_electronico: ''
    };
  },
  mounted() {
    this.getAlumnos()
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

      axios.post('http://127.0.0.1:8000/api/estudiantes/', formData)
        .then(response => {
          // Realizar acciones después de enviar los datos
          console.log(response.data);
        })
        .catch(error => {
          // Manejar errores en caso de que la solicitud falle
          console.error(error);
        });
    },
    eliminarAlumno(id) {
      if (confirm('¿Estás seguro de eliminar este alumno?')) {
        axios.delete(`http://127.0.0.1:8000/api/estudiantes/${id}`)
        .then(response => {
          // Realizar acciones después de eliminar el alumno
          console.log(response.data,'Alumno eliminado');
         // Volver a cargar la lista de alumnos
         this.getAlumnos();
        })
        .catch(error => {
          console.error(error);
          // Manejar errores en caso de que la solicitud falle
        });
      }
    },
    redirectToEdit(id) {
      this.$router.push({ path: `/alumnos/editar/${id}` });
    },
    getAlumnos() {
      axios.get('http://127.0.0.1:8000/api/estudiantes/').then(
        (response) => {
          this.alumnos = response.data;
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