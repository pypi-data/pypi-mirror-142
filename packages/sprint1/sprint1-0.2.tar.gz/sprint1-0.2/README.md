# Calculator

## Installation

Use the command to install package.

```bash
pip install sprint1
```

## Usage example

```python
import sprint1

# create instance
cal = sprint1.Calculator()
# method resets memory
cal.reset()

# addition command
cal.add(42)

#division command
cal.sub(6)

#n root command, n is the brakets
print(cal.root(2))

# multiplication
print(cal.mul(4))

#division
print(cal.div(8))

#print memory
print(cal.memory)

```


## License
[MIT](https://choosealicense.com/licenses/mit/)