# python

## 前提

一般地讲，计算机只能运行低级语言("机器语言"或"汇编语言")编写地程序
高级语言(C、C++、Perl、Java等)必须先处理才能运行，有两种程序可以处理转换高级语言：解释器和编译器

解释器每次处理一小部分程序，交替读入代码行并进行运算，一行一行解释翻译
编译器将源代码编译为可以在硬件上执行地目标代码(或可执行代码)，即完整地编译为低级语言

程序是指一组定义如何进行计算的指令的集合，编程语言一般包括的基本指令有：输入、输出、数学、条件执行、重复

程序因为某些原因而出错，程序错误被称为bug，查捕bug的过程称为调试(debugging)
常见的错误：语法错误、运行时错误(异常)、语义错误

形式语言和自然语言(英语、法语等)，编程语言是人们设计出来用来表示计算过程的形式语言

## 算法

量级就是各种渐进增长被认为是同等的函数的集合。例如，2n、100n 和 n+1 都是一个量级，用大 O 标记法写作 O(n)，并通常被称为线性的
所有首项是 n² 的函数都属于 O(n²)，它们被称为平方的

| 量级 | 名称 |
| ---- | ---- |
| O(1) | 常量级 |
| O(log<sub>b</sub>n) | 对数级(对任意b) |
| O(n) | 线性级 |
| O(nlog<sub>2</sub>n) | nlogn |
| O(n<sup>2</sup>) | 平方级 |
| O(n<sup>3</sup>) | 立方级 |
| O(c<sup>n</sup>) | 指数级(底数c任意) |

### 术语

