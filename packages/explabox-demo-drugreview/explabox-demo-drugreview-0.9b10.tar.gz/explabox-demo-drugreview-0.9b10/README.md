<a href="https://explabox.rtfd.io" target="_blank">
<img src="https://git.science.uu.nl/m.j.robeer/explabox/-/raw/main/img/explabox-logo-text.png" alt="explabox-logo">
</a>

# explabox-demo-drugreview

Welcome to the demo of the [explabox](https://explabox.rtfd.io) on the [UCI Drug Reviews](https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29#) dataset. To speed up the demo, we made a smaller subset of the train and test dataset. The demo 
also includes a pretrained black-box classifier, which aims to predict whether a `review` in the text got a `rating` of 
`negative` (1-5), `neutral` (5-6) or `positive` (6-10).

**To start the demo, you require:**
- Python 3.8 or above (see the [installation guide](https://www.python.org/downloads/))
- Jupyter Notebook installed (see the [installation guide](https://jupyter.org/install))

**Install the demo via:**
- `pip3 install explabox`
- `pip3 install explabox-demo-drugreview`

## Importing the necessary files
To start the demo, open your Jupyter Notebook and run the following line:

```python
from explabox_demo_drugreview import model, dataset_file 
```

The `dataset_file` is the location of the dataset (`drugsCom.zip`), containing a train split (`drugsComTrain.tsv`) and test split (`drugsComTest.tsv`). You can import this dataset with the [explabox](https://explabox.rtfd.io) with the data in the column `review` and labels in the column `rating`:

```python
from explabox import import_data
data = import_data(dataset_file, data_cols='review', label_cols='rating')  
```

The model can directly be imported as-is. Make sure you explicitly include that `drugsComTrain.tsv` includes the `train` split and `drugsComTest.tsv` the `test` split of the data:

```python
from explabox import Explabox

box = Explabox(data=data,
               model=model,
               splits={'train': 'drugsComTrain.tsv', 'test': 'drugsComTest.tsv'})
```

Now you are ready to `.explore`, `.examine`, `.expose` and `.explain` with the [explabox](https://explabox.rtfd.io)!

## Documentation
Having trouble? Want to know which functionalities the [explabox](https://explabox.rtfd.io) includes? Check out the documentation at [https://explabox.rtfd.io](https://explabox.rtfd.io).
