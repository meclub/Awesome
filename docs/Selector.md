# 爬虫数据解析

## 成员变量
- response 一个HtmlResponse或者XmlResponse对象
- text 一个unicode字符串或者utf-8文本，当response为空的时候才有效。同时使用text和response是未定义行为
- type 定义selector的类型，可以是html、xml或None(default)
    - 如果type为None，那么selector会根据response自动选择最佳的type，如果定义了text那么默认成html类型
    - response的类型确定：
    - xml：XmlResponse
    - html：HtmlResponse
    - html：其他类型
    - 如果已经设定了type那么强制使用设定好的type。

## 主要函数
- xpath() 寻找匹配xpath query 的节点，并返回 SelectorList 的一个实例结果，单一化其所有元素。返回的列表元素也实现了 Selector 的接口。query 是包含XPATH查询请求的字符串。
- css() 应用给定的CSS选择器，返回 SelectorList 的一个实例。在后台，通过 cssselect 库和运行 .xpath() 方法，CSS查询会被转换为XPath查询。
- extract() 串行化并将匹配到的节点返回一个unicode字符串列表。 结尾是编码内容的百分比
- reg(regex) 应用给定的regex，并返回匹配到的unicode字符串列表。regex 可以是一个已编译的正则表达式，也可以是一个将被 re.compile(regex) 编译为正则表达式的字符串。
- register_namespaces(prefix, uri) 注册给定的命名空间，其将在 Selector 中使用。 不注册命名空间，你将无法从非标准命名空间中选择或提取数据。
- remove_namespaces() 移除所有的命名空间，允许使用少量的命名空间xpaths遍历文档
- __nonzero__() 如果选择了任意的真实文档，将返回 True ，否则返回 False 。 也就是说， Selector 的布尔值是通过它选择的内容确定的。

## SelectorList用法
SelectorList 类是内建 list 类的子类，提供了一些额外的方法。
- xpath(query) 对列表中的每个元素调用 .xpath() 方法，返回结果为另一个单一化的 SelectorList
- css(query) 对列表中的各个元素调用 .css() 方法，返回结果为另一个单一化的 SelectorList
- extract() 对列表中的各个元素调用 .extract() 方法，返回结果为单一化的unicode字符串列表
- re() 对列表中的各个元素调用 .re() 方法，返回结果为单一化的unicode字符串列表
- __nonzero__() 列表非空则返回True，否则返回False

## 命名空间
```
// 注册
sel.register_namespace("g", "http://base.google.com/ns/1.0")
sel.xpath("//g:price").extract()

// 移除
selector.remove_namespaces()
```

## 基本用法
'//' 是绝对路径， './/'是当前路径, '@'是选择attr
```
body = '<html><body><span>good</span></body></html>'
Selector(text=body).xpath('//span/text()').extract()
response = HtmlResponse(url='http://example.com', body=body)
response.xpath('//base/@href').extract()
response.css('base::attr(href)').extract()
response.xpath('//a[contains(@href, "image")]/@href').extract()
response.css('a[href*=image]::attr(href)').extract()
response.xpath('//a[contains(@href, "image")]/img/@src').extract()
response.css('a[href*=image] img::attr(src)').extract()
```

## css选择器可以采用CSS3伪元素
```
response.css('title::text').extract()
```

## 嵌套选择器
```
links = response.xpath('//a[contains(@href, "image")]')
```

## 正则表达式
```
response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
```

## test函数
例如在XPath的 starts-with() 或 contains() 无法满足需求时， test() 函数可以非常有用。例如在列表中选择有”class”元素且结尾为一个数字的链接:
```
doc = """
<div>
     <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
      </ul>
</div>
 """
sel = Selector(text=doc, type="html")
sel.xpath('//li//@href').extract()
sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()
```

## text使用
- 当你想要使用文本内容作为XPath函数的参数时，避免使用.//text()，采用.来替代。
```
sel.xpath("//a[contains(., 'Next Page')]").extract()
```

- 使用.//text()没有结果
```
sel.xpath("//a[contains(.//text(), 'Next Page')]").extract()
```

## 当通过class查询的时候, 考虑使用CSS
因为一个元素可能含有多个CSS class，用XPath的方式选择元素会很冗长，scrapy允许链式使用选择器，因此多数情况下你可以先用CSS选择class，再使用XPath。
```
sel.css('.shout').xpath('./time/@datetime').extract()
```
