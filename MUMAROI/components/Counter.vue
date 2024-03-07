<template>
    <div class="flex items-center">
      <button
        @click="decrement"
        class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-bold py-2 px-4 rounded-l-md"
      >-</button>
      <input
        v-model="count"
        type="number"
        class="w-12 text-center text-black p-2 border border-gray-300 bg-white rounded-md"
      />
      <button
        @click="increment"
        class="bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-r-md"
      >+</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        count: 0,
      };
    },
    methods: {
      increment() {
        this.count++;
      },
      decrement() {
        if (this.count > 0) {
          this.count--;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  </style>
  

  <!-- <script>
  import Counter from "~/components/Counter.vue";
  
  export default {
    components: {
      Counter,
    },
  };
  </script> -->