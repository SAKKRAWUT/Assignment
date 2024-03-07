<template>
    <div class="flex flex-col">
      <!-- Scrollable Tab Bar -->
      <div class="flex overflow-x-auto no-scrollbar">
        <div class="flex space-x-2 sm:space-x-4 p-2">
          <button
            v-for="(tab, index) in tabs"
            :key="index"
            :class="{
              'bg-blue-500 text-white': currentTab === index,
              'bg-white text-gray-500': currentTab !== index,
            }"
            class="px-3 py-1 sm:px-4 sm:py-2 rounded-md text-xs sm:text-sm font-medium whitespace-nowrap"
            @click="scrollToSection(index)"
          >
            {{ tab }}
          </button>
        </div>
      </div>
      
      <!-- Content Sections -->
      <div v-for="(content, index) in tabContents" :key="index" :ref="`section${index}`" class="section">
        {{ content }}
        
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const tabs = ['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Curry', 'Tab 7'] // Add more tabs as needed
  const tabContents = ['Content for Tab 1', 'Content for Tab 2', 'Content for Tab 3', 'Content for Tab 4', 'Content for Tab 5', 'Curry', 'Content for Tab 7'] // Add more content as needed
  const currentTab = ref(0)
  const sectionRefs = ref({})
  
  const scrollToSection = (index) => {
    currentTab.value = index
    const sectionRef = sectionRefs.value[`section${index}`]
    if (sectionRef) {
      sectionRef.scrollIntoView({ behavior: 'smooth' })
    }
  }
  
  // Dynamically assign refs to the sections
  const setSectionRef = (el, name) => {
    if (el) {
      sectionRefs.value[name] = el
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
  .section {
    padding-top: 1rem; /* Adjust as necessary */
  }
  </style>
  