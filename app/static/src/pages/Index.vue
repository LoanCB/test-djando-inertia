<template>
  <div>
    <h1 class="title">Hello {{ name }} from Inertia + Django + Vite + Vue!</h1>
    <button @click="increment">Add</button>
    <p>Count: {{ count }}</p>
  </div>
</template>

<script>
export default {
  name: "test",
  props: {
    name: String
  },
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  }
}
</script>

<style scoped>
.title {
  color: green;
}
</style>