<template>
   <!-- buton X -->
   <form method="dialog">
        <button class="btn btn-sm btn-circle btn-ghost absolute  ">✕</button>
      </form>

    <div class="card">
      <div class="">
        <div class="">
          <img :src="`${product.image}`" class="mx-auto  w-full h-[30rem]" />
        </div>

        <div class="p-5">
          <h2 class="text-4xl my-7">{{ product.title }}</h2>
          <p class="text-xl my-7">฿{{ product.price }}</p>
          <div class="detail ">
      <p>ข้อความเพิ่มเติม (ถ้ามี)</p>
      <div class="textbox mt-4">
        <input type="text" placeholder="Type here" class="input input-bordered w-full " />
      </div>
    </div>

    <div class="foot flex justify-between mt-8 pr-6">
      <Counter />
      <div class="btn w-3/5 ">
        add cart
      </div>
    </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    const { product } = defineProps(['product'])
  </script>
  
  <style scoped>
    img {
      max-width: 400px;
    }
  </style>