<template>
  <div class="main_page">
    <navbar></navbar>
  <div class="main">
    <div class="container">
      <product-list></product-list>
    </div>
    <Myfooter class="Myfooter"></Myfooter>
  </div>
  </div>
</template>

<script>
import Navbar from '../UI/Navbar'
import Myfooter from '../UI/footer'
import productList from '../productList'
export default {
  name: 'main',
  components: {productList, Navbar, Myfooter}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  box-sizing: border-box;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.main_page {
  background-image: linear-gradient(to top, #c4c5c7 0%, #dcdddf 52%, #ebebeb 100%);
}
.container{
  max-width: 1200px;
  margin: 0 auto;
  flex: 1 0 auto;
}
.main {
  min-height: 88.4vh;
  display: flex;
  flex-direction: column;
}
</style>
