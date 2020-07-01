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
		- [x] 登录（只要在在数据库里查找、对比就好了）
		- [x] 重构！重构！全面重构！用and_和or_全面重构！
		- [x] 之前已经注册过的话就不能注册了
		- [x] 忘记密码（验证码，通过后重新修改密码，要求重新登录）
		- [x] 自定义错误码
		- [x] session保持登录状态
		- [x] 从api接口返回到前端的resp都转成json格式，在其中夹带状态码，前端方便做判断。下一步要做的就是get_session转json
		- [x] log out
		- [ ] 重定向，在vue router里做
		- [x] 保存log
		- [ ] log按时间切分
		- [ ] error的log邮箱通知
		- [x] 上下文转蓝图
		- [ ] 免密码登录接口
		- [x] 文章发布
		- [x] 发布前验证手机号，已验证非id==1无法发送，还需验证id==1能够发送
		- [x] 需要保存的东西——标题（db）、摘要（db）、头像（io）、封面图（io）、时间（db）、浏览量（db）、评论量（db）、正文（io）、插图（io）
		- [x] 测试前端上传页面
		- [x] 测试完上传页面后，再测试读取文章列表的页面
		- [x] 然后是动态生成文章页面
		- [ ] 修改：md、html各生成一份，md、html、cover、插图都保存到同一个文件夹
		- [ ] 倒数第二步：前端还原markdown格式，并且要有图片
		- [ ] 最后是文章留言
		- [ ] 检验密码强度、各种空值在前端做
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
- [ ] 懒加载，最后决定不用了