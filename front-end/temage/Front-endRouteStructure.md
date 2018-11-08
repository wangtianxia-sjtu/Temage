# Front-end Route Structure

## App.vue 

> 登陆后的单页面 

### topbar.vue

> 顶部导航栏	    

- logo
- user-info
- #search
- #notification

###  sidebar.vue

> 侧面导航栏，button与route映射

- homepage-btn

- gallery-btn
  - #share 

- workspace-btn
  - new
  - review

### router-vue.vue

> 由路由控制的区域，实现功能切换

#### homepage.vue

> 登录后的默认页面，展示my_card

#####    card.vue  

>  用户头像+用户名+标题+图片 +summary(hover)

#####    my_card.vue 	

> card子类，标题+图片 +summary(hover)

- row-group #1 Recent cards
- row-group #2 Saved cards
- row-group #3 collection cards

#### gallery.vue 

> 社交以及浏览，展示被share过的card，类比adobe CC, [Pinterest ](www.pinterest.com) (out of wall)

##### timeline.vue  <like twitter lazy loading>

> 可以复用card组件和review.vue的页面($card.on(click))

#### workspace.vue

> 主要的工作区

##### creat.vuw

> 新建一个项目的输入页面

- text_input.vue (raw)
- image_input.vue (upload pic and select)
- generate-btn  (upload materials)

##### review.vue

> 预览已经被排列过的文章，并手动调整

- review_area.vue
- edit-btn (unlock review_area into text_area)

##### download-btn

> 给出model 选择下载文件格式

## Welcome.vue

> 欢迎页面，使用文档，用户注册，用户登录
>
> 为本地下载model拖延时间