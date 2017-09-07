# Metamath expression tree to SAT solver cnf

*Status: Needs code review and documentation.*
*Mood: Proud of the code!*

Converts metamath expression tree into SAT solver format and optimizes number of variables. 

## Run

## Example
Example of input (pre-filtered for clarity):

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

which represents  
` ( -. ph -> ps ) <-> ( -. ps -> ph ) )`

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

where:
 
* `1` is  `( ( -. ph -> ps ) <-> ( -. ps -> ph ) )` 
* `2` is  `( -. ph -> ps )`
* `3` is  `( -. ps -> ph )`
* `4` is `ph`
* `5` is `ps`

Notice the first clause is 
```
-1 0
```

Which is the negation of the expression we want to prove. Assuming that our tautological statement `1` is true, adding the clause `-1 0` guarantees that the system is unsolvable. From there we can set up a trace for the SAT solver and attempt to automate the proof of `1` by resolving the trace (work to come). 

