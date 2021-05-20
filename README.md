## Valid usage

Single logical variable
```
python3 main.py "P"
```

AND formula
```
python3 main.py "(P and Q)"
```

OR formula
```
python3 main.py "(P or Q)"
```

Implication formula
```
python3 main.py "(P -> Q)"
```

Negate formula
```
python3 main.py "-P"
```

Nested formulae
```
python3 main.py "((P -> Q) and (Q -> P))"

python3 main.py "((P and Q) and R)"
```

## Invalid usage

```
python3 main.py "P -> Q"
```
because parentheses are necessary

```
python3 main.py "(P and Q and R)"
```
because parentheses must be used correctly (the program does not understand precedence rules)
