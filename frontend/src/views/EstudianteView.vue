<template>
    <div class="alumnos">
        <h2>ALUMNOS</h2>
        <ListaEstudiante/>
    </div>
</template>

<script>
// @ is an alias to /src
import ListaEstudiante from '@/components/Estudiantes/ListaEstudiante.vue'

export default {
  name: 'EstudianteView',
  components: {
    ListaEstudiante
  }
}
</script>