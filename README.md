# Python-Cookbook #
``Learning Cookbook......``
## Chap 1 数据结构与算法 ##
### 2_1,3_2,3,4,5,6,7 ###
#### 6/8/2016 10:53:25 PM  ####
1. 利用简单的赋值语句(保持 var 数量一致)解压并赋值给多个变量

	`p = (1 , 2 , 3)`
	 `x , y , z = p`
	 
2. 利用 * Expression 独立解压可变 var 数量

	` r = ('mzc' , 19 , '199' , 'aa')`
	`name , age , * tel = r`
	
	1. 扩展迭代解压 不确定或任意个数元素的可迭代对象
	2. 可在字符串操作时 进行分割
	
		`name , * fields , sh = line.split(':')`
		
	3. 使用 _ OR ign 进行忽略废弃 多余 的解压后元素
	4. 将 list 分割成前后两个部分
	5. 利用与递归算法
	6. 保留最后 N 个元素
3. 利用 collections.deque 进行保留最后有限几个元素的历史记录

	 ``` 
	     d = deque()
	     d.append((1 , 2 , 3))
	     d
	     >> deque([(1 , 2 , 3)])
	     d.append(1)
	     d
	     >>deque([(1 , 2 ,3) , 1])
	     d.appendleft(4)
	     d
	     >>deque([1 , (1 , 2 , 3) , 1])
	     d.pop()
	     d
	     >>1
	     d
	     >>deque([1 , (1 ,2 ,3)])
	     d.popleft()
	     >>1
	     d
	     >>deque([(1 , 2 , 3)])
	```
	> 利用 collections.deque 可以将 列表操作 转换成 队列操作 前者 时间复杂度为 O(N) , 后者才 O(1)

4. 利用 heapq 来从一个 set 中获得最大 OR 最小的 N 个元素序列

	`heapq.nlargest(3 , nums , key=lambda s : s[''])`
	`heapq.nsmallest(3, nums ,key=)`	
	> 在查找元素个数较小时 使用之很合适 当较大时 利用 max min OR sorted(items)[:N]

5. 利用 heapq 来进行优先级排序 队列
	
	`heapq.heappush()`
	`heapq.heapop()`
	> 分别在 _queue 队列中插入 OR 删除第一个元素 同时保证 _queue 第一个元素拥有最小 OR 大 优先级

6. 利用 collections.defaultdict 来进行 实现 一 key 对应 多 value [multidict]
	1. 一个 dict 一个 key 对应 多个值 则应该将此多值放置其他容器中 list OR set
	2. 若要保持 element の 插入顺序则选择 list | 若要去掉 重复 element 则选择 set 可选择 defaultdict
	3.  当然可以使用  setdefault 来在一个普通 dict 上进行多值映射
7. 利用 collections.OederedDict 来对其中 element 进行排序 在迭代操作时会保持 element 插入时的 Order
	1. OrderDict 内部维护着另一个 链表 内存消耗大
8. 利用 zip 将 key AND value 反转过来 进行计算 zip(p.values() , p.keys())
	1. zip created a 只能访问一次 の 迭代器 二次使用会置空
	2. IF 不进行 zip 反转 则会 直接多 keys 进行 字母排序运算
	3. 可利用 lambda Func 对计算 Func 添加辅助 参数 : key = lambda k : p[k] | valuse = lambda v : p[v]
	4.  IF instance 中出现相同 value 则会继续 判断 key 进行 排序
9.  利用 dict の keys() AND values() AND items() Func 进行判断两 dict 共同点 同时可进行 set 操作 
	1.  p1.keys() & / - p2.keys() | p1.values() & / - p2.vlaues() | p1.items() & / - p2.items()
	2.  利用 字典推导 进行排除指定 dict c = {key : a[key] for key in a.keys() - {'z' , 'w'}} # c 排除了 {'z' , 'w'} 对应 の item
10. 利用 set OR generator 来在一个 sequence 上保持顺序 の 同时并消除 重复 value --> hashable
11. 利用 slice 进行命名切片 slice(start , stop , step)
12. 利用 collections.Counter 来找出 sequence 中出现次数最多的元素
	1. 将 sequence 对象转换成 Counter 对象
	2. 利用 most _common(most frequency_num)
	3. 利用 Counter(words)['ma'] Return 'ma' 对应出现次数
	4. 利用 update Func 更新外来 の words
	5. 利用 Counter 来进行数学计算 主要是 set 操作 + - 
13. 利用 operator.itemgetter 来通过某些 dict 字段来进行排序
14. 利用 operator.attrgetter OR lambda 来进行排序不支持比较 の 对象
15. 利用 itertools.groupby 来通过 某些 dict 字段来将之按照 所需进行分组
16. 利用 列表推导进行过滤 sequence
	1. 将过滤代码放置为一个 Func 后使用 内建 filter Func
	2. 利用 itertools.compress 以一个 iterable 对象 AND 相对应 Boolean 选择 对应 True の element
17. 利用 字典推导 进行 From dict 中提取子集
	1. 亦可 created a tuple sequence 然后 传至 dict 进行实现
18. 利用 collections.namedtuple 来初始化 一个 namedtuple 类 [命名元组]
	1. Sub = namedtuple('Sub' , ['attr1' , 'attr2']) 
	2. 将代码从下标[nums]操作解脱出来['attr']
	3. 替代 dict 而且 namedtuple 不支持 同步更改
19.  利用 生成器表达式 进行 转换并同时计算 DATA 
20.  利用 collections.ChainMap 进行 dict OR 映射 合并
	1.  对 dict の 更新 OR 删除操作 只会影响 lsit 中第一个 dict
	2.  可以另外 created a dict 来 update 合并 --> 不同于 ChainMap 前者 本身操作 不影响 被合并 dict 后者则可