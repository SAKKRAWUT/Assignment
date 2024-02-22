<template>
  <div class="header relative">
    <div class="head  ">
      <nav class="flex w-full  absolute justify-between p-4 ">
        <!-- table -->
        <div class="text-[30px] h-22 text-black bg-white rounded-[12px] p-1"> Table 300</div>
        <ul class="flex gap-4">
          <!-- history-->
          <!-- <li>
            <button class="btn btn-square btn-outline border-transparent" onclick="my_modal_4.showModal()">
              <Icon name="ic:round-list-alt" size="50" />
            </button>
            <orderlist />
          </li> -->
          <!-- history-->
          <li>
            <NuxtLink to="/orderlist"><button class="btn btn-square btn-outline border-transparent ml-6">
                <Icon name="ic:round-list-alt" size="50" />
              </button>
            </NuxtLink>
          </li>
          <!--cart  -->
          <li>
            <NuxtLink to="/cart"><button class="btn btn-square btn-outline border-transparent mr-6">
                <Icon name="material-symbols:shopping-cart-outline-rounded" size="50" />
              </button></NuxtLink>
          </li>
        </ul>
      </nav>
    </div>
    <!-- pic -->
    <div class="img ">
      <img src="" class="w-full h-52 bg-red-600" alt="">
    </div>
    <!-- name -->
    <div class="namelabel bg-white text-center p-1">
      <h1 class="text-[22px] text-black">Mum Aroi</h1>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped></style>
