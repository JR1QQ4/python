1、Python网络爬虫与信息提取
- Requests：自动爬取HTML页面，自动网络请求提交
    - request: params data json headers cookies auth files timeout proxies allow_redirects stream verify cert
- robots.txt：网络爬虫排除标准
- Beautiful Soup：解析HTML页面
    - 解析器
        - ba4的HTML解析器——pip install bs4
        - lxml的HTML解析器——pip install lxml
        - lxml的XML解析器——pip install lxml
        - html5lib的解析器——pip install html5lib
- Projects：实战项目
- Re：正则表达式
- Scrapy：网络爬虫原理介绍，专业爬虫框架介绍

2、HTTP协议
- HTTP是一个基于”请求与响应“模式的、无状态的应用层协议
- HTTP协议采用URL作为定位网络资源的标识
- GET、HEAD（获取头部信息）、POST（附加）、PUT（全部覆盖更新）、PATCH（局部替换更新）、DELETE

3、网络爬虫的限制
- 来源审查
- 发布公告：Robots协议，告知所有爬虫网站的爬取策略，要求爬虫遵守
    - 在网站根目录下的robots.txt文件

4、Beautiful Soup
- 遍历
    - 下行遍历：contents、children、descendants
    - 上行遍历：parent、parents
    - 平行遍历：next_sibling、previous_sibling、next_siblings、previous_siblings
- 格式化：`soup.prettify()`











