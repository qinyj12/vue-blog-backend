## 功能
* 前端
	* 用户
		- [x] 登录组件
		- [x] header组件
		- [x] 导航栏
		- [x] footer组件
		- [x] 登录页
		- [x] 文章列表组件
        - [x] 留言展示组件
        - [x] 搜索组件
		- [x] 文章列表页（主页）
		- [x] 关于我组件
		- [x] 文章详情组件
		- [x] 评论展示组件
		- [x] 文章详情页
		- [x] 关于我页
		- [ ] 配合后端的各种细节
		- [ ] 留言和评论发送组件
		- [ ] 移动端适配
		---
		- [ ] 添加加载动画
		- [ ] 音乐播放组件
	* 管理
		- [x] 文章发布组件
		- [ ] 文章修改组件 => 文章发布组件
* 后端
	* 用户api
		- [ ] 注册
		- [ ] 登录
		- [ ] 找回密码
		- [ ] 评论
	* 管理api
		- [ ] 发布文章
		- [ ] 修改文章
		- [ ] 删除文章

## 目录
|-- frontend/  
|　|-- src/（css + js）  
|　|-- index.html  
|-- backend/  
|　|-- api/（orm接口）  
|　|-- database/（数据库）  
|　|-- config/（配置文件）  
|　|-- test/（测试用）  
|　|-- app.py（主程序，调用api）  
|-- README.md  

## 难点
- [ ] 打开首页之前的白屏，即过渡动画（最后在index.html中添加）
- [ ] 切换路由之间的动画
- [ ] 屏幕滚动，动态加载组件，即懒加载。懒加载element有组件，但更好的办法应该是滑到底部，再发送ajax请求
- [ ] 动态加载组件时的动画，即懒加载的动画
- [x] v-for倒序迭代列表。直接用原型链v-for="(item, index) in Array.prototype.reverse.call(item)"
- [x] css hack，用来连接article-shadow和article-main。没必要，用ref一并操作。
- [x] vue操作css，这样v-for遍历对象时，可以根据对象元素的不同，加载不同的样式。直接上:style=""
- [ ] el-input获得焦点时的边框删除
- [ ] 用memcached存储验证码