
### 功能


> 项目需求

- 数据库统一使用默认数据库SQLite
- 实现注册，登录（可以使用邮箱登录）
- 实现主页面轮播，电影列表显示，电影详情信息
- 实现用户信息修改（邮箱修改）
- 实现收藏，与取消收藏
- 在注册前实现用户名预校验，密码数据安全
- 前端可以转换成模板，或者前后端分离


> 实现的功能


- 使用的了SQLite数据库


- 注册
  - 使用用户名注册
  - 注册的时候密码两次加密，密码数据安全
  - 注册时ajax实现用户名校验，两次密码是否一致的校验，后面显示相对应的字段
  - 注册提交加了check（）验证
  - 注册成功后直接跳转主页，正确显示用户头像和用户名


- 登录
  - 使用用户名密码登录
  - 验证用户名和密码是否匹配，如果匹配不上显示提示信息
  - ajax实现密码的加密
  - 登录成功之后直接跳转到首页的，正确显示用户头像和用户名
  - 登录使用的session会话技术，设置了有效时长为1分钟

- 退出
	- 添加了一个退出功能


- 轮播
	- 实现主页面轮播，电影列表显示，电影详情信息

- 用户信息
	- 实现了用户邮箱的修改
	- 实现了用户头像的修改，上传成功后直接跳转到首页，显示新的头像
	- 头像的大小添加了css



- 前端
	- 前端转换成了模板的格式，使用的是继承基模板的



- 收藏
	- 已更新，使用外键实现



> 未实现的功能


- 登录
	- 邮箱登录未实现，想使用Q对象过滤，然后判断但是一直报错





















