<template>
      <Header />

<!-- NavMenu -->
<Scrollbar />

    <div>
      <div class="grid grid-cols-2 gap-5 p-2">
        <div v-for="p in products">
          <ProductCard :product="p" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    //  fetch the products
    const { data: products } = await useFetch('https://fakestoreapi.com/products')
  
    definePageMeta({
      layout: "products",
    })
  
    // useHead({
    //   title: 'Nuxt Dojo | Merch',
    //   meta: [
    //     { name: 'description', content: 'Nuxt 3 Merch'}
    //   ]
    // })
  </script>
