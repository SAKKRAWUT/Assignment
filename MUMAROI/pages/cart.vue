<template>
    <div class="cart h-[54rem] p-4 w-full bg-white">
      <!-- x butom -->
      <form method="dialog">
        <button class="btn btn-sm btn-circle btn-ghost absolute  ">✕</button>
      </form>
      <!-- namecart -->
      <div class="name flex justify-center pb-4 text-[32px] border-b-2">
        Cart
      </div>
      <!-- itemlist -->
      <div class="itemlist flex-row  ">
        <!-- item01 -->
        <ItemList />
        <ItemList />
        <ItemList />
        <ItemList />
        
      </div>
    </div>
  
  
    <!-- footerconstant -->
    <div class="foot flex justify-between object-bottom p-4 bg-white" id="foot">
      <div class="text-black">Total</div>
      <div class="text-black">฿480</div>
    </div>
    <div class="flex justify-center p-4 bg-white">
      <button class="btn w-[53rem] bg-purple-500 hover:bg-purple-400 text-white ">Order</button>
  
    </div>
  </template>