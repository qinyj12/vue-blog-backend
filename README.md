## 功能
* 后端
	* 用户api
		- [x] GET还是POST发送邮箱？
		- [x] 邮件发送模板并附带4位随机码
		- [x] 验证随机码，随机码过期
		- [x] 验证码根据时间戳排序，然后再判断是否过期
		- [x] 发送验证码1分钟内只能发1次
		- [x] 在orm里生成验证码，api里发送邮件
		- [x] 验证码表里同一个用户多次发码是否实现覆盖？还是不覆盖？选择不覆盖
		- [x] 验证码使用一次后作废
		- [ ] 邮件带链接，点击实现注册（如果重新发送验证码）
		- [x] 注册的完整流程，调用验证码orm和注册orm
		- [ ] 登录（只要在在数据库里查找、对比就好了）
		- [ ] 找回密码（验证码，通过后重新修改密码，要求重新登录）
		- [ ] session保持登录状态
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