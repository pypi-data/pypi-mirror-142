# Marquedown

Extending Markdown further by adding a few more useful notations.
It can be used in place of `markdown` as it also uses and applies it.

## Examples

### Blockquote with citation

This is currently limited to the top scope with no indentation.
Surrounding dotted lines are optional.

```md
......................................................
> You have enemies? Good. That means you've stood up
> for something, sometime in your life.
-- Winston Churchill
''''''''''''''''''''''''''''''''''''''''''''''''''''''
```

```html
<blockquote>
    <p>
        You have enemies? Good. That means you've stood up
        for something, sometime in your life.
    </p>
    <cite>Winston Churchill</cite>
</blockquote>
```

### Embed video

#### YouTube

```md
![dimweb](https://youtu.be/VmAEkV5AYSQ "An embedded YouTube video")
```

```html
<iframe
    src="https://www.youtube.com/embed/VmAEkV5AYSQ"
    title="An embedded YouTube video" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>
```