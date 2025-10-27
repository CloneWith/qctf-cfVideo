<script setup lang="ts">
</script>

<template>
  <div>
    <nav style="margin-bottom:2rem; font-size:1.1em">
      <span><b>澄峰祝福视频平台</b></span>
      <router-link to="/">主页</router-link>
      |
      <router-link to="/order">下单</router-link>
      |
      <router-link to="/budget">赞助</router-link>
    </nav>
    <router-view/>
    <footer style="margin-top:2rem; color:#888; font-size:0.9em">
      <span>澄峰祝福视频平台 &copy; 2025</span>
    </footer>
  </div>
</template>

<style>
body, html {
  font-family: 'Segoe UI', 'PingFang SC', 'Hiragino Sans', 'Arial', sans-serif;
  background: #f7f8fa;
  margin: 0;
  padding: 0;
}

nav {
  background: #fff;
  border-bottom: 1px solid #eee;
  padding: 1rem 2rem;
  box-shadow: 0 2px 8px #0001;
}

nav a {
  color: #42b883;
  text-decoration: none;
  margin: 0 0.5em;
  font-weight: 500;
}

nav a.router-link-active {
  color: #2c3e50;
}

main {
  max-width: 600px;
  margin: 2rem auto;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 16px #0002;
  padding: 2rem;
}

button {
  background: #42b883;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 0.5em 1.2em;
  font-size: 1em;
  cursor: pointer;
  margin: 0.5em 0.2em;
  transition: background 0.2s;
}

button:hover {
  background: #2c3e50;
}

input, textarea {
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 0.5em;
  margin: 0.3em 0;
  width: 100%;
  font-size: 1em;
  box-sizing: border-box;
}

label {
  display: block;
  margin: 0.7em 0 0.2em 0;
  font-weight: 500;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  background: #f2f6f9;
  margin: 0.5em 0;
  padding: 1em;
  border-radius: 8px;
  box-shadow: 0 1px 4px #0001;
}

footer {
  text-align: center;
  padding: 1em 0 0.5em 0;
}
</style>
