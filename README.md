# ipsum-gen
Just a simple class to generate some lorem ipsum text.

Supports a number of paragraphs and a total word count. It then divides the two and generates paragraphs with an equal number of words (except for the last, which may have the remainder of words from the modulus of word count & paragraphs.

Absolutely no support for more paragraphs than words. The results get weird and I'm not going to bother fixing.


# Usage

```python
ipsum = IpsumGenerator(paragraph_count=9, word_count=1200)
text_test = ipsum.generate_paragraphs()
print(text_test)
```
