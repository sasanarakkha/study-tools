# common roots — Front Template

```html

<table>

    <tr valign="top">
        <td class="another_color">Pāli Root:</td>
        <td><b>{{root_clean}}</b></td>
    </tr>
    {{#sanskrit_root}}
    <tr valign="top">
        <td class="another_color">Sk Root:</td>
        <td><b>{{sanskrit_root}}</b></td>
    </tr>
    {{/sanskrit_root}}

    {{#main_verb}}
    <tr valign="top">
        <td class="another_color">Main verb:</td>
        <td>{{main_verb}}</td>
    </tr>
    {{/main_verb}}

    {{#examples}}
    <tr valign="top">
        <td class="another_color">Examples:</td>
        <td>{{examples}}</td>
    </tr>
    {{/examples}}

</table>


```
