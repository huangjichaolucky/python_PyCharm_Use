flask cookie 章节
###cookie 
1. 为
2. 如果服务器返回了`cookie`给浏览器，那么浏览器
3. `cookie`是保存在浏览器中的，相对的是浏览器
### session
1
2 使用session的好处，
	* 敏感数据不是直接发送给浏览器，而是发送为一个`session_id`，服务器将`session_id`和敏感数据做一个映射存储在`session`中，更安全
	 *`session_id` 可以设置过期时间，更保证了账号安全


###flask的session机制
1. flask的session机制： 把敏感数据加密后放到`session`中，然后再把`session`存放到`cookie`中，下次请求的时候，再把浏览器发送的`cookie`中读取`session`，然后再从`session`中读取敏感数据，并进行解密，获取最终的用户数据
2. 可以节省服务器的开销，因为把所有信息都存储在了客户端（浏览器）
3. 安全是相对的，把`session`放到`cookie`中，经过加密，也是比较安全的




###操作session
1. 使用`session`需要从`flask`中导入`session`， 以后所有的`session`相关操作都是通过这个变量来的
2. 使用`session`需要设置`secret_key`，用来加密用的，并且这个`secret_key`如果每次服务器启动后都变化的话，那么之前的 `session`不能通过这个`secret_key`进行解密了
3. 跟操作字典一致 ，有设置、获取、删除操作
4. session的过期时间
	* 默认过期时间是关闭浏览器就过期
	* 设置permanent 为 true， 则过期时间为一个月
		* permanent 为 true时， 设置app.config['PERMAMENT_SESSION_LIFETIME'] = timedelta(days=7)， 则过期时间为7天




