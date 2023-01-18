# Module yaml_json_config

This is a module to facilitate reading a config file or text string in json or yaml to a python object, vice versa.

Not only flat key value style is supported, event embeded objects and list of objects can be supported.

## Demo of Usage
Let's say there is a sample config file in yaml format
```yaml
address: #368 GuangZhou District, GZ, GD
telephone: +86206666666666
boss:
  name: alpha
  id: 001
  age: 40
members:
  - name: alpha
    id: 001 
    age: 40
  - name: beta 
    id: 002 
    age: 33
  - name: sigma
    id: 006 
    age: 38
```

### Shallow Load to Object
### Deep Load to Object
### Dump to JSON
### Dump to YAML