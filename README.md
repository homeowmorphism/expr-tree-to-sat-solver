Still need to do:
* Stream the input

Example of input:

```
atom |-
    atom <->
      atom ->
        atom -.
          atom ph
        atom ps
      atom ->
        atom -.
          atom ps
        atom ph
```

Resulting output:
```
p cnf 6 11
-1 0
2 -5 0
2 -4 0
-2 5 4 0
3 -4 0
3 -5 0
-3 4 5 0
1 2 3 0
1 -2 -3 0
-1 2 -3 0
-1 -2 3 0
 ```
