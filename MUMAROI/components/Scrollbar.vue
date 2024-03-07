<template>
    <div class="flex flex-col">
      <!-- Scrollable Tab Bar -->
      <div class="flex overflow-x-auto scroll-smooth no-scrollbar snap-x">
        <div class="flex space-x-2 snap-start p-2">
          <button
            v-for="(tab, index) in tabs"
            :key="index"
            :class="{
              'border-b-4 border-b-indigo-500 text-purple-500': currentTab === index,
              ' text-gray-600': currentTab !== index,
            }"
            
            class="px-3 py-1 sm:px-4 sm:py-2 rounded-md text-xs sm:text-sm font-medium whitespace-nowrap"
            @click="scrollToContent(index)"
          >
            {{ tab }}
          </button>
        </div>
      </div>
      

      
      <!-- Content Sections -->
    <div class="content-section" ref="contentSection0">
      <!-- Content for Tab 0 -->
      
    </div>
    <div class="content-section" ref="contentSection1">
  
      <!-- Content for Tab 1 -->
      
    
    </div>
    <!-- Add more content sections for additional tabs -->
  </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const tabs = ['Recommend', 'Fried', 'Stir-fried', 'Curry', 'Appetizer', 'Beverage', 'Tab 7'] // Add more tabs as needed
  const currentTab = ref(0)
  const contentSections = ref([])
  // This function will scroll to the content section associated with the tab index
const scrollToContent = (index) => {
  currentTab.value = index
  contentSections.value[index].scrollIntoView({ behavior: 'smooth' })
}

// This function is used to dynamically assign refs to the content sections array
const setContentSectionRef = (el, index) => {
  if (el) {
    contentSections.value[index] = el
  }
}
  </script>
  
  
<style scoped>
/* Hide scrollbar for cleaner look */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

/* You might want to add some top padding to each content section so that 
when it's scrolled to, it doesn't stick to the top of the viewport. */
.content-section {
  padding-top: 1rem; /* Adjust the padding as needed */
}
</style>
  
    
  <!-- class="px-4 py-2 rounded-md text-sm font-medium whitespace-nowrap "
  @click="currentTab = index" -->