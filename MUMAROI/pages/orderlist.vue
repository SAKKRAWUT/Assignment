<template>
<!-- <dialog id="my_modal_4" class="modal relative "> -->
  <div class=" ">
    <!-- w-[128rem] h-[50rem] mb-52 -->
  <!-- buton X -->
        <form method="dialog">
        <button class="btn btn-sm btn-circle btn-ghost absolute  ">✕</button>
      </form>
      <div class="cart h-[54rem] p-4 w-full bg-white">
        
        <!-- OrderList & time -->
        <div class="name flex flex-col pb-4 text-[32px] border-b-2">
          <div class="text-center">
            <h1>Order List</h1>
            <p>Time 21.30</p>
          </div>
        </div>
        <!-- itemlist -->
        <div class="itemlist flex-row  ">
          <!-- item01 -->
          <ItemStatus />
          <ItemStatus />
          <ItemStatus />
          <ItemStatus />
          
          
          
        </div>
      </div>
    
    
      <!-- footerconstant -->
      <div class="foot flex justify-between object-bottom p-4 bg-white" id="foot">
        <div class="text-black">4 Item</div>
        <div class="text-black">฿480</div>
      </div>
      <div class="flex justify-center p-4 bg-white">
        <button class="btn w-full bg-purple-500 hover:bg-purple-400 text-white ">Bill</button>
    
      </div>
    </div>
  <!-- </dialog> -->
  </template>

<script setup>

</script>

<style lang="scss" scoped>

</style>