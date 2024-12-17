# Resumen de Ejercicios

Este repositorio incluye una serie de ejercicios prácticos orientados a la gestión de sistemas **ERP-CRM en Odoo**, organizados en **cuatro actividades principales**.

---

## 📝 **Activitat 01: Vista Kanban y Calendario para Tareas**

**Objetivo:**
Modificar el ejemplo básico de la lista de tareas para agregar nuevas vistas y funcionalidades.

**Tareas Realizadas:**
- 📌 Crear una **vista Kanban** para visualizar las tareas.
- 📅 Añadir una **fecha asignada** a cada tarea.
- 🗓️ Implementar una **vista Calendario** que muestre las fechas asignadas.

---

## 📚 **Activitat 02: Gestió de Biblioteca de Còmics**

**Objetivo:**
Extender el módulo de biblioteca de còmics.

**Nuevas Funcionalidades:**
- 👤 Gestionar **socios** con datos de nombre, apellido e identificador.
- 📖 Introducir **ejemplares de cómics** para préstamo.
- 🗂️ Crear un nuevo modelo de **ejemplares de préstamo** que controle:
  - Usuario que tiene el cómic.
  - Fecha de inicio del préstamo *(no posterior al día de hoy)*.
  - Fecha prevista de devolución *(no anterior al día de hoy)*.

**Restricciones:**
- ❌ No se implementa historial de préstamos, solo el estado actual del ejemplar.

---

## 🏥 **Activitat 03: Gestió d’Hospital**

**Objetivo:**
Crear un módulo para gestionar **pacientes y médicos** de un hospital.

**Modelos Implementados:**
- 🧑‍🤝‍🧑 **Pacient**: Nombre, apellidos y síntomas.
- 🧑‍⚕️ **Metge**: Nombre, apellidos y número de colegiado.
- 🗒️ **Atenció**: Registro de diagnósticos entre médicos y pacientes.

**Relaciones:**
- 🔄 Un paciente puede ser atendido por **varios médicos**.
- 🔄 Un médico puede atender a **varios pacientes**.

**Vistas:**
- 📋 Implementadas **vistas** para gestionar los 3 modelos.

---

## 🏫 **Activitat 04: Gestió d’Estudis de Cicles Formatius**

**Objetivo:**
Crear un módulo que represente los **estudios de un instituto**.

**Modelos Implementados:**
- 📘 **Cicle Formatiu**: Relacionado con uno o más módulos.
- 📗 **Mòdul**: Relacionado con un ciclo, alumnos matriculados y profesores asignados.
- 🎓 **Alumne**: Relacionado con los módulos matriculados.
- 👨‍🏫 **Professor**: Relacionado con los módulos que imparte.

**Configuración de Seguridad:**
- 🛡️ Usuarios con rol **“Director”** pueden **modificar todos los registros**.
- 👀 Usuarios con rol **“Professor”** pueden **ver** (modo lectura) los datos de los profesores.

---

✨ ¡Cada actividad presenta una práctica concreta de desarrollo en Odoo, optimizando la gestión y visualización de datos! 🚀
