<template>
  <div class="dropdown">
    <button class="dropbtn"><slot></slot></button>
    <div class="dropdown-content" v-for="category in categories" :key="category.id">
      <a href="#">{{ category.name }}</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'categoryDropdown',
  data () {
    return {
      categories: null
    }
  },
  mounted () {
    axios.get(`/store/api/category-list/`).then(
      response => (this.categories = response.data)
    )
  }
}
</script>

<style scoped>
.dropbtn {
  font-size: initial;
  color: antiquewhite;
  background-color: inherit;
  margin: 0;
  padding: 0 0 0 15px;
  text-decoration: none;
  list-style: none;
  text-transform: uppercase;
  border: none;
  cursor: pointer;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  border-radius: 10px;
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  backdrop-filter: blur(5px);
  min-width: 160px;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #f1f1ff;
  backdrop-filter: blur(5px);
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  color: #42b983;
  transition: all 0.4s ease-in-out;
}
@media screen and (max-width: 700px) {
  .dropbtn {
    padding: 15px;
  }
}
</style>
