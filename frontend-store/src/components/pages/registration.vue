<template>
  <div class="main">
    <navbar></navbar>
    <div class="container">
      <div class="registration__inner">
        <form action="" class="registration__form">
          <div class="form__left">
            <h1>Регистрация</h1>
            <div class="form__item">
              <label for="username" class="username__label">Логин</label>
              <input type="text" class="username_inp" id="username">
            </div>
            <div class="form__item">
              <label for="name" class="name__label">Имя</label>
              <input type="text" class="name_inp" id="name">
            </div>
            <div class="form__item">
              <label for="lastname" class="lastname__label">Фамилия</label>
              <input type="text" class="lastname_inp" id="lastname">
            </div>
            <div class="form__item">
              <label for="secondname" class="secondname__label">Отчество</label>
              <input type="text" class="secondname_inp" id="secondname">
            </div>
            <div class="form__item">
              <label for="email" class="email__label">Адресс электронной почты</label>
              <input type="email" class="password_inp" id="email">
            </div>
            <div class="form__item">
              <label for="password" class="password__label">Пароль</label>
              <input type="password" class="password_inp" id="password">
            </div>
          </div>
          <div class="form__right">
            <h2>Content</h2>
          </div>
        </form>
      </div>
    </div>
    <Myfooter class="Myfooter"></Myfooter>
  </div>
</template>

<script>
import Navbar from '../UI/Navbar'
import Myfooter from '../UI/footer'

export default {
  name: 'registration',
  components: {Navbar, Myfooter}
}
</script>

<style scoped>
.registration__inner {
  margin: 30px;

}
.registration__form {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  max-width: 700px;
  align-items: flex-start;
  margin: auto auto;
  min-height: 500px;
  background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
  padding: 5px 25px 25px;
  border-radius: 35px;
  position: relative;
  overflow: hidden;
}
.registration__form label{
  margin-bottom: 5px;
  align-self: flex-start;
  font-size: 22px;
  color: #111111;
  font-weight: 700rem;
  letter-spacing: 1px;
}
.form__left::before{
  color: white;
  padding-top: 50px;
  font-size: 35px;
  content: "";
  left: 0;
  top: 225px;
  width: 350px;
  height: 600px;
  position: absolute;
  background: #f12711;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #f5af19, #f06e16);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #f5af19, #f06e16); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

  transition: all 2s ease;
  transform: skewY(354deg);
  z-index: 3;
}
.form__right::before{
  content: "";
  position: absolute;
  color: #f9f9f9;
  left: 350px;
  top: 0;
  width: 400px;
  height: 600px;
  background: #f12711;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #f06e16, #f12711);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #f06e16, #f12711); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

  transition: all 2s ease;
}
.form__left h1{
  position: relative;
}
.registration__form:hover .form__left::before {
  left: -100%;
}
.registration__form:hover .form__right::before {
  top: 40%;
  left: 20%;
  transform: skewY(64deg);
  width: 750px;
  height: 150px;
}
.registration__form input{
  outline:none;
  padding: 7px;
  max-width: 300px;
  min-width: 200px;
  border: none;
  height: 18px;
  border-bottom: #122936 solid 1px;
  background-color: transparent;
  margin-bottom: 15px;
}
.form__item{
  display: flex;
  flex-direction: column;
  justify-items: center;
}
.email__label {
  text-align: left;
}
.form__right{
  width: 350px;
}
.form__left{
  width: 350px;
}
@media screen and (max-width: 388px) {
  .registration__form:hover .form__left::before {
    left: -200%;
  }
  .registration__form:hover .form__right::before {
    z-index: 0;
  }
}
</style>
