##get post 请求

###get请求、post请求

1 get请求
	*使用场景：
只对服务器获取数据，没有对服务器产生任何影响
	*参数:传参放到url中，并通过问号的形式来指定key 和value的

1 post请求
	*使用场景：
当对服务器产生影响时，使用post请求
	*参数:参数通过 `form data`的形式发送给服务器



###post get如何获取参数值
3 post 请求注意点
	* 在写form 表单时，要指定  method = post，并指定 action = ‘/login/‘

