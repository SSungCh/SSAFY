# Day 4

## Python Dictionary

```python
my_dict = {'apple': '사과', 'banana': '바나나'}

# 1. 일반 반복문
for key in my_dict:
    print(key)
    print(my_dict[key]) # value 접근

# 2. key, value 
for key, value in my_dict.items():
    print(key, value)

# 3. value
for value in my_dict.values():
    print(value)
    
# 4. key
for key in my_dict.keys():
    print(key)
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict['apple']
# => 사과
my_dict['cat']
# => 오류 발생(Key Error)
my_dict.get('apple')
# => 사과
my_dict.get('cat')
# => None
my_dict.get('cat', 'Not Found')
# => Not Found
```