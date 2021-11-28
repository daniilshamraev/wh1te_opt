<template>
  <footer class="footer__inner">
    <div class="about">
      <p><a href="tel:79507760820">+79507760820</a></p>
      <p><span>Сайт разработал <a href="https://t.me/on_plc">Даниил Шамраев</a></span></p>
      <p class="footer__about-text">
        Оптовый магазин 2021©
      </p>
    </div>
    <div class="links">
      <ul class="links__list">
        <li class="list__item"><a href="https://vk.com/wh1te_opt" class="links__item"><img src="@/assets/social/vk.png" alt="vk"></a></li>
        <li class="list__item"><a href="https://t.me/wh1te_opt" class="links__item"><img src="@/assets/social/telegram.png" alt="telegram"></a></li>
        <li class="list__item"><a href="" class="links__item"><img src="@/assets/social/instagram.png" alt="insta"></a></li>
      </ul>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Myfooter'
}
</script>

<style scoped>
.footer__inner{
  width: 100%;
  min-height: 200px;
  background-color: black;
  color: #f9f9f9;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin: 0 auto;
  margin-top: auto;
}
.list__item a{
  text-decoration: none;
  color: inherit;
}
.links__list{
  list-style: none;
  display: flex;
  justify-content: space-around;
}
.about{
  margin-bottom: auto;
  margin-top: auto;
}
.links{
  margin-bottom: auto;
  margin-top: auto;
  padding: 10px;
}
.links__list li img {
  padding: 10px;
  width: 50px;
  margin: 0 auto;
}
.about p a{
  text-decoration: none;
  color: inherit;
}
@media screen and (max-width: 534px){
  .footer__inner{
    padding-top: 15px;
    padding-bottom: 15px;
    flex-direction: column;
    align-items: center;
  }
  .links__list {
    padding-left: 0;
  }
}
</style>
