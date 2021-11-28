<template>
  <article class="product">
    <img :src="product.images" :alt="product.name">
    <div class="block__select">
      <h2 class="product__title"> {{ product.name }} </h2>
      <label>
        <select class="selection" @change="changePrice">
          <option class="option" v-for="specification in specifications" :key="specification.id">
            {{ specification.name }}
          </option>
        </select>
      </label>
    </div>
    <p class="product__price"> {{ price }}<span class="product__currency"> ₽ </span></p>
    <button class="product__btn_buy">Добавить в корзину</button>
  </article>
</template>

<script>
import axios from 'axios'

export default {
  name: 'product',
  props: {
    product: Object,
    specifications: null,
    price: 10
  },
  mounted () {
    axios.get(`/store/api/specification-product/${this.product.id}/`).then(
      response => {
        this.specifications = response.data.specifications
        this.price = response.data.specifications[0].price
      }
    )
  },
  methods: {
    changePrice (event) {
      for (let i = 0; i < this.specifications.length; i++) {
        if (this.specifications[i].name === event.target.value) {
          this.price = this.specifications[i].price
        }
      }
    }
  }
}
</script>

<style scoped>
.product{
  position: relative;
  margin: 30px;
  width: 300px;
  height: 370px;
  background-color: #122936;
  color: #ffffff;
  border-radius: 20px;
  font-weight: 500;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  overflow: hidden;
  transition: .3s;
}
.product:hover{
  box-shadow: 0 6px 10px 0 rgba(0, 0, 0, 0.4), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.product::before{
  content: "";
  display: block;
  width: 100%;
  height: 100%;
  background-color: #2196f3;
  transform: skewY(345deg);

  position: absolute;
  top: -50%;
  transition: 0.5s;
}
.product:hover::before{
  transform: skewY(390deg);
  top: -70%;
}
.product img {
  margin-top: 60px;
  width: 100%;
  position: relative;
  transition: .5s;
}
.product__title{
  font-size: 22px;
  margin: 25px 0 10px;
  position: relative;
  text-shadow: 0 0 4px rgba(202, 228, 225, 0.92), 0 0 20px rgba(202, 228, 225, 0.34), 0 0 6px rgba(191, 226, 255, 0.52), 0 0 11px rgba(191, 226, 255, 0.92), 0 0 34px rgba(191, 226, 255, 0.78), 0 0 54px rgba(191, 226, 255, 0.92);
}
.product__price{
  font-size: 24px;
  margin: 0 0 35px;
  position: relative;
  transition: .5s;
}
.product__currency{
  font-size: 18px;
  position: relative;
}
.product__btn_buy{
  border: none;
  cursor: pointer;
  background-color: #02a717;
  padding: 15px 30px;
  border-radius: 30px;
  color: inherit;
  text-transform: inherit;
  font-weight: inherit;
}
.product__btn_buy:hover{
  background-color: #038614;
}
.product:hover img{
  width: 70%;
}
.product:hover .product__price{
  margin: 0 0 15px;
}
.product_btns{
  display: flex;
  align-items: center;
  position: relative;
  background-color: transparent;
  border: none;
  padding: 10px 0px;
}
.product:hover .product_btns img{
  width: 30px;
}
.block__select{
  display: flex;
  align-items: center;
  justify-content: center;
}
.selection{
  height: 26px;
  font-size: 22px;
  position: relative;
  margin: 23px 0 10px 10px;
  background-color: inherit;
  border: none;
  color: #f9f9f9;
  outline: none;
}
.option{
  background-color: #122936;
  outline: none;
  border: none;
}
</style>
