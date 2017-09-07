# Metamath expression tree to SAT solver cnf

*Status: Code review pending.*
*Mood: Proud of the code!*

Converts [Metamath](http://us.metamath.org/) expression tree into SAT solver format and optimizes number of variables. First step to automatically generating tautology proof from SAT solvers based on [this idea](https://groups.google.com/forum/#!topic/metamath/WwP52TVqWg8) by [Raph Levien](https://github.com/raphlinus).

## Quickstart 

Make sure you have a version of Python that is compatible with Python 2.7. Clone the repository and cd into it. 

```
$ python translate.py
```

You should see the output in `out/ex.cnf`. 

**To modify the input/output files** open `translate.py` and change

```
INPUT_FILE = "your_input_file"
OUT_FILE = "your_output_file"
```

### Pass output to picoSAT 

Download [picoSAT](http://fmv.jku.at/picosat/).

In the picoSAT folder type in

```
$ picosat PATH_TO_THIS_REPO/out/ex.cnf
```

## Example

**Input** `input/theorem.out` (filtered for clarity):

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

where `theorem.out` represents the theorem "not P implies Q iff not Q implies P", written as

` ( -. ph -> ps ) <-> ( -. ps -> ph ) )`.

**Output** `out/ex.cnf`

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

## Acknowledgements

This project was done at the [Recurse Center](https://www.recurse.com/), where [Raph](https://github.com/raphlinus) and I met and had a discussion on [Ghilbert](http://ghilbert.org/) which prompted him to have the idea for this project. I would like to thank him for sitting down with me and explaining his idea! 
