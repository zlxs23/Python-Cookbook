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