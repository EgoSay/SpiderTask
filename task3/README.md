### python爬虫学习Task3

- 安装selenium并学习,使用selenium模拟登陆163邮箱。
    
   1. selenium简介
        >中文文档链接：https://selenium-python-zh.readthedocs.io/en/latest/
   2. 自动化测试流程
       ```
       1）定位页面元素

       2）操作页面元素

       3）验证

       4）记录测试结果
       ```
   3. 模拟登陆163邮箱    
        >163邮箱直通点：https://mail.163.com/
         chromedriver=2.46.628411
      - 第一步： 安装selenium: `pip install selenium` 
        >注意：如果电脑上有多个python2, python3多个环境注意对应的pip安装
        
      - 第二步：安装电脑系统对应版本的浏览器驱动\
        我这里是`Mac OS X 10.13.6 x86_64`, 选择的谷歌浏览器`73.0.3683.86`, 下载的chromedriver `2.46.628411`
      
      - 第三步：进入163邮箱登陆页面定位页面元素(谷歌浏览器打开开发者工具定位)
      
    4. 遇到的问题总结
        
        - Mac系统下安装`chromedriver`, 我这里用的 `anaconda3` 环境需要将解压后的chromedriver放到 `anaconda3/bin` 目录下
        - 代码中操作页面元素等需要sleep睡眠等待时间，不然可能会还没进行操作就退出了\
            
            ```
            time.sleep(3)
            browser.switch_to.frame(0)
            ```
            另外在 这里如果没有设置等待 3s 时可能会报如下错\
            <font color=red>selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"name","selector":"email"}</font>
            
    

