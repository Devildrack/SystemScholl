

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EstudianteView from '../views/EstudianteView.vue'
import EditarEstudiante from '@/components/Estudiantes/EditarEstudiante.vue'
import EditarProfesor from '@/components/Profesores/EditarProfesor.vue'
import ListaProfesores from '@/components/Profesores/ListaProfesores.vue'
import ListaMaterias from '@/components/Materias/ListaMaterias.vue'
import EditarMateria from '@/components/Materias/EditarMateria.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/alumnos',
    name: 'alumnos',
    component: EstudianteView
  },
  {
    path: '/alumno/editar/:id',
    name: 'alumno-editar',
    component: EditarEstudiante
  },
  {
    path: '/profesores',
    name: 'profesores',
    component: ListaProfesores
  },
  {
    path: '/profesor/editar/:id',
    name: 'profesor-editar',
    component: EditarProfesor
  },
  {
    path: '/materias',
    name: 'materias',
    component: ListaMaterias
  },
  {
    path: '/materia/editar/:id',
    name: 'materia-editar',
    component: EditarMateria
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
