<template>
  <div class="list">
    <div class="product_list">
      <product  v-for="product in products" :key="product.id" :product="product"></product>
    </div>
  </div>
</template>

<script>
import product from './UI/product'
import axios from 'axios'

export default {
  name: 'productList',
  components: {
    product
  },
  data () {
    return {
      products: null
    }
  },
  mounted () {
    axios.get(`/store/api/product-list/`).then(
      response => {
        this.products = response.data
      }
    )
  }
}
</script>

<style scoped>
.product_list {
  display: flex;
  flex-wrap: wrap;
  flex-flow: column wrap;
  flex-direction: row;
  align-content: stretch;
  justify-content: space-around;
  align-items: center;
}
</style>
