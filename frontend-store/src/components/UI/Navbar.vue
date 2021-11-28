<template>
  <div class="navbar">
    <nav class="nav__inner">
      <h1>wh1te_opt</h1>
      <div class="nav_items">
        <ul class="nav_ul">
          <li class="nav_li"><a @click="$router.push('/')" class="nav_link">Главная</a></li>
          <categoryDropdown>Категории</categoryDropdown>
        </ul>
      </div>
      <div class="nav_btns">
        <div class="favorites">
          <a href="" class="favorites__link">
            <img src="@/assets/favorites.png" alt="favorites icon" class="favorites__img">
          </a>
        </div>
        <div class="cart">
          <a href="" class="cart__link">
            <img src="@/assets/shopping-cart.png" alt="Card image">
          </a>
        </div>
        <div class="account">
          <a @click="$router.push('/registration')" class="account__link">
            <img class="account__img" src="@/assets/user.png" alt="user">
          </a>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import categoryDropdown from './categoryDropdown'
export default {
  name: 'Navbar',
  components: {categoryDropdown}
}
</script>

<style scoped>
.nav__inner{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

h1 {
  padding-left: 15px;
  padding-right: 40px;
  text-transform: uppercase;
}
.favorites__img{
  width: 30px;
}
.favorites{
  margin-left: auto;
  margin-right: 30px;
  filter: brightness(0) invert(1);
}
.navbar{
  background-color: #131313;
  border-radius: 10px;
  color: antiquewhite;
  max-width: 1150px;
  margin: 30px auto 0;
}
.nav_btns{
  display: flex;
  align-items: center;
  margin-left: auto;
  align-self: center;
}
.nav_ul{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding-left: 0;
}

.nav_li {
  text-decoration: none;
  list-style: none;
  text-transform: uppercase;
}
.nav_li:first-child{
  padding: 15px;
}
.nav_link{
  cursor: pointer;
  text-decoration: none;
  color: antiquewhite;
  animation: ease-in-out;
}
.nav_link:hover{
  color: #42b983;
  transition: all 0.4s ease-in-out;
}
.cart{
  margin-right: 30px;
}
.account__img{
  width: 30px;
  filter: brightness(0) invert(1);
}
.account{
  margin-right: 50px;
  align-self: center;
  cursor: pointer;
}
@media screen and (max-width: 700px) {
  .nav__inner {
    display: flex;
    justify-content: space-around;
    flex-direction: column;
  }
  .nav_ul {
    padding: 0;
  }
  .nav_btns {
    margin: 0 auto;
  }
  .cart{
    margin: 15px;
  }
  .account {
    margin: 15px;
  }
  .favorites {
    margin: 15px;
  }
  .nav__inner h1 {
    padding: 0;
  }
}
</style>
