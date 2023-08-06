## Hidden Markov Machine (HMM)

This module provides the function `write(prompt, length, bias, training)` which adds `length` words to the end of the prompt. If the bias is set to 0 (the minimum), there will be no bias, and the closer it gets to 1 (the maximum) nouns in the prompt are more likely to be chosen. If a bias is not provided, the default is 0. The training variable is optional, it defaults to a file of writing I've done in the past, but can be set to a different file. If you choose to change the training, change it to a txt file hosted online, e.g. [`"https://raw.githubusercontent.com/TobyCK/markov-chain/master/Training/dataset2.txt"`](https://raw.githubusercontent.com/TobyCK/markov-chain/master/Training/dataset2.txt). Below is an example of how to use the module:

```py
from hmm_write import hmm
hmm.write("The quick brown fox jumps over the", 50, 0.3)
```