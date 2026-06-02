# common roots — Back Template

```html
{{FrontSide}}

<hr id=answer>

<table>

    {{#marks}}
    <tr valign="top">
        <td class="another_color">My notes:</td>
        <td class="another_color"><i>{{marks}}</i></td>
    </tr>
    {{/marks}}

    <tr valign="top">
        <td class="another_color">Root info:</td>
        <td><b>{{root_clean}} {{root_group}} {{root_sign}} ({{root_meaning}})</b> {{#native}}<b>({{native}})</b>{{/native}}</td>
    </tr>

</table>

<hr>
<div class="small">{{feedback}}</div>

<span class="spacer"></span>
```
