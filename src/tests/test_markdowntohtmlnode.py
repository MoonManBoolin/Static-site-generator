import unittest
from src.markdowntohtmlnode import markdown_to_html_node

class TestTextNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
    the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\n    the **same** even with inline stuff\n</code></pre></div>",
        )
    def test_multiple_code_blocks(self):
        md = """
```
First code block
```

Some paragraph text.

```
Second code block
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>First code block\n</code></pre><p>Some paragraph text.</p><pre><code>Second code block\n</code></pre></div>",
        )
    def test_paragraph_with_special_characters(self):
        md = """
Paragraph with <tags> & symbols like $ and #.

Another paragraph with "quotes" and 'apostrophes'.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Paragraph with <tags> & symbols like $ and #.</p><p>Another paragraph with \"quotes\" and 'apostrophes'.</p></div>",
        )
    def test_paragraph_with_inline_code_and_bold(self):
        md = """
This is a paragraph with `inline code` and **bold text**.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with <code>inline code</code> and <b>bold text</b>.</p></div>",
        )
    def test_single_h1_heading(self):
        md = """
# My Title
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>My Title</h1></div>")

    def test_all_heading_levels(self):
        md = """
# H1

## H2

### H3

#### H4

##### H5

###### H6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>H1</h1><h2>H2</h2><h3>H3</h3><h4>H4</h4><h5>H5</h5><h6>H6</h6></div>",
        )

    def test_heading_trims_extra_spaces(self):
        md = """
#    Spaced Title   
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Spaced Title</h1></div>")

    def test_heading_with_inline_markdown(self):
        md = """
## Heading with `code` and **bold** and _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Heading with <code>code</code> and <b>bold</b> and <i>italic</i></h2></div>",
        )

    def test_mixed_paragraph_and_heading(self):
        md = """
Intro paragraph text.

### Section Title

Another paragraph.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Intro paragraph text.</p><h3>Section Title</h3><p>Another paragraph.</p></div>",
        )
    def test_simple_ordered_list(self):
        md = """
1. First
2. Second
3. Third
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>",
        )

    def test_ordered_list_with_inline_formatting(self):
        md = """
1. Item with `code` and **bold**
2. Another with _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item with <code>code</code> and <b>bold</b></li><li>Another with <i>italic</i></li></ol></div>",
        )

    def test_mixed_paragraph_and_ordered_list(self):
        md = """
Intro text.

1. One
2. Two

After list.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Intro text.</p><ol><li>One</li><li>Two</li></ol><p>After list.</p></div>",
        )

    def test_single_item_ordered_list(self):
        md = """
1. Only one
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ol><li>Only one</li></ol></div>")
    def test_simple_unordered_list(self):
        md = """
- First
- Second
- Third
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First</li><li>Second</li><li>Third</li></ul></div>",
        )

    def test_unordered_list_with_inline_formatting(self):
        md = """
- Item with `code` and **bold**
- Another with _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item with <code>code</code> and <b>bold</b></li><li>Another with <i>italic</i></li></ul></div>",
        )

    def test_mixed_paragraph_and_unordered_list(self):
        md = """
Intro paragraph.

- One
- Two

After list.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Intro paragraph.</p><ul><li>One</li><li>Two</li></ul><p>After list.</p></div>",
        )

    def test_single_item_unordered_list(self):
        md = """
- Only one
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>Only one</li></ul></div>")

    def test_unordered_list_trims_whitespace(self):
        md = """
-   Item one   
-    Item two
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item one</li><li>Item two</li></ul></div>",
        )

    def test_hyphen_without_space_is_paragraph(self):
        md = """
-Bad item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>-Bad item</p></div>")
    def test_simple_blockquote(self):
        md = """
> A simple quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>A simple quote</blockquote></div>")

    def test_blockquote_with_inline_formatting(self):
        md = """
> Quote with `code` and **bold** and _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quote with <code>code</code> and <b>bold</b> and <i>italic</i></blockquote></div>",
        )

    def test_multiline_blockquote_merges_lines(self):
        md = """
> Line one
> Line two continues
> and line three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Line one Line two continues and line three</blockquote></div>",
        )

    def test_mixed_paragraph_and_blockquote(self):
        md = """
Intro paragraph.

> Quoted text

After paragraph.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Intro paragraph.</p><blockquote>Quoted text</blockquote><p>After paragraph.</p></div>",
        )

    def test_blockquote_trims_marker_and_whitespace(self):
        md = """
>    Spaced content     
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>Spaced content</blockquote></div>")
    def test_full_document_mixed_blocks(self):
        md = """
# Title

This is a paragraph with **bold** and `code`.

- Item A
- Item B with _italic_

1. First
2. Second

> A quoted line
> continued.

```
line1
line2
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Title</h1><p>This is a paragraph with <b>bold</b> and <code>code</code>.</p><ul><li>Item A</li><li>Item B with <i>italic</i></li></ul><ol><li>First</li><li>Second</li></ol><blockquote>A quoted line continued.</blockquote><pre><code>line1\nline2\n</code></pre></div>",
        )

    def test_full_document_varied_structure(self):
        md = """
## Overview

> Quote with `code`

Some text with _italic_.

- One
- Two

```
print("hi")
```

### Next

1. Uno
2. Dos
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Overview</h2><blockquote>Quote with <code>code</code></blockquote><p>Some text with <i>italic</i>.</p><ul><li>One</li><li>Two</li></ul><pre><code>print(\"hi\")\n</code></pre><h3>Next</h3><ol><li>Uno</li><li>Dos</li></ol></div>",
        )

    def test_full_document_with_paragraphs_lists_quote_and_code(self):
        md = """
Intro paragraph.

# Heading

- First
- Second

> Multi
> line

1. One
2. Two
3. Three

Closing paragraph.

```
echo done
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Intro paragraph.</p><h1>Heading</h1><ul><li>First</li><li>Second</li></ul><blockquote>Multi line</blockquote><ol><li>One</li><li>Two</li><li>Three</li></ol><p>Closing paragraph.</p><pre><code>echo done\n</code></pre></div>",
        )
if __name__ == "__main__":
    unittest.main()