| 术语表 | / | / |
| ---- | ---- | ---- |
| 问题解决(problem solving) | 高级语言(high-level language) | 低级语言(low-level language) |
| 可移植性(portability) | 解释(interpret) | 编译(compile) |
| 源代码(source code) | 目标代码(object code) | 可执行文件(executable) |
| 提示符(prompt) | 脚本(script) | 交互模式(interactive mode) |
| 脚本模式(script mode) | 程序(program) | 算法(algorithm) |
| 故障(bug) | 调试(debugging) | 语法(syntax) |
| 语法错误(syntax error) | 异常(exception) | 语义(semantics) |
| 语义错误(semantic error) | 自然语言(natural language) | 形式语言(formal language) |
| 记号(token) | 语法分析(parse) | print语句(print statement) |
| - | - | - |
| 值(value) | 类型(type) | 整数(integer) |
| 浮点数(floating-point) | 字符串(string) | 变量(variable) |
| 语句(statement) | 赋值(assignment) | 状态图(state diagram) |
| 关键字(keyword) | 操作符(operator) | 操作数(operand) |
| 舍去式除法(floor division) | 表达式(expression) | 求值(evaluate) |
| 优先级规则(rules of precedence) | 拼接(concatenate) | 注释(comment) |
| - | - | - |
| 函数(function) | 函数定义(function definition) | 函数对象(function object) |
| 函数头(header) | 函数体(body) | 形参(parameter) |
| 函数调用(function call) | 实参(argument) | 局部变量(local variable) |
| 返回值(return value) | 返回值(return value) | 有返回值函数(fruitful function) |
| 无返回值函数(void function) | 模块(module) | import语句(import statement) |
| 模块对象(module object) | 句点表示法(dot notation) | 组合(composition) |
| 执行流程(flow of execution) | 栈图(stack diagram) | 图框(frame) |
| 回溯(traceback) |  |  |
| - | - | - |
| 实例(instance) | 循环(loop) | 封装(encapsulation) |
| 泛化(generalization) | 关键词参数(keyword argument) | 接口(interface) |
| 重构(refactoring) | 开发计划(development plan) | 文档字符串(docstring) |
| 前置条件(precondition) | 后置条件(postcondition) |  |
| - | - | - |
| 求模操作符(modules operator) | 布尔表达式(boolean expression) | 关系操作符(relational operator) |
| 逻辑操作符(logical operator) | 条件语句(conditional statement) | 条件(condition) |
| 复合语句(compound statement) | 分支(branch) | 条件链语句(chained conditional) |
| 嵌套条件语句(nested conditional) | 递归(recursion) | 基准情形(base case) |
| 无限递归(infinite recursion) |  |  |
| - | - | - |
| 临时变量(temporary variable) | 无效代码(dead code) | None |
| 增量开发(incremental development) | 脚手架代码(scaffolding) | 守卫(guardian) |
| - | - | - |
| 多重赋值(multiple assignment) | 更新(update) | 初始化(initialization) |
| 增量(increment) | 减量(decrement) | 迭代(iteration) |
| 无限循环(infinite loop) |  |  |
| - | - | - |
| 对象(object) | 序列(sequence) | 项(item) |
| 下标(index) | 切片(slice) | 空字符串(empty string) |
| 不可变(immutable) | 遍历(traverse) | 搜索(search) |
| 计数器(counter) | 方法(method) | 方法调用(invocation) |
| - | - | - |
| 文件对象(file object) | 问题识别(problem recognition) | 特殊情形(special case) |
| - | - | - |
| 列表(list) | 元素(element) | 下标(index) |
| 嵌套列表(nested list) | 列表遍历(list traversal) | 映射(mapping) |
| 累加器(accumulator) | 增加赋值(augmented assignment) | 化简(reduce) |
| 映射(map) | 过滤(filter) | 对象(object) |
| 相等(equivalent) | 相同(identical) | 引用(reference) |
| 别名(aliasing) | 分隔符(delimiter) |  |
| - | - | - |
| 字典(dictionary) | 键值对(key-value pair) | 项(item) |
| 键(key) | 值(value) | 实现(implementation) |
| 散列表(hashtable) | 散列函数(hash function) | 可散列(hashable) |
| 查找(lookup) | 反向查找(reverse lookup) | 单件(singleton) |
| 调用图(call graph) | 直方图(histogram) | 备忘(memo) |
| 全局变量(global variable) | 标志(flag) | 声明(declaration) |
| - | - | - |
| 元组(tuple) | 元组赋值(tuple assignment) | 收集(gather) |
| 分散(scatter) | DSU(decorate-sort-undecorate) | 数据结构(data structure) |
| 数据结构的构形(shape of a data structure) |  |  |
| - | - | - |
| 确定性(deterministic) | 伪随机(pseudorandom) | 默认值(default value) |
| 覆盖(override) | 基准测试(benchmarking) |  |
| - | - | - |
| 持久性(persistent) | 格式操作符(format operator) | 格式字符串(format string) |
| 文本文件(text file) | 目录(directory) | 路径(path) |
| 相对路径(relative path) | 绝对路径(absolute path) | 捕获(catch) |
| 数据库(database) |  |  |
| - | - | - |
| 类(class) | 类对象(class object) | 实例(instance) |
| 属性(attribute) | 内嵌对象(embedded object) | 浅复制(shallow copy) |
| 深复制(deep copy) | 对象图(object diagram) |  |
| - | - | - |
| 原型和补丁(prototype and patch) | 有规划开发(planned development) | 纯函数 |
| 修改器(modifier) | 函数式编程风格(functional programming style) | 不变式(invariant) |
| - | - | - |
| 面向对象语言(object-oriented language) | 面向对象编程(object-oriented programming) | 方法(method) |
| 主体(subject) | 操作符重载(operator overloading) | 基于类型的分发(type-based dispatch) |
| 多态(polymorphic) | 信息隐藏(information hiding) |  |
| - | - | - |
| 编码(encode) | 类属性(class attribute) | 实例属性(instance attribute) |
| 饰面(veneer) | 继承(inheritance) | 父类(parent class) |
| 子类(child class) | IS-A关联(IS-A relationship) | HAS-A关联(HAS-A relationship) |
| 类图(class diagram) | 重载(multiplicity) |  |
| - | - | - |
| GUI(graphical user interface) | 部件(widget) | 选项(option) |
| 键值参数(keyword argument) | 回调(callback) | 绑定方法(bound method) |
| 事件驱动编程(event-driven programming) | 事件(event) | 事件循环(event loop) |
| 画布项(item) | 边界盒(bounding box) | 包装(pack) |
| 几何管理器(geometry manager) | 绑定(binding) |  |
|  |  |  |
