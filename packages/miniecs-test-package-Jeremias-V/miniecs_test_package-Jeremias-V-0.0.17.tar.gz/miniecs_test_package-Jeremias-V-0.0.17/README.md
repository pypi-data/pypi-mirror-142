# Mini Elastic Container Service Package

- This is **NOT** intended for commercial use, neither for developing any application.
- This package is just for a project of the Operating Systems course at my university.

The build is done with the following script.

```bash
#!/bin/bash

rm dist/*

VERSION=$(grep "version" setup.cfg | awk -F. -v OFS=. '{print $3 + 1}')

sed -i -e "/version =/ s/= .*/= 0.0.$VERSION/" setup.cfg

python3 -m build

python3 -m twine upload dist/*
```

The default socket ip is `localhost` and the port `65535`. To change either value you must use the class constructor, an example is presented below:

```python
from miniecs_test_package import miniecs

CONNECTION = miniecs.MiniECS(address='192.168.1.100', port=8080)
CONNECTION.create_container(name='Test_Container')
CONNECTION.stop()   # To stop the socket connection.
```
