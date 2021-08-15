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
- Re：正则表达式，简洁表达一组字符串
    - IP地址：`(([1-9]?\d|1\d{2}|2[0-4]\d|25[0.5]).){3}`
    - 正则表达式的标识类型
        - raw string 类型（原生字符串类型）：`r'[1-9]\d{5}'`
        - string 类型：`'[1-9]\\d{5}'`
    - Re 库主要功能函数
        - re.search()，搜索匹配第一个位置，返回 match 对象
        - re.match()：从一个字符串的开始位置进行匹配，返回 match 对象
        - re.findall()：搜索字符串，以列表形式返回全部能匹配的子串
        - re.split()：将字符串按照正则匹配结果进行分割，返回列表类型
        - re.finditer()：搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素都是 match 对象
        - re.sub()：替换所有匹配到的字符串，返回替换后的字符串
        - re.compile()：将正则表达式的字符串形式编译成正则表达式对象，`regex = re.compile(r'[1-9]\d{5}')`
- Scrapy：网络爬虫原理介绍，专业爬虫框架介绍
    - "5+2"结构：SPIDERS、ENGINE、SCHEDULER、DOWNLOADER、ITEM PIPELINES
    - Scrapy 常用命令
        - 创建一个新工程：`scrapy startproject <name> [dir]`
        - 创建一个爬虫：`scrapy genspider [options] <name> <domain>`
        - 获取爬虫配置信息：`scrapy settings [options]`
        - 运行一个爬虫：`scrapy crawl <spider>`
        - 列出工程中所有爬虫：`scrapy list`
        - 启动 URL 调试命令行：`scrapy shell [url]`
    - 常用的类
        - Request 类
        - Response 类
        - Item 类

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
- 查找
    - `soup.find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)`
        - name：对标签名称的检索字符串
        - attrs：对标签属性值的检索字符串，可标注属性检索
        - recursive：是否对子孙全部检索，默认True
        - string：`<>...</>`中字符串区域的检索字符串
    - <>.find()：搜索且只返回一个结果，字符串类型，同find_all参数
    - <>.find_parents() 与 <>.find_parent
    - <>.find_next_siblings() 与 <>.find_next_sibling
    - <>.find_previous_siblings() 与 <>.find_previous_sibling()

5、信息处理
- 信息标记
    - HTML/XML：用于Internet上的信息交互与传递
    - JSON：用于应用云端和节点的信息通信，接口，无注释
    - YAML：各类系统的配置文件，有注释易读
- 信息提取
    - 方法一：完整解析信息的标记形式，再提取关键信息
    - 方法二：无视标记形式，直接搜索关键信息
    - 方法三：以上两种方式融合

-- 今天在摸鱼

















