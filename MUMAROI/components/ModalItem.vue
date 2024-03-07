<template>
    <dialog id="my_modal_3" class="modal relative ">
    <div class=" ">
        <!-- buton X -->
        <form method="dialog">
        <button class="btn btn-sm btn-circle btn-ghost absolute  ">✕</button>
      </form>
      <!-- pic -->
    <div class="img h-[32rem]  ">
        
<img src="" class="w-full h-full bg-red-600" alt="">
    </div>
    <!-- name -->
    <div class="p-3 h-[28rem] bg-white">
    <div class="content h-56">
      <h1 class="text-[60px]">ปลากระพงทอดน้ำปลา</h1>
      <p class="text-[25px]">฿480</p>
    </div>
  <!-- detail -->
    <div class="detail ">
      <p>ข้อความเพิ่มเติม (ถ้ามี)</p>
      <div class="textbox mt-4">
        <input type="text" placeholder="Type here" class="input input-bordered w-full " />
      </div>
    </div>
<!-- footer -->
    <div class="foot flex justify-between mt-8 pr-6">
      <Counter />
      <div class="btn w-4/5 ">
        add cart
      </div>
    </div>
  </div>
    </div>
  </dialog>
    
</template>

