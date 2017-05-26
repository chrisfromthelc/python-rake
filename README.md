RAKE
====

A Python implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in: Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents. In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons.

The source code is released under the MIT License.

## Usage

Import `rake` and `operator`.

```
import rake
import operator
```

Initialize RAKE with a stopword list and keyword parameters.
`rake_object = rake.Rake("SmartStoplist.txt", 5, 3, 4)`

This creates a RAKE object that extracts keywords where:
- Each word has at least 5 characters
- Each phrase has at most 3 words
- Each keyword appears in the text at least 4 times

Store the text you want to process in a variable, process with RAKE, and print to the screen.
```
sample_file = open("data/docs/fao_test/w2167e.txt", 'r')
text = sample_file.read()
keywords = rake_object.run(text)
print "Keywords:", keywords
```

You should get an output like this:
`Keywords: Keywords: [('household food security', 7.711414565826329), ('indigenous groups living', 7.4), ('national forest programmes', 7.249539170506913), ('wood forest products', 6.844777265745007)...`
