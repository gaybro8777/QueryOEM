# QueryOEM
Query OEM for information about workstations, laptops, servers and others.

# How to Install
Just issue ```pip install QueryOEM```

# Supported OEM's
Only DELL is supported at this moment

# Usage
There are two diferent classes. **QueryOEM** will query a single equipment and **MultipleQueryOEM** is a wrapper
which will return a list of <QueryOEM>

## Quering a single equipment
```python
import QueryOEM

my_laptop = QueryOEM.QueryOEM(PART_NUMBER="XXXXXX")
my_laptop.get_from_dell()

# Return a dictionary
print(my_laptop.dell_data)

# Return a JSON and save it into a file
fopen = open('c:/temp/my_laptop.json', 'w')
fopen.write(my_laptop.json_from_dell())
fopen.close()
```

## Quering multiple equipments
```python
import QueryOEM

assets_list = MultipleQueryOEM(['XXXXXX','YYYYYY','WWWWWW','ZZZZZZ'])
assets_list.get_from_dell()

# Loop over the queried equipments
for i in assets_list.results:
  print(i)

# Retrieve a JSON containing all equipments
JSON = assets_list.json_from_dell()
fopen = open('c:/temp/assets_list.json', 'w')
fopen.write(JSON)
fopen.close()
```
