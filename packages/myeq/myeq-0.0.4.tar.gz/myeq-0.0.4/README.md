# My equations (myeq)
Some simple useful math equations.

# Distance

Equation to measure distances between values.

## Inverse normalized sigmoid

```python
from myeq.distance import inv_norm_sigmoid

def inv_norm_sigmoid(x: float, s: float = 0.3, t: float = 0.88, p: float = 3.3, adjust: bool = False) -> float:
```

This function is used to normalize a value that represents a distance using an inverted sigmoid function as following:

![Inverse Normalized Sigmoid](images/inv_norm_sigmoid.png)

I usually use this function to normalize the Levenshtein or another edition distance that is not normalized.
This way, when the distance is small, the value is very close to 1, in the middle the value decreases very fast,
but far away the velocity of decrease goes slower with the limit to 0.
In the Levenshtein algorithm, this means that when the difference is small, the similarity value is very close to 1.
But it quickly decreases when there are more text editions.

You can adjust the function parameters using the 
[Inverse Normalized Sigmoid Demos web page](https://www.desmos.com/calculator/36mx8dlkyt).

Examples of usage:

```python
from myeq.distance import inv_norm_sigmoid

print(inv_norm_sigmoid(0))  # Almost 1: 0.9999853027487737)
print(inv_norm_sigmoid(1))  # Close to 1: 0.9999910856079368)
print(inv_norm_sigmoid(3))  # Start to reduce quickly: 0.7633315491944042)
print(inv_norm_sigmoid(5))  # Very low: 0.12000003643145052)        
```

The _adjust_ parameter is to force the value 1 when the distance is 0, for example:

```python
from myeq.distance import inv_norm_sigmoid

print(inv_norm_sigmoid(0, adjust=True))  # Exactly 1.0)
```