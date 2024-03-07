<template>

    <div class="card text-center">
      <NuxtLink :to="`/products/${product.id}`">
        <img :src="`${product.image}`" class="thumb" />
        
      <p class="font-bold text-left text-gray-500 m-4 truncate">{{ product.title }}</p>
      <p class="font-bold text-left text-gray-500 m-4 truncate">฿{{ product.price }}</p>
        
      </NuxtLink>
    </div>
  </template>
  
  <script setup>
    const { product } = defineProps(['product'])
  </script>
  
  <style scoped>
    .thumb {
      max-height: 120px;
      max-width: 70%;
      margin: 0 auto;
    }
  </style>